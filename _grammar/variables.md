---
layout: grammar
title: Variables and bindings
order: 6
---
Consider this question and this ungrammatical fragment:

>- Tatorhu kapi abū fazu?
>- bear D2\WHAT chase Q
>- Who did a bear chase?

>- *Tatorhu kapi abū?
>- bear D2\WHAT chase
>- A bear chased —?

The word
_kapi_ puts a _free variable_
on the stack, and the word _fazu_
_binds_ it to create a wh-question. If there are unbound
variables on the stack, as in the second example above, the
sentence is not complete.

**TODO** make forall/exists pseudo-numerals instead?

The word _fazu_ binds a variable by associating it with
“the thing the speaker is asking about.” It can also be bound
with a universal quantifier using _nhu_, or an existential
quantifier with _ŋžu_.

>- Kapu pi abū nhu.
>- WHAT D2\1SG chase FORALL
>- Everything chases me.

>- Kapu azu pi abū ŋžu.
>- WHAT big D2\1SG chase EXISTS
>- Something big chases me.

>- Kapu kapi ŋži abū nhu.
>- WHAT D2\WHAT D2\EXISTS chase FORALL
>- Everything chases something.

>- Tatorhu padur.
>- bear good
>- A bear is good.

>- Kapu tatorhu-du padur ŋži.
>- WHAT bear-APPL good EXISTS
>- Some bear is good.

>- Kapu tatorhu-du ŋži padur.
>- WHAT bear-APPL EXISTS good
>- The existence of at least one bear is good.

>- Kapu tatorhu-du padur nhu.
>- WHAT bear-APPL good FORALL
>- All bears are good.

>- Kapu tatorhu-du nhu padur.
>- WHAT bear-APPL FORALL good
>- The existence of all bears is good.

A variable can also be bound to a particular predicate.

>- Tatorhu kapi abū pi rdū.
>- bear D2\WHAT chase D2\1SG BIND
>- A bear chased someone, who was me.

When a variable is placed on the stack, all copies of it refer to
the same thing.

>- Kapu-pū taterhi mta-gi ürter-ðē mhar-gi abū fazu?
>- WHAT-NMLZ D2\bear D2\OVER-DNMLZ
  D3\1PL-two D2\ROLL-DNMLZ chase Q
>- What quality do we both share with the bear who chased us?

When there are multiple free variables and multiple binding
words in the same utterance, the variables are bound in the
reverse of the order in which they were declared. One can
imagine the directory of unbound variables as forming a stack
of its own, independent of what we have been calling “the stack.”[^1]
However, there are no grammatical particles for copying or rearranging
items on this other stack.

[^1]:
    Those who have learned the Forth programming language may recall its
    distinction between the “data stack” and the “return stack.”

>- Kapu kapi abū fazu fazu?
>- WHAT D2\WHAT chase Q Q
>- Who chased whom?

>- Kapu kapi mta-gi ürter-ðē mhar-gi
    abū taterhi rdū fazu?
>- WHAT D2\WHAT D2\OVER-DNMLZ
      D3\1PL-two D2\ROLL-DNMLZ chase
    D2\bear WHAT Q
>- What quality do we both share with the one who chased us,
        namely, the bear?

Free-variable markers exist for all three valences; there is
also a special marker for (valence-1) quantities.

>- Tatorhu ahur ti abū fazu?
>- bear HOW D2\1SG chase Q
>- What kind of bear chased you?

>- Tatorhu ti du fazu?
>- bear D2\1SG DO Q
>- What did a bear do to you?

>- Tatorhu mhur ti abū fazu?
>- bear HOW.MUCH D2\1SG chase Q
>- How many bears chased you?

If one simply wants to use a placeholder word to indicate some
arbitrary thing, quality, or action, there is no need to
combine free variables with _ŋžu_; there are special
words for this purpose.

>- Pazu azu pi abū.
>- something big D2\1SG chase
>- Something big chases me.

>- Tatorhu padu pi abū.
>- bear somehow D2\1SG chase
>- Some kind of bear chased me.

>- Tatorhu azu pi bazu.
>- bear big D2\1SG some.action
>- A big bear did something to me.

>- Pazu padu pazi bazu.
>- something somehow D2\something some.action
>- Some kind of something did something to something else.

_Pazu padu pazi bazu_ is a Daemonica catchphrase which might
be translated, more idiomatically, as “Stuff’s going on.” It may
be said in a casual, anticipatory, or dejected tone of voice,
depending on the nature of that “stuff.”

While free variables may be used for words of all three valences,
the word binding them,
_rdū_, is always valence-2. Therefore, the single
predicate at the top of the stack must be interpreted as the one
binding the nearest free variable, regardless of the variable’s
valence.

>- *Tatorhu ahur pi abū mhu rdū.
>- bear HOW D2\1SG chase black BIND
>- ???

>- Tatorhu ahur pi abū mhi rta-rdū.
>- bear HOW D2\1SG chase D2\black DUP-BIND
>- The event of a bear chasing me was as black as the bear itself.

>- Tatorhu ahur pi abū mhi-pī rdū.
>- bear HOW D2\1SG chase D2\black-NMLZ BIND
>- The bear that chased me was black.

In the first example above, _tatorhu ahur pi abū mhu_
creates a single stack item, meaning, roughly, “The event of a
— bear chasing me was black.” Since _rdū_ is a valence-2
word, it cannot be used when the stack contains a single item:
that would be just as ungrammatical as _pi abū_, “— chased
me.” If one really wants to bind a
variable recursively, the second example shows how to do
it, but the third is more likely to be what the
speaker intended.

If word denoting a free variable has suffixes and/or
semantics-changing prefixes, they
are applied to give its meaning when the variable is bound. This
also provides a way to apply grammatical operations that normally
operate on a single word to an entire phrase.

>- Šar-kapu ti abū fazu?
>- NEG-WHAT D2\1SG chase Q
>- What _didn’t_ chase you?

>- Fa-kapu taterhi mhi rdū pi abū.
>- approx-WHAT D2\bear D2\black
  BIND D2\1SG chase
>- A sort-of-black-bear chased me. (Not a bear that was
  sort-of-black, but a borderline instance of the class 
  <q>black bear.</q>)

When a variable is bound, every instance of that variable in
the stack is bound, not just instances that appear at the top
of the stack. Because binding does not work like regular stack
operations, binding words can even precede the variables they
reference: this construction is marked, but grammatical.

>- Tatorhu fazu ti du?
>- bear Q D2\1SG DO
>- What the hell did a bear do to you?

>- Kapu pi tütærhe rdī abū.
>- WHAT D2\1SG D3\bear D2\BIND chase
>- Something chased—it was a bear, it chased me.

>- Kapu kapi fazi mta-gi dntše-pē
    rdī ürter-ðē mhar-gi abū.
>- WHAT D2\WHAT D2\Q
    D2\OVER-DNMLZ D3\young-NMLZ
    D2\BIND D3\1PL-two
    D2\ROLL-DNMLZ chase
>- Something (what was that thing?) fitting a certain
    description, that description being <q>young,</q> which
    also applies to us, chased us.

The last example above might best be explained word by
word. In the translations below, X and Y are the free variables.

<dl>
<dt>Kapu</dt> <dd>X</dd>
<dt>Kapu kapi</dt> <dd>X / Y</dd>
<dt>Kapu kapi fazi</dt> <dd>X / What thing?</dd>
<dt>Kapu kapi fazi mta-vi</dt> <dd>X / What is (described by the
attribute) X?</dd>
<dt>Kapu kapi fazi mta-vi dntše-pē</dt>
<dd>X / What is X? / youth</dd>
<dt>Kapu kapi fazi mta-vi dntše-pē rdī</dt>
<dd>youth / What is a young creature?</dd>
<dt>Kapu kapi fazi mta-vi dntše-pē rdī ürter-ðē</dt>
<dd>youth / What is a young creature? / we two</dd>
<dt>Kapu kapi fazi mta-vi dntše-pē rdī ürter-ðē
mhar-vi</dt>
<dd>What is a young creature? / we two youths</dd>
<dt>Kapu kapi mzar-fazi mta-vi dntše-pē
rdī ürter-ðē mhar-vi abū.</dt>
<dd>What young creature chased us two youths?</dd>
</dl>

Note, in particular, the line _Kapu kapi fazi mta-vi
dntše-pē rdī._ Even though _rdū_ (_rdī_, as
inflected) is a valence-2 word, the replacement of “X” happened
throughout the stack, not simply on the items that a valence-2
word normally is restricted to affecting.

Perhaps, at this point, you would like another drink.
