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
balance of voiced and unvoiced plosives.
Valence-0 words and valence-reducing affixes must have more
unvoiced than voiced plosives; valence-2 words and
valence-increasing affixes must have more voiced than unvoiced
plosives; all other words must either have no plosives at
all, or an equal balance of voiced and unvoiced. If prefixes
and/or suffixes change the valence of their root, the combined
word must have a balance of voiced and unvoiced plosives
appropriate to the new valence; if necessary, an affix may be
repeated to create this balance. Repetition of an affix does
not change its meaning.

>- Tu kšu-du.
>- 2SG star-APPL
>- You are a star.

>- Tu tatorhu-dudu.
>- 2SG bear-APPL
>- You are a bear.

>- Tu tatorho-þpordū-dudu.
>- 2SG bear-white-APPL
>- You are a polar bear.

Two words may be
conjoined to create a new word stem. The valence of the combined
word is determined by the
balance of all the plosives put together. Vowel patterns can be
used to distinguish a stem formed in this way from a stem plus an
affix, or two distinct words.

>- tatorhu þpardū
>- bear white
>- a white bear

>- tatorhoþpordū
>- bear:white
>- a polar bear

>- skahmvu-ðū
>- planet-two
>- two planets

>- skahmvoðū
>- planet:two
>- a double-planet system

>- mzā-skahmvoðū
>- PN-planet:two
>- Earth


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

A Daemonica word stem is either a single free morpheme, or a
sequence of conjoined morphemes that begin and end with free
morphemes. If an affix is in the middle of this latter sequence,
it is treated as an irreducible part of the stem, not a particle
with grammatical
effect.

>- þahodor-vō-porhnpu
>- grind-TEL-meat
>- hamburger

>- þahodor-vō-porhnpu-vū
>- grind-TEL-meat-TEL
>- a finished hamburger

>- *þahodor-porhnpu
>- grind-meat
>- ???

When a word has multiple prefixes and/or suffixes, the cumulative
meaning is determined, first by applying the semantics-changing
prefixes, from right to left; then by applying the suffixes, from
left to right; then by applying the stack-changing prefixes, from
left to right. Stack-changing prefixes appear first in the word,
even though they are applied last. As we have seen, the vowel
inflection indicating stack depth is based on the valence of the
entire word, and is applied to all morphemes of the word,
including constituents which, themselves, have a different valence.


>- Tatorhu pi abū-ðū.
>- bear D2\1SG chase-two
>- A bear chased me, twice.

>- Tatorhu pi abū-ðū-vū.
>- bear D2\1SG chase-two-TEL
>- A bear chased me twice, culminating in my capture.

>- Tatorhu pi abū-vū-ðū.
>- bear D2\1SG chase-TEL-two
>- A bear caught me twice.

>- Tatorhu pi abū-vū þū.
>- bear D2\1SG chase-TEL two
>- I was caught by a bear, twice (not necessarily the same
      bear both times).

>- Tatorhu pi mzar-habū-vū-ðū.
>- bear D2\1SG SWAP-chase-TEL-two
>- I caught a bear twice.

>- Tatorhu pi mzar-šar-habū-ðū.
>- bear D2\1SG SWAP-NEG-chase-two
>- In two instances, I did not chase a bear.

>- Tatorhu pi mzar-šar-tŋda-habū-vū-ðū.
>- bear D2\1SG SWAP-NEG-CANON-chase-two
>- In two instances, I did not, _strictly speaking_, chase
  a bear.

>- *Tatorhu pi šar-mzar-tŋda-habū-vū-ðū.
>- bear D2\1SG NEG-SWAP-CANON-chase-TEL-two
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
>- ??? chased ???.[^1]


[^1]:
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

>- Tatorhu pi abū, fmfpu-du!
>- bear D2\1SG chase blood-APPL
>- A bear is chasing me, dammit!

Valence-2 words, aside from serving the same function as
transitive verbs, can also be used to add additional arguments to
a predicate. Some words in the valence-2 class also serve the
function of conjunctions.

TODO these have subject and object swapped?

>- Tatorhu pi dāfbū.
>- bear D2\1SG give
>- I gave something to a bear.

>- Tatorhu dāfbū dzu pi dāfbū.
>- bear D2\fish and D2\1SG give
>- I gave things to a bear and a fish.

>- Tatorhu pi dāfbū tatŋði sdu tahēhi dahu.
>- bear D2\1SG give D2\fish OBL
  D2\hand INS
>- I handed a fish to a bear.

We will see further examples of these phenomena later.

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