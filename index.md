## A language of demons

### Introduction

One of the more obscure records of the Inquisition refers to a cell
of heretics who spoke among each other using “a language of demons
[_lingua daemonica_], which no pious man can endeavor to
learn without going mad.” The NKVD, surveilling suspected
nationalists in Ukraine and the Baltics, transcribed some furtive
conversations which corresponded to no known Slavic language; the
speakers of this language were accused of sending coded messages
to counter-revolutionaries, and summarily executed. Contemporary
signals intelligence, by both Eastern and Western agencies, has
collected enough samples of this language to develop a phonology
and a list of words, but the few cryptanalysts and linguists who
have studied it have not been able to deduce a lexicon or a grammar.

The reason for their frustration, and for the Inquisition’s
accusations of heresy, is that the fundamental structure of
Daemonica[^1] is
unlike that of any natural human language. In other
languages, a complete sentence is a sequence of words that can be
parsed into a recursive, tree-like structure. In Daemonica, every
utterance-in-progress is associated with a notional
_stack_[^2], on which predicates can be added,
modified, and
removed, until a single predicate remains and the speaker yields
their turn.

[^1]:
    The endonym for Daemonica is
    _tāzbabzū_, “our language,” but even its native
    speakers admit that “Daemonica” has a certain cachet.

[^2]:
    Daemonica is inspired by Jeffrey
    Henning’s award-winning conlang, [Fith](https://www.frathwiki.com/Fith).
    _Þu davbī dðiy šüvbe gģe kši pm._

For very simple sentences, this makes Daemonica resemble an SOV
language:

>- Tatorhu þi-bi fābur.
>- bear D2\1.EXCL-DU chase
>- A bear chased[^3] both of us.

[^3]:
    Aspect and tense will be discussed below. In
    general, Daemonica words are unmarked as to both; these
    English translations will use whatever verb form makes the
    most sense in context, which would usually be the simple past.

When words are used out of their canonical order, or when the
same word is used as an argument more than once, prefixes can be
used to change the word’s valence, invert the argument order, or
manipulate the stack:

>- Sba-dðuy   tn     tütærhe pir    fi      þe-be          pir    fābur.
>- NMLZ-young D2\DUP D3\bear D2\ABS D2\SWAP D3\1.EXCL-DU   D2\ABS chase
>- A bear, who is young like we are, chased us.

>- Þu ķu-tþur taterhi se aybir fū.
>- 1.EXCL far-IRR D2\bear D3\2 D2\choice.or ERG
>- I don’t have to outrun the bear; I just have to outrun you.

Every word is inflected, by changing its vowels, to indicate the
current depth of the stack: hence _tatorhu_
vs. _taterhi_ vs. _tütærhe_.

Daemonica casual conversation heard by a person for whom recursive linguistic
structures cause the short-term memory to balk at four stack levels
induce frustration even when typical for it. True adepts can speak fluently to
a depth of over twenty levels. The community of Daemonica
speakers is partly a secret society, in which proficiency in this
language is the coin of admission, and partly an ethnic group,
because only those who possess a rare genetic trait have any hope
of speaking it proficiently at all.

At this point, you, like the
priests of the medieval Inquisition or the analysts of Stalin’s
NKVD, might fancy a stiff drink.

### Reference grammar

{% assign gpages = site.grammar | sort: "order" %}
{% for page in gpages %}
- [{{ page.title }}]({{ site.baseurl }}{{ page.url }})
{% endfor %}

### Sample texts

{% assign tpages = site.texts | sort: "order" %}
{% for page in tpages %}
- [{{ page.title}}]({{ site.baseurl }}{{ page.url }})
{% endfor %}

### Other

- [Lexicon]({{ site.baseurl }}/lexicon)
- [Colophon]({{ site.baseurl }}/about)
