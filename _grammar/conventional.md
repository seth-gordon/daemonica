---
layout: grammar
title: Translations of conventional grammatical structures
order: 3
---

The rules described above for manipulating the stack comprise
almost all of Daemonica’s grammar. Most other expressions that
require special grammatical forms in other languages are
accomplished lexically in Daemonica.

### Deixis, demonstratives, and determinacy

The valence-1 words _ū, ur, ahu_ are the proximal, medial,
and distal demonstratives. In highly casual speech, _ur_, or
_urkur_, its valence-0 form, can be
used to refer to a predicate that used to be on the stack; this is
the closest Daemonica comes to having a third-person pronoun or
a specific determiner.

>- Tatorhu ahu pi abū.
>- bear DIST D2\1SG chase
>- Yonder bear is chasing me.

>- Ū-kur azu
>- PROX-NMLZ big
>- This is big.

>- Tatorhu pi abū; ir-kir dntši dzu.
>- bear D2\1SG chase D2\MED-NMLZ big and
>- A bear chased me; it was young. (casual)

>- Tatorhu pi abū; taterhi ir dntši dzu.
>- bear D2\1SG chase D2\bear D2\MED
  D2\young and
>- A bear chased me; the bear was young. (casual)

>- Tatorhu rta-hī pe abī; mzar-dntši dzu.
>- bear D2\COPY-PROX D3\1SG D2\CHASE D2\SWAP-young and
>- A bear chased me; it was young.

In the last example, _rta-hī_ copies the top word on the stack
and points to it (“this bear”), so that it can be the subject
of the next phrase, _…pe abī_. Copying the stack item to create
the subject and going directly to the object, _tatorhu rtü-pe abī,_
would be ungrammatical, because it would have a depth-3 word
immediately follow a depth-1 word.

### Valence-changing suffixes

#### kur (nominalizer)

This is the generic nominalizer: it reduces
the valence of the word it is attached to by one.
When a valence-0 word is nominalized, it becomes an
abstraction. Thus:


|                |                                    |
|----------------|------------------------------------|
| _tatorhu_      | bear                               |
| _tatorhu-kur_  | bear-ness                          |
| _dntšu_        | [A] is young                       |
| _dntšu-kur_    | youth                              |
| _þū_           | two of [A]; [A], twice             |
| _þū-kur_       | two (the number)                   |
| _abū_          | [E] chases [A]                     |
| _abū-kur_      | [A] either chases or is chased     |
| _dāfbū_        | [E] gives something to [A]         |
| _dāfbū-kurkur_ | [A] is either a donor or recipient |

Note the ambiguity of _abūkur_ and _dāfbūkurkur_.
This is true whenever a valence-2 word is modified with _kur_:
the absolutive and ergative arguments are collapsed into the
absolutive argument.

#### tū (passive)

This nominalizer is similar to the passive voice in a more
conventional language. Applied to a valence-2 word, it drops the
ergative argument (the subject), so the modified word only takes
the absolutive argument. Applied to a valence-1 word, it refers to
another word’s absolutive argument. It is also used to
metaphorically extend valence-0 words.

|              |                               |
|--------------|-------------------------------|
| _tatorhu_    | bear                          |
| _tatorhu-tū_ | prey for bears                |
| _dntšu_      | [A] is young                  |
| _dntšu-tū_   | young person                  |
| _þū_         | two of [A]; [A], twice        |
| _þū-tū_      | something that comes in pairs |
| _abū_        | [E] chases [A]                |
| _abū-tū_     | [A] is chased                 |
| _dāfbū_      | [E] gives something to [A]    |
| _dāfbū-tūtū_ | [A] receives a gift           |

#### pū (antipassive)

This is the anti-passive: instead of dropping the ergative
argument of a valence-2 word, it drops the absolutive argument
and promotes the ergative argument to its place. With other words,
it means “agent related to…”

|              |                                                               |
|--------------|---------------------------------------------------------------|
| _tatorhu_    | bear                                                          |
| _tatorhu-pū_ | bear expert                                                   |
| _dntšu_      | [A] is young                                                  |
| _dntšu-pū_   | elixir of youth; stimulant                                    |
| _þū_         | two of [A]; [A], twice                                        |
| _þū-pū_      | binary relationship; something that creates pairs; adding two |
| _abū_        | [E] chases [A]                                                |
| _abū-pū_     | [A] chases                                                    |
| _dāfbū_      | [E] gives something to [A]                                    |
| _dāfbū-pūpū_ | [A] gives                                                     |

#### putur (infinitive)

This removes _both_ arguments of a valence-2 word, simultaneously,
or creates a higher-level abstraction for other words.
It should be contrasted with the use of _pū_ and _tū_ in succession.

|                 |                                   |
|-----------------|-----------------------------------|
| _tatorhu_       | bear                              |
| _tatorhu-putur_ | the Platonic essence of bear-ness |
| _dntšu_         | [A] is young                      |
| _dntšu-putur_   | pediatrics; pedagogy              |
| _þū_            | two of [A]; [A], twice            |
| _þū-putur_      | duality                           |
| _abū_           | [E] chases [A]                    |
| _abū-putur_     | chase (noun)                      |
| _abū-pū-tū_     | someone who chases                |
| _abū-tū-pū_     | someone who is chased             |
| _dāfbū_         | [E] gives something to [A]        |
| _dāfbū-putur_   | giving                            |
| _dāfbū-pū-tū_   | donor                             |
| _dāfbū-tū-pū_   | recipient                         |

#### du (applicative suffix)

This adds an argument. For valence-0 words, it functions as
a copula. For valence-1 words, it adds an agent. Since
valence-3 words are not allowed in Daemonica, then a valence-2
word with a _du_ suffix has an oblique argument in its
absolutive position, substituting for the usual absolutive
argument.

|                |                                      |
|----------------|--------------------------------------|
| _tatorhu_      | bear                                 |
| _tatorhu-dudu_ | [A] is a bear                        |
| _dntšu_        | [A] is young                         |
| _dntšu-du_     | [E] makes [A] young                  |
| _þū_           | two of [A]; [A], twice               |
| _þū-du_        | [E] doubles [A]; [E] plus two of [A] |
| _abū_          | [E] chases [A]                       |
| _abū-du_       | [E] chases someone towards [A]       |
| _dāfbū_        | [E] gives something to [A]           |
| _dāfbū-du_     | [E] gives [A] to someone             |

#### bur, krbur (descriptive applicative suffixes)

These derive
words for colors, sounds, and other sensory descriptions: _bur_ increases the
valence of the base word, while _krbur_ leaves it constant. These suffixes are
almost always used to produce valence-1 words; if the result is valence-2, the
ergative argument of the derived word is the experiencer who is sensing
the color or sound or other attribute.

|                   |                                                         |
|-------------------|---------------------------------------------------------|
| _tatorhu_         | bear                                                    |
| _tatorhu-burbur_  | [A] is brown                                            |
| _dntšu_           | [A] is young                                            |
| _dntšu-krbur_     | [A] looks cute                                          |
| _þū_              | two of [A]; [A], twice                                  |
| _þū-bur_          | from [E]’s perspective, [A] has a twin structure        |
| _þū-krbur_        | [A] has a twin structure                                |
| _abū_             | [E] chases [A]                                          |
| _abū-putur-bur_   | [A] is out of breath (like someone involved in a chase) |
| _dāfbū_           | [E] gives something to [A]                              |
| _dāfbū-tūtū-kbur_ | [A] wears expensive clothes (like a wealthy person)     |
| _dāfbū-pūpū-kbur_ | [A] has a sanguine attitude (like a generous person)    |

#### dmdu (oblique applicative suffix)

To valence-0 words, this adds an agent argument.
To valence-1 words, this adds an oblique argument.
To valence-2 words, this places an oblique argument in
the ergative position.

|                |                                                       |
|----------------|-------------------------------------------------------|
| _tatorhu_      | bear                                                  |
| _tatorhu-dmdu_ | [A] studies bears; [A] manages bear populations       |
| _dntšu_        | [A] is young                                          |
| _dntšu-dmdu_   | by [E]’s standard, [A] is young                       |
| _þū_           | two of [A]; [A], twice                                |
| _þū-dmdu_      | [E] plus [A] times two; [A] is measured as two of [E] |
| _abū_          | [E] chases [A]                                        |
| _abū-dmdu_     | [A] is chased towards [E]                             |
| _dāfbū_        | [E] gives something to [A]                            |
| _dāfbū-dmdu_   | [A] receives the gift [E] from someone                |


### Case

There are valence-2 words that function much like adpositions
or case markers: they add the predicate in the absolutive
position as an argument to the predicate in the ergative
position. We will now consider each of these in turn.

#### gu (absolutive)

This may be thought of as reversing the _kur_ suffix:
the predicate in the absolutive position is treated as
the absolutive argument of whatever predicate is in the
ergative position.

>- Dntšu-kur pi gu.
>- young-NMLZ D2\1SG ABS
>- I am young.

>- Abū-putur pi gu.
>- chase-NMLZ.2 D2\1SG ABS
>- I am chased.

>- Tatorhu abū-pū pi gu.
>- bear D2\chase-ANTIP D2\1SG ABS
>- A bear chases me.

>- Tatorhu pi abū ti gu.
>- bear D2\1SG chase D2\2SG ABS
>- A bear chasing me has you as its object.

The last example above is rather forced, but it illustrates how the
ergative argument of _gu_ can be any predicate, not just one with a
conveniently unoccupied slot. This can lead to grammatical but
nonsensical phrases of the “colorless green ideas sleep furiously”
variety, or poetry, or idiomatic construction.

The most important idiomatic construction involving _gu_ is the genitive:

>- Tatorhu ti gu pi abū.
>- bear D2\2SG ABS D2\1SG chase
>- Your bear chases me.

#### smdur (ergative)

This adds an ergative argument to a predicate (equivalent
to the nominative or ablative case in an Indo-European language),
or adjoins information about an agent, experiencer, or source.

>- Abū-putur taterhi smdur.
>- chase-NMLZ.2 D2\bear ERG
>- A bear chases.

>- Tu dntšu pi smdur.
>- 2SG young D2\1SG ERG
>- You make me young.

>- Tatorhu pi abū ti smdur.
>- bear D2\1SG chase D2\2SG ERG
>- It’s your fault that a bear is chasing me.

>- Tatorhu dmti-pī-tī smdur pi abū.
>- bear D2\north-ANTIP-PASS ERG D2\1SG chase
>- A bear from the South is chasing me.

#### sdu (oblique)

This word adds an oblique argument, such as an indirect object.

>- Tatorhu pi abū ti sdu.
>- bear D2\1SG chase D2\2SG OBL
>- A bear is chasing me in your direction.

>- Tu dntšu pi sdu.
>- 2SG young D2\1SG OBL
>- You seem young to me.

>- Pu taterhi dāfbū tatŋði smdur.
>- 1SG D2\bear give D2\fish OBL
>- I give a bear a fish.

#### Other case adpositions

Absolutive, ergative, and oblique cases may be marked by either
suffixes or adpositions, but other cases (or equivalents thereof)
can only be marked by adpositions.

>- Pu taterhi abū tatsir dahu.
>- 1SG D2\bear chase wood INS
>- I chased a bear with a stick.

>- Tatorhu pi abū tšarhu bahur.
>- bear D2\1SG chase rain LOC
>- A bear chased me in the rain.

>- Tatorhu pi abū fmfpi bmhu.
>- bear D2\1SG chase current ADE
>- A bear chased me near the river.

>- Šmhar-tatorhu ŋģu-du pi abū!
>- VOC-bear base-APPL D2\1SG chase
>- Woe unto you, bear, that you chase me!

>- Tatorhu ti gu-nžu pi abū šarheštir bahur-ģu.
>- Bear D2\2SG ABS-PFV D2\1SG chase D2\house LOC-INCH
>- The bear that used to be yours chased me into the house.

The last example combines case markers with aspect markers,
which we shall discuss next.

### Mood, aspect and shape

The same suffix, depending on the sort of word it is attached to,
can either denote the shape of an object or be equivalent to the
aspect or modal marker on a verb. The “shape” referred to may be
relative to space, or to time; context is required to determine
which.

#### sū (imperfective)

>- Tatorhu pi abū-zū.
>- bear D2\1SG chase-IPFV
>- A bear used to be chasing me.

>- Tatorhu tatsir-zī bahur.
>- bear D2\wood-IPFV LOC
>- A bear is on a chunk of wood.

>- Tatorhu mhu-zū.
>- bear black-IPFV
>- A bear is black in some places.

#### mhur (habitual)

>- Tatorhu pi abū-mhur.
>- bear D2\1SG chase-HAB
>- A bear keeps chasing me.

>- Tatorhu tatsir-mhir bahur.
>- bear D2\wood-HAB LOC
>- A bear is on a surface of wooden slats.

>- Tatorhu mhu-mhur.
>- bear black-HAB
>- A bear has black spots.

#### hnžu (perfective)

>- Tatorhu pi abū-hnžu.
>- bear D2\1SG chase-PRF
>- A bear chased me.

>- Tatorhu tatsir-hnžu bahur.
>- bear D2\wood-PRF LOC
>- A bear is on a log.

>- Tatorhu mhu-hnžu.
>- bear black-PRF
>- A bear is black all over.

### Mood

The suffix _hur_ is used for the irrealis mood, while the
suffix _hrvur_ is used for the modal of necessity. Both
may be used as commands; the former is the more polite form.

>- Tatorhu-hur pi abū.
>- bear-IRR D2\1SG chase
>- Something, which might have been a bear, chased me.

>- Tatorhu-hrvur pi abū.
>- bear-IMP D2\1SG chase
>- Something, which must have been a bear, chased me.

>- Tu taterhi abū-hrvur!
>- you D2\bear chase-IMP
>- Chase the bear!

>- Tatorhu abū-tū-hur.
>- bear chase-UNACC-IRR
>- The bear could be chased.

### Tense

Tense is generally inferred from context and, if context is
insufficient, from mood and aspect. There are valence-1 and
valence-2
words that can attach tense information to a predicate, but they
are usually ambiguous as to whether they refer to a time or a
place.

The metaphorical arrow of time, in Daemonica, corresponds
to the acceleration of the frame of reference. Thus, in the
simplest case, “the future” is “down.” But if one is accelerating
along a horizontal path—driving a car, for example—then “the
future” can also be the direction of that acceleration. For
someone moving along a circular path, such as a rider on a carousel
or a planet revolving around a star, “the future” is toward the
center of revolution. Taking this metaphor a step further, when
speaking of
mechanical parts, people, or bureaucratic offices arranged in
some system of control, “the future” is towards higher authority:
the engine, CEO, or Central Committee is the axis around which
all the lesser components revolve, literally or figuratively.

>- Tatorhu pi abū whur.
>- bear D2\1SG chase yesterday
>- A bear chased me yesterday, _or_  
 A bear chased me in a
  place we are accelerating away from.

>- Tatorhu pi abū, ti tütŋði abī, dngzu.
>- bear D2\1SG chase D2\2SG D3\fish chase
  after
>- A bear chased me after you chased the fish, _or_  
   A bear chased me below where you chased the fish.

>- Pi taterhi sdur.
>- bear D2\1SG before
>- I am above a bear, _or_  
   I am ruled by a bear.

The words _dngzū_ and _āhnbzū_, in a spatial
context, indicate relative changes in position, rather than
someone’s position relative to a vector of acceleration. In a
temporal context, these words describe how events or objects
affect one another, regardless of their relative positions in time.

>- Tatorhu pi dngzū.
>- bear D2\1SG approach
>- A bear is gaining on me.

>- Tartsū pi āhnbzū-hnžu.
>- boss D2\1SG recede-PRF
>- I have been demoted.

>- Tatorhu ti abū pi āhnbzū.
>- bear D2\1SG chase 1SG recede
>- You being chased by a bear does not matter much to me.

### Logic

Logical connectives are valence-2 words.

>- Tatorhu tatsir-vī drbur ahu.
>- bear D2\wood-TEL random.or DIST
>- That over there is either a bear or a tree.

>- Artur taterhi tütŋðe darhir dahoždu-hur.
>- 1PL.INCL D2\bear D3\fish D2\choice.or
  see-IRR
>- We could go see either bears or fish.

>- Tatorhu pi tütŋðe dzi ardu.
>- bear D2\1SG D3\fish D2\and eat
>- A bear is eating me and some fish.

>- Pu taterhi ahnbzu tatēhi smbu.
>- 1SG D2\bear flee D2\arm cost
>- I escaped the bear, but it bit my arm off.

>- Tatorhu tatŋði sudur pi abu.
>- bear \D2fish except \D21SG chase
>- A bear, not a fish, chased me.

>- Tatorhu pi mta-hahnbzi mzür-te abī dur.
>- bear D2\1SG D2\OVER-flee D3\SWAP-2SG D2\chase make
>- A bear is chasing you because I escaped it.

>- Tatorhu pi mta-hahnbzi mzür-te abī šdur.
>- bear D2\1SG D2\OVER-flee D3\SWAP-2SG D2\chase uphill
>- My escaping the bear might be the cause of it chasing you.

The words _drbur_ and _darhur_ both mean “or,” but
with different connotations. If a condemned prisoner is to be
shot _or_ hanged at dawn, according to the warden’s
discretion, then from the warden’s point of view, “or” is
translated as _darhur_, but from the prisoner’s point of
view, it is translated _drbur_.

The word _smbu_ is a special kind of “and,” indicating
that one thing is gained _and_ another thing is lost.

### Phatic expressions

Even phatic expressions must conform to the stack-based
grammatical structure.

#### Cussing

The word _ātsur_ has the force of the English f-word. It literally
means “vacuum,” but it is almost never used in its literal sense
(unless someone is at risk of being exposed to a literal vacuum,
in which case, an English speaker would be using the
f-word, anyway).

>- Ātsur!
>- vacuum
>- Fuck!

>- Ātsur pi abū.
>- vacuum D2\1SG chase
>- Some fucker is chasing me.

>- Tatorhu pi ātsir-du abū.
>- bear D2\1SG D2\vacuum-APPL chase
>- A bear is chasing me, and I am fucked.

>- Tatorhu ātsur-dmdu pi abū.
>- bear vacuum-OBL.APPL D2\1SG chase
>- A fucking bear is chasing me.

>- Tatorhu ātsur-dmdu pi gu.
>- bear vacuum-OBL.APPL D2\1SG APPL
>- A bear is fucking with me.

To refer politely to a literal vacuum, one can employ a euphemism.

>- Tatorhu džartfir-kir gahu.
>- bear D2\empty-NMLZ fly
>- The bear flew into space.

A milder curse, _ŋģu,_ literally means “base matter.”

>- Ŋģu pi abū.
>- junk D2\1SG chase
>- Some piece of crap is chasing me.

#### Regulatory expressions

The valence-0 word _artū_ is the conventional Daemonica
greeting. It may be
decorated with additional predicates to show the speaker’s
respect for the audience, or simply dropped to begin whatever
actually needs to be said.

A speaker can use the valence-1 word _sprdū_ to explicitly
yield their turn.

>- Artū, mdar-tatorhu pi abū, sprdū.
>- hello DROP-bear 1SG chase yield
>- Hi, a bear chased me. What’s new with you?
