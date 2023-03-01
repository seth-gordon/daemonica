from collections import defaultdict
from enum import Flag, auto
from random import choices
import yaml


def zipfchoice(*options):
    """Randomly select one of the given options according to
    Zipf's Law (in which the second item is half as likely to
    be chosen as the first, the third item is one-third as
    likely, and so on)."""
    weights = []
    for i in range(len(options)):
        weights.append(1.0 / (i + 1))
    return choices(options, weights=weights, k=1)[0]


class Phone(Flag):
    LABIAL = auto()
    DENTAL = auto()
    POST_ALV = auto()
    DORSAL = auto()
    GLOTTAL = auto()
    NASAL = auto()
    PLOSIVE = auto()
    SIBILANT = auto()
    FRICATIVE = auto()
    APPROX = auto()
    VOICED_C = auto()
    VOWEL = auto()
    LONG_V = auto()
    MIDDLE_V = auto()
    FIRST_V = auto()

    def is_voiced(self):
        return bool(self & (self.VOWEL | self.VOICED_C | self.APPROX))

    def sonorized(self):
        if self.is_voiced() or bool(self & self.GLOTTAL):
            return self
        else:
            return self | self.VOICED_C

    @classmethod
    def normalize(cls, phs: ['Phone']):
        # drop word-initial 'h'
        if phs[0] == cls.FRICATIVE | cls.GLOTTAL:
            return cls.normalize(phs[1:])
        # soften fricatives between voiced phonemes
        for i in range(len(phs)):
            if 1 <= i < (len(phs) - 1):
                left, middle, right = phs[i-1:i+2]
                if (left.is_voiced() and right.is_voiced() and
                        bool(middle & (cls.SIBILANT | cls.FRICATIVE))):
                    phs[i] = middle.sonorized()
        return phs

    @classmethod
    def valence(cls, phs: ['Phone']):
        vowel = None
        consonant = None
        for ph in phs:
            if bool(ph & (cls.VOWEL | cls.APPROX)) and vowel is None:
                vowel = ph
                if consonant is None:
                    consonant = cls.FRICATIVE | cls.GLOTTAL
                    break
            elif consonant is None:
                consonant = ph
            if vowel is not None and consonant is not None:
                break
        central_c = (bool(consonant & (cls.DENTAL | cls.POST_ALV)) and
                     bool(consonant & (cls.PLOSIVE | cls.SIBILANT | cls.FRICATIVE)))
        vy = vowel is not None and bool(vowel & cls.DORSAL)
        plain_v = vowel is not None and not bool(vowel & (cls.APPROX | cls.LONG_V | cls.DENTAL | cls.DORSAL))
        if central_c:
            return 1 if vy else 0
        else:
            return 1 if plain_v else 2


class PhoneMapper(object):
    def __init__(self):
        P = Phone
        mappings = (
            (P.NASAL | P.LABIAL, 'm'),
            (P.NASAL | P.DENTAL, 'n'),
            (P.NASAL | P.DORSAL, 'ŋ'),
            (P.PLOSIVE | P.LABIAL, 'p'),
            (P.PLOSIVE | P.LABIAL | P.VOICED_C, 'b'),
            (P.PLOSIVE | P.DENTAL, 't'),
            (P.PLOSIVE | P.DENTAL | P.VOICED_C, 'd'),
            (P.PLOSIVE | P.DORSAL, 'k'),
            (P.PLOSIVE | P.DORSAL | P.VOICED_C, 'g'),
            (P.SIBILANT | P.DENTAL, 's'),
            (P.SIBILANT | P.DENTAL | P.VOICED_C, 'z'),
            (P.SIBILANT | P.POST_ALV, 'š'),
            (P.SIBILANT | P.POST_ALV | P.VOICED_C, 'ž'),
            (P.FRICATIVE | P.LABIAL, 'f'),
            (P.FRICATIVE | P.LABIAL | P.VOICED_C, 'v'),
            (P.FRICATIVE | P.DENTAL, 'þ'),
            (P.FRICATIVE | P.DENTAL | P.VOICED_C, 'ð'),
            (P.FRICATIVE | P.DORSAL, 'ķ'),
            (P.FRICATIVE | P.DORSAL | P.VOICED_C, 'ģ'),
            (P.FRICATIVE | P.GLOTTAL, 'h'),
            (P.APPROX | P.LABIAL, 'w'),
            (P.APPROX | P.DENTAL, 'r'),
            (P.APPROX | P.DORSAL, 'y'),
            (P.VOWEL, 'u'),
            (P.VOWEL | P.LONG_V, 'ū'),
            (P.VOWEL | P.DENTAL, 'ur'),
            (P.VOWEL | P.DORSAL, 'uy'),
            (P.VOWEL | P.MIDDLE_V, 'o'),
            (P.VOWEL | P.MIDDLE_V | P.LONG_V, 'ō'),
            (P.VOWEL | P.MIDDLE_V | P.DENTAL, 'or'),
            (P.VOWEL | P.MIDDLE_V | P.DORSAL, 'oy'),
            (P.VOWEL | P.FIRST_V, 'a'),
            (P.VOWEL | P.FIRST_V | P.LONG_V, 'ā'),
            (P.VOWEL | P.FIRST_V | P.DENTAL, 'ar'),
            (P.VOWEL | P.FIRST_V | P.DORSAL, 'ay')
        )
        self.map = dict(mappings)
        self.map.update([(m[1], m[0]) for m in mappings])

    def __call__(self, value):
        if value not in self.map:
            raise ValueError('No translation for %r' % value)
        else:
            return self.map[value]


class Syllable(object):
    def __init__(self, strong=True, pos=2):
        pm = PhoneMapper()
        labialish = [pm('p'), pm('b'), pm('f'), pm('s')]
        dentalish = [pm('t'), pm('d'), pm('þ'), pm('š')]
        dorsalish = [pm('k'), pm('g'), pm('š'), pm('ķ')]
        glottalish = [pm('h')]
        if strong:
            nucleus: Phone = zipfchoice(pm('u'), pm('ū'), pm('ur'), pm('uy'))
            if pos == 0:
                nucleus = nucleus | Phone.FIRST_V
            if pos == 1:
                nucleus = nucleus | Phone.MIDDLE_V
            consonants: [Phone] = zipfchoice(labialish, dentalish, dorsalish, glottalish)
        else:
            nuclei, consonants = zipfchoice(
                ((pm('m'), pm('w')), labialish),
                ((pm('n'), pm('r')), dentalish),
                ((pm('ŋ'), pm('y')), dorsalish)
            )
            nucleus = zipfchoice(*nuclei)
        if len(consonants) == 1:
            onset = consonants
        else:
            consonant_pair: [Phone] = zipfchoice(
                [consonants[0], consonants[2]],
                [consonants[1], consonants[3]],
                [consonants[0], consonants[3]],
                [consonants[1], consonants[2]]
            )
            onset: [Phone] = zipfchoice(
                consonant_pair[0:1],
                consonant_pair[1:2],
                consonant_pair,
                consonant_pair[-1::-1]
            )
        phone_sequence: [Phone] = onset + [nucleus]
        self.phone_sequence: [Phone] = phone_sequence

    def valence(self):
        return Phone.valence(self.phone_sequence)

    def __str__(self):
        Phone.normalize(self.phone_sequence)
        pm = PhoneMapper()
        return ''.join(pm(p) for p in self.phone_sequence)


def syllables(n, strong=True):
    results = [defaultdict(int), defaultdict(int), defaultdict(int)]
    for i in range(n):
        syl = Syllable(strong=strong)
        results[syl.valence()][str(syl)] += 1
    sorted_results = [
        sorted(r.items(), key=lambda item: item[1], reverse=True)
        for r in results
    ]
    return sorted_results


def medium_words(n):
    results = [list(), list(), list()]
    for i in range(n):
        syls = [Syllable(pos=0), Syllable(pos=1), Syllable()]
        valence = syls[0].valence()
        combined_phone_sequence = (
            syls[0].phone_sequence + syls[1].phone_sequence + syls[2].phone_sequence
        )
        combined_phone_sequence = Phone.normalize(combined_phone_sequence)
        pm = PhoneMapper()
        results[valence].append(''.join(pm(p) for p in combined_phone_sequence))
    return results


def short_words(n):
    results = [list(), list(), list()]
    prefix_mappings = {
        'dar': {'da'},
        'sar': {'sa', 'sā', 'sba'},
        'škar': {'ša'},
        'þar': {'þa', 'tar', 'tā'},
        'þay': {'ba', 'fa'},
        'pfa': {'fa', 'pa', 'bva'},
        'bay': {'bar', 'dā'},
        'pfay': {'fpā', 'pa', 'pfa'},
    }
    for _ in range(n):
        syls = [Syllable(pos=0), Syllable()]
        valence = syls[0].valence()
        combined_phone_sequence = (
            syls[0].phone_sequence + syls[1].phone_sequence
        )
        combined_phone_sequence = Phone.normalize(combined_phone_sequence)
        pm = PhoneMapper()
        next_result = ''.join(pm(p) for p in combined_phone_sequence)
        for replacement, prefixes in prefix_mappings.items():
            for prefix in prefixes:
                if next_result.startswith(prefix) and next_result[len(prefix)] not in ('r', 'y'):
                    next_result = next_result.replace(prefix, replacement, 1)
                    break
        results[valence].append(next_result)
    return results


def daemo_sort_key(s):

    def _char_key(c):
        specials = {
            'ã': 'a3', 'ũ': 'u3',
            'æ': 'a2', 'ü': 'u2',
            'ā': 'a1', 'ð': 'd1', 'ē': 'e1', 'ģ': 'g1', 'ī': 'i1',
            'ķ': 'k1', 'ŋ': 'n1', 'ō': 'o1', 'š': 's1', 'þ': 't1',
            'ū': 'u1', 'ž': 'z1'
        }
        if c in specials:
            return specials[c]
        else:
            return f'{c}0'
    key = '.'.join([_char_key(c) for c in s.strip('-')])
    # prefixes and suffixes should sort after base words with the same name
    if s.endswith('-') and s.startswith('-'):
        key += '.=2'
    elif s.endswith('-'):
        key += '.-0'
    elif s.startswith('-'):
        key += '.-1'
    return key


def annotate_lexicon(input_filename, output_filename):
    pm = PhoneMapper()
    with open(input_filename, 'r') as input_file:
        lex_yaml = yaml.safe_load(input_file)
    word_count = 0
    xrefs = defaultdict(set)
    for entry in lex_yaml:
        word_count += 1
        dword: str = entry['d']
        if 'plus' in entry:
            word_count += len(entry['plus'])
        entry['key'] = daemo_sort_key(dword)
        if 'xref' in entry:
            for xword in entry['xref']:
                xrefs[xword].add(dword)
        dw = dword.strip('-')
        phones = list()
        for i in range(len(dw)):
            if i > 0 and phones and bool(phones[-1] & Phone.VOWEL) and dw[i] in ('r', 'y'):
                continue
            next_p = pm(dw[i])
            if bool(next_p & Phone.VOWEL) and i + 1 < len(dw) and dw[i + 1] in ('r', 'y'):
                next_p = pm(dw[i:i+2])
            phones.append(next_p)
        valence = Phone.valence(phones)
        if dword.endswith('-'):
            valence = '{}p'.format(valence)
        if dword.startswith('-'):
            valence = 's'
        if 'valence' not in entry:
            entry['valence'] = valence
        elif valence != entry['valence'] and entry['valence'] != 'n':
            entry['d_VALENCE_ERROR'] = '{}: computed {}, entered {}'.format(dword, valence, entry['valence'])
    for xword, xs in xrefs.items():
        for entry in lex_yaml:
            if entry['d'] == xword:
                merged = set(entry.get('xref', [])).union(xs)
                if merged:
                    entry['xref'] = sorted(list(merged), key=daemo_sort_key)
    print(f'{word_count} words')
    lex_yaml.sort(key=lambda e: e['key'])
    with open(output_filename, 'w') as output_file:
        yaml.safe_dump(lex_yaml, stream=output_file, allow_unicode=True)
