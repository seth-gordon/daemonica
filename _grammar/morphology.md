---
layout: grammar
title: Basic morphology and syntax
order: 2
---

### Morpheme and word classes

Daemonica morphemes may be divided into the following classes:

- free morphemes
  - valence-0 (noun-like)
  - valence-1 (adjective-like)
  - valence-2 (verb-like)
- numerals
  - actual numerals (digits in base-30)
  - pseudo-numerals
- prefixes
  - stack-modifying 
    - valence-reducing (copying stack items)
    - valence-preserving
    - valence-increasing (dropping stack items)
  - semantics-modifying
- suffixes
  - valence-reducing
  - valence-preserving
  - valence-increasing

The valence of a morpheme or a word must correspond with its
balance of {/b/, /d/, /g/} and {/p/, /t/, /k/} phonemes.
Valence-0 words (such as _tatorhu_, “bear”)
and valence-reducing affixes (such as _mta_, a stack-copying prefix)
must have more
in the latter group; valence-2 words (such as _abū_, “chase”) and
valence-increasing affixes must have more in the former group;
all other words must either have none at all (such as _vi_, a denominalization suffix)
or have them in equal balance (such as _dntšu_, “young”). If prefixes
and/or suffixes change the valence of their root, the combined
word must have a balance of voiced and unvoiced plosives
appropriate to the new valence; if necessary, an affix may be
repeated to create this balance. Repetition of an affix does
not change its meaning.

|word |translation | valence
|-|-|-|
| _kšu_ | star | 0 |
| _kšu-du_ | being a star | 1 |
| _tatorhu_ | bear | 0 |
| _tatorhu-dudu_ | being a bear | 1 |
| _tatorho:þpordū-dudu_ | being a polar bear | 1 |

Two words may be
conjoined to create a new word stem. The valence of the combined
word is determined by the
balance of all the plosives put together. Vowel patterns can be
used to distinguish a stem formed in this way from a stem plus an
affix,[^1] or two distinct words.

[^1]:
    In this grammar, for clarity, we use colons to separate the
    morphemes within a stem (these will usually not be glossed separately),
    and hyphens to separate affixes
    from each other and from the stem they are attached to.
    However, no form of written Daemonica makes such a distinction.


| | |
|-|-|
| _tatorhu þpardū_ | white bear |
| _tatorho:þpordū_ | polar bear |
| _skahmvu-ðū_ | two planets |
| _skahmvo:ðū_ | double-planet system |
| _mzā-skahmvo:ðū_ | Earth |


The cumulative effect of all the affixes on a
word may never give it a valence of less than 0 or more than
2; that is to say, a word can never add or remove more than one
item from the stack, and therefore, its stack-depth inflection
can never be more than one step removed from its predecessor.

>- Tatorhu pi abū.
>- bear D2\1SG chase
>- A bear chased me.

>- Tatorhu pi mdar-hrta-habū.
>- bear D2\1SG DROP-DUP-chase
>- A bear chased itself.

>- *Tatorhu pi te mdar-mdar-hrta-habū.
>- bear D2\1SG D3\2SG DROP-DROP-DUP-chase
>- A bear chased itself.

### Affix mini-grammar

We might describe the internal structure of a Daemonica word
using the following rules, in which _inflect()_ is a function
transforming the vowels of a word according to the stack depth,
and _stackPrefix,_ _semanticPrefix,_ _suffix,_ _pseudoDigit,_
and _largeDigit_ are terminals listed in the lexicon:

* _DepthInflectedWord_ → _inflect(Word)_
* _Word_ → _stackPrefix_* _semanticPrefix_* _Stem_ _suffix_*
* _Stem_ → _freeMorpheme_ | _Number_
           _Stem_ _suffix_* _semanticPrefix_* _Stem_
* _Number_ → _FirstDigit_ (_SecondDigit_ _AnyDigit_*)
* _FirstDigit_ → “šur” (0) | “u” (1) | “þū” (2) | “šu” (3) | “þu” (4)
* _SecondDigit_ → _FirstDigit_ | “sr” (5) | _pseudoDigit_
* _AnyDigit_ → _SecondDigit_ | _largeDigit_ (digits for 6 through 29)

An affix in the middle of the stem loses its
grammatical function, and simply becomes a
lexicalized part of the stem.

>- þahodor:vō:porhnpu
>- grind:telic:meat
>- hamburger

>- þahodor:vō:porhnpu-vū
>- grind:telic:meat-telic
>- a finished hamburger

>- *þahodor:porhnpu
>- grind:meat
>- ???

When a word has multiple prefixes and/or suffixes, the cumulative
meaning is determined, first by applying the semantics-changing
prefixes, from right to left; then by applying the suffixes, from
left to right; then by applying the stack-changing prefixes, from
left to right. As we have seen, the vowel
inflection indicating stack depth is based on the valence of the
entire word, and is applied to all morphemes of the word,
including constituents which, themselves, have a different valence.


>- Tatorhu pi abū-ðū.
>- bear D2\1SG chase-two
>- A bear chased me, twice.

>- Tatorhu pi abū-ðū-vū.
>- bear D2\1SG chase-two-telic
>- A bear chased me twice, culminating in my capture.

>- Tatorhu pi abū-vū-ðū.
>- bear D2\1SG chase-telic-two
>- A bear caught me twice.

>- Tatorhu pi abū-vū þū.
>- bear D2\1SG chase-telic two
>- I was caught by a bear, twice (not necessarily the same
      bear both times).

>- Tatorhu pi mzar-habū-vū-ðū.
>- bear D2\1SG SWAP-chase-telic-two
>- I caught a bear twice.

>- Tatorhu pi mzar-šar-habū-ðū.
>- bear D2\1SG SWAP-NEG-chase-two
>- In two instances, I did not chase a bear.

>- Tatorhu pi mzar-šar-tŋda-habū-vū-ðū.
>- bear D2\1SG SWAP-NEG-canonical-chase-two
>- In two instances, I did not, _strictly speaking_, chase
  a bear.

>- *Tatorhu pi šar-mzar-tŋda-habū-vū-ðū.
>- bear D2\1SG NEG-SWAP-canonical-chase-telic-two
>- ???

### Valence

Each item on the grammatical stack is called a
_predicate_. By definition, a valence-0 word adds one
predicate to the stack, a valence-1 word preserves the size of
the stack, and a valence-2 word removes one predicate from the
stack.

To a first approximation (and for the purpose of writing a
lexicon), valence-0 words are nouns, valence-1 words are
adjectives or intransitive verbs, and valence-2 words are
transitive verbs. However, this first approximation does not tell
the whole story. For example, a single valence-0 word, being a
predicate all by itself, can be a complete sentence. Words of
higher valence cannot, because they depend on something else
being on the stack.

>- Tatorhu.
>- bear
>- There is a bear.

>- Abū-putur.
>- chase-NMLZ.2
>- There is a chase.

>- *Abū.
>- chase
>- ??? chased ???.[^2]


[^2]:
    This kind of formally ungrammatical
    construction might be used for poetic effect:
    at the opening of a horror
    story, for example.

Adjectives, adverbs, and even phatic
expressions can be translated as valence-1 words.

>- Šmhar-tatorhu pi dahoždu!
>- VOC-bear D2\1SG see
>- Hey, bear, I see you!

>- Tatorhu whur pi abū.
>- bear yesterday D2\1SG chase
>- Something, which yesterday was a bear, chased me.

>- Tatorhu pi abū whur.
>- bear D2\1SG chase yesterday
>- A bear chased me yesterday.

>- Tatorhu pi abū, ŋģu-du!
>- bear D2\1SG chase chaos-APPL
>- A bear is chasing me, dammit!

Valence-2 words, aside from serving the same function as
transitive verbs, can also be used to add additional arguments to
a predicate. Some words in the valence-2 class also serve the
function of conjunctions.

>- Pu taterhi dāfbū.
>- 1SG D2\bear give
>- I gave something to a bear.

>- Pu taterhi tütŋðe dzi dāfbū.
>- 1SG D2\bear D3\fish D2\and D2\1SG give
>- I gave things to a bear and a fish.

>- Pu taterhi dāfbū tatŋði sdu tahēhi dahu.
>- 1SG D2\bear give D2\fish OBL D2\hand INS
>- I handed a fish to a bear.

We will see further examples of these phenomena later.

### Ergativity

Compare the following two sentences:

>- Tatorhu pi abū.
>- bear D2\1SG chase
>- A bear chased me.

>- Tatorhu þpardū.
>- bear white
>- A bear is white.

In the case of the valence-2 word _abū_, the predicate at the top of the stack
is taken as the _object_ of “chase,” but in the case of the valence-1 word _þpardū_,
the predicate at the top of the stack is taken as the _subject._ This is similar
to the pattern in languages with ergative-absolutive alignment, such as Basque,
in which the agent of a transitive verb is marked in one way (the ergative case),
and the argument of an intransitive verb and patient of an intransitive verb are
marked in a common, different way (the absolutive case). Therefore, we will
sometimes refer to the top of the stack as the “absolutive” position, and the
second-from-top as the “ergative” position; or refer to the “ergative” and “absolutive”
arguments of a word, especially if affixes have modified its arguments; or, in
defining a word, use “[A]” and “[E]” as placeholders for its arguments.

### Quotation

A quoted phrase, in Daemonica or any other language, is treated
as a single predicate, regardless of its morphology. The speaker
will use pitch, breathiness, or some other pattern of intonation to
distinguish
quoted phrases from the rest of the sentence.

>- “Pu ti ardu,” taterhi gur.
>- <u>1SG D2\2SG eat</u> D2\bear say
>- <q>I’m going to eat you,</q> the bear said.

>- ?“Bear” “tatorhu” gū.
>- <u>“bear”</u> <u>bear</u> mean
>- <q>Bear</q> (in English) means <q>tatorhu</q> (in Daemonica).

>- gū-pū “bear” smdur “tatorhu” adu.
>- mean-NMLZ <u>“bear”</u> SBJ
  <u>bear</u> OBJ
>- <q>Bear</q> (in English) means <q>tatorhu</q> (in Daemonica).

The third construction above is preferred over
the second, because it is more clearly a sentence
with two short quotations rather than one longer one. Note that
in both these examples, _tatorhu_ appears in its citation
form, the form used for a depth-1 stack, even though, if it were
unquoted, it would be in its depth-2 _taterhi_ inflection.
