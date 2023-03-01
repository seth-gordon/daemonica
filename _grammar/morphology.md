---
layout: grammar
title: Basic morphology and syntax
order: 2
---

### Morpheme and word classes

Daemonica morphemes may be divided into the following classes:

- free morphemes
  - nullary (noun-like)
  - unary (adjective-like)
  - binary (verb-like)
- numerals
  - digits
  - numeric constants
  - measure words
- prefixes
  - pseudo-unary (create a nullary word)
  - pseudo-binary (create a unary word)
  - pseudo-ternary (create a binary word)
  - numeric
- suffixes

The valence of a word is determined by its first syllable;
that syllable may be a prefix.

| | begins with _t, d, þ, s,_ or _š_ | any other onset |
|-|-|-|
| **_Vy_ nucleus** | unary | nullary |
| **plain _V_ nucleus** | nullary | unary |
| **any other nucleus** | nullary | binary |


Each item on the grammatical stack is called a
_predicate_. By definition, a nullary word adds one
predicate to the stack, a unary word preserves the size of
the stack, and a binary word removes one predicate from the
stack. No single word can add or remove more than one item
from the stack.

To a first approximation (and for the purpose of writing a
lexicon), nullary words are nouns; unary words are
adjectives or intransitive verbs; and valence-2 words are
transitive verbs. However, this first approximation does not tell
the whole story. For example, a single valence-0 word, being a
predicate all by itself, can be a complete sentence. Words of
higher valence cannot, because they depend on something else
being on the stack.

>- Tatorhu.
>- bear
>- There was a bear.

>- Sba-vābur.
>- NMLZ-chase
>- There was a chase.

>- *Fabur.
>- chase
>- ??? chased ???.[^2]

[^2]:
    This kind of formally ungrammatical
    construction might be used for poetic effect:
    at the opening of a horror
    story, for example.

Adverbs, phatic
expressions, and expletives can be translated as unary words.

>- Tatorhu kazu!
>- bear VOC
>- Hey, bear!

>- Tatorhu akķu þi fābur.
>- bear yesterday D2\1.EXCL chase
>- Something, which yesterday was a bear, chased me.

>- Tatorhu þi fābur akķu.
>- bear D2\1.EXCL chase yesterday
>- A bear chased me yesterday.

>- Tatorhu þi fābur, paðoybu?
>- bear D2\1.EXCL chase yield.turn
>- A bear chased me. What’s new with you?

>- Tatorhu fa-žkur þi abū, škur!
>- bear UNACC-junk D2\1.EXCL chase chaos-APPL
>- A damn bear is chasing me!

Binary words, aside from serving the same function as
transitive verbs, can also be used to add additional arguments to
a predicate, or to conjoin two predicates.

>- Þu taterhi gžur.
>- 1.EXCL D2\bear give
>- I gave something to a bear.

>- Þu taterhi düžŋģē bm gžur.
>- 1.EXCL D2\bear D3\fish D2\and give
>- I gave things to a bear and a fish.

>- Þu taterhi gžur dažŋģī kū
>- 1SG D2\bear give D2\fish OBL
>- I gave a fish to a bear.

We will see further examples of these phenomena later.

### Affixes, syllable repetition, and compounds

As mentioned previously, prefix syllables take the first vowel
of the paradigm for their word’s stack depth, while suffixes
take the last vowel. One consequence of this is that in a word
with prefixes, the earliest prefix determines its valence.

|                      |                                                       |
|----------------------|-------------------------------------------------------|
| _tatorhu_            | bear                                                  |
| _bva-tatorhu_        | is a bear                                             |
| _sba-bva-tatorhu_    | being a bear                                          |
| _sā-tatorhu_         | bear den                                              |
| _sā-bva-tatorhu_     | place where one can be a bear                         |
| _sā-zba-bva-tatorhu_ | place associated with the abstraction of being a bear |

Repeating the first syllable of a binary word switches its arguments. With
words of other valences, it creates an antonym.

>- Þu taterhi fā~vōbur.
>- 1.EXCL D2\bear PASS~chase
>- I was chased by a bear.

>- Se þi fābur ta~to:terhi kū.
>- 2 D2\1.EXCL chase D2\PASS~bear OBL
>- You chased me with bear spray.

Repeating the last syllable creates a diminutive.

>- Tator:ho~hu þi fābur.
>- bear~DIM D2\1.EXCL chase
>- A bear cub chased me.

Note that the extra syllables created by repetition are not, morphologically,
affixes: if they were, then “bear spray” would be _tatatorhu_ and “bear cub”
would be _tatorhuhu._

Close semantic variants of a word may be created by inserting weak
syllables, especially between repeated syllables.

>- Ta:dn:torhu þi fābur.
>- panda D2\1.EXCL chase
>- A panda chased me.

>- Tatorho:hŋ:hu þi fābur.
>- teddy.bear D2\1.EXCL chase
>- A teddy bear chased me.

Words may also be conjoined, with appropriate changes to their vowel structure.

>- Tatorhu spi fū þi fābur.
>- bear D2\ice ERG D2\1.EXCL chase
>- A bear from the ice chased me.

>- Tatorhozpu þi fābur.
>- polar.bear D2\1.EXCL chase
>- A polar bear chased me.

### Ergativity

Compare the following two sentences:

>- Tatorhu þi fābur.
>- bear D2\1.EXCL chase
>- A bear chased me.

>- Tatorhu þayžgu.
>- bear white
>- A bear is white.

In the case of the binary word _fābur_, the predicate at the top of the stack
is taken as the _object_ of “chase,” but in the case of the unary word _þpardū_,
the predicate at the top of the stack is taken as the _subject._ This is similar
to the pattern in languages with ergative-absolutive alignment, such as Basque,
in which the agent of a transitive verb is marked in one way (the ergative case),
and the argument of an intransitive verb and patient of an intransitive verb are
marked in a common, different way (the absolutive case). Therefore, we will
refer to the top of the stack as the “absolutive” position, and the
second-from-top as the “ergative” position; or refer to the “ergative” and “absolutive”
arguments of a word, especially if affixes have modified its arguments; or, in
writing out a definition, use “[A]” and “[E]” as placeholders for its arguments.

### Quotation

A quoted phrase, in Daemonica or any other language, is treated
as a single predicate, regardless of its morphology. The speaker
will use pitch, breathiness, or some other pattern of intonation to
distinguish
quoted phrases from the rest of the sentence.

>- Tatorhu “þu si gģur,” bzū.
>- bear <u>1.EXCL D2\2 eat</u> say
>- <q>I’m going to eat you,</q> the bear said.

>- ?“Bear” “tatorhu” bzābzū.
>- <u>“bear”</u> <u>bear</u> mean
>- <q>Bear</q> (in English) means <q>tatorhu</q> (in Daemonica).

>- Sba-bzābzū “bear” fū “tatorhu” pur.
>- NMLZ-say <u>“bear”</u> ERG
  <u>bear</u> ABS
>- <q>Bear</q> (in English) means <q>tatorhu</q> (in Daemonica).

The third construction above is preferred over
the second, because it is more clearly a sentence
with two short quotations rather than one longer one. Note that
in both these examples, _tatorhu_ appears in its citation
form, the form used for a depth-1 stack, even though, if it were
unquoted, it would be in its depth-2 _taterhi_ inflection.
