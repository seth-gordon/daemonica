---
layout: grammar
title: Variables and bindings
order: 5
---

Consider this question and this ungrammatical fragment:

>- Tatorhu šku fābur pu?
>- bear D2\what chase WH.Q
>- Who did the bear chase?

>- *Tatorhu šku fābur?
>- bear D2\what chase
>- A bear chased —?

The word
_šku_ puts a _free variable_
on the stack, and the word _pu_
_binds_ it to create a wh-question. If there are unbound
variables on the stack, as in the second example above, the
sentence is not complete.

A variable can also be bound to a particular predicate.

>- Tatorhu šku fābur þi gū.
>- bear D2\what chase D2\1.EXCL bind
>- A bear chased someone, who was me.

When a variable is placed on the stack, all copies of it refer to
the same thing.

>- Šku   tn     tütærhe pir    fi      þe-be          pir    fābur pu?
>- what  D2\DUP D3\bear D2\ABS D2\SWAP D3\1.EXCL-DU   D2\ABS chase WH.Q
>- What do we have in common with the bear that chased us?

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

>- Šku ški fābur pu pu?
>- what D2\what chase Q Q
>- Who chased whom?

>- Šku   tn     bve     pir    fi      þe-be          pir    fābur taterhi gū   pu?
>- what  D2\DUP D3\what D2\ABS D2\SWAP D3\1.EXCL-DU   D2\ABS chase D2\bear bind WH.Q
>- What do we have in common with the one who chased us, namely, the bear?

Free-variable markers exist for all three valences. To make a variable
for a quantity, put a numeric prefix in front of _šku._

>- Tatorhu bvu si fābur pu?
>- bear how D2\2 chase WH.Q
>- What kind of bear chased you?

>- Tatorhu si ķgū pu?
>- bear D2\2 do.what Q
>- What did a bear do to you?

>- Tatorhu pa-žku si fābur pu?
>- bear D2\numeric.1-what D2\2 chase Q
>- How many bears chased you?

>- Tatorhu pa-žku þi fābur tr-habī gū
>- bear D2\numeric.1-what D2\1.EXCL chase D2\numeric.0-long bind
>- I was chased by some number of bears, a large number.

Note that the free variable _pa-žku_ is unary, but the word
used to bind it, _tr-habū,_ is nullary. The absolutive argument of _gū,_ the binding
particle, must be a single predicate. Preceding _gū_ with a unary
or binary word may lead to unexpected results, if not outright bad grammar.

>- Tatorhu bvu þi fabūr þdiy gū.
>- bear how D2\1.EXCL chase black bind
>- A bear chased me; it was a black–(…-bear-chasing-me) bear.

In the above example, _tatorhu bvi þi fabūr_ is an almost-complete
sentence: “a — bear chased me.” Because _þdiy_ is unary, it modifies
the entire sentence: “the event of a — bear chasing me was black.”
The final _gū_ binds that sentence to the free variable within it:
“the event of a (the event of a (the event of a (…)-type bear was
black)-type bear was black)-type bear was black.”

The speaker of that sentence probably meant to say this:

>- Tatorhu bvu þi fabūr sba-ðdiy gū.
>- bear how D2\1.EXCL chase D2\NMLZ-black bind
>- The bear that chased me was black.

If word denoting a free variable has suffixes and/or
semantics-changing prefixes, they
are applied to give its meaning when the variable is bound. This
also provides a way to apply grammatical operations that normally
operate on a single word to an entire phrase.

>- Šku-žu si fabūr pu?
>- what-NEG D2\2 chase WH.Q
>- What _didn’t_ chase you?

>- Šku-bur fāðir þu taterhi se fabīr gū.
>- what-MED D2\sadden 1.EXCL D2\bear D3\2 D2\chase bind
>- I was depressed by that event of a bear chasing you.

>- Sardður bvu ķū taterhi þe fabīr gū.
>- dirt how wet D2\bear D3\1.EXCL D2\chase bind
>- The dirt is wet; it is bear-chasing-me dirt.

(The last of these examples could be rephrased as
_sardður taterhi þe fabīr fi pur ķū._)

When a variable is bound, every instance of that variable in
the stack is bound, not just instances that appear at the top
of the stack. Because binding does not work like regular stack
operations, binding words can even precede the variables they
reference: this construction is marked, but grammatical.

>- Tatorhu pu si ķgū?
>- bear WH.Q D2\2 do.what
>- What the heck did a bear to do you?

>- Šku þi tütærhe gī fabūr.
>- what D2\1.EXCL D3\bear D2\bind chase
>- Something did to me—it was a bear, it chased me.

>- Šku ški ķgī ške tn psu per fe pse spü-dþuy gē
   pir tē gī fabūr.
>- what D2\what D2\WH.Q D3\how D4\COPY D4\PICK D3\ABS D3\SWAP D3\ROLL D4\NMLZ-young D3\bind 
   D2\ABS D3\1.INCL D2\bind chase
>- Something (what was that thing?) fitting a certain
    description, that description being <q>young,</q> which
    also applies to us, chased us.

The last example above might best be explained word by
word. In the translations below, X, Y, and Z are the free variables,
and the slashes divide the items on the stack.

<dl>
<dt>Šku</dt> <dd>X</dd>
<dt>Šku ški</dt> <dd>X / Y</dd>
<dt>Šku ški ķgi</dt> <dd>X / What thing?</dd>
<dt>Šku ški ķgī ške</dt> <dd>X / What thing? / Z</dd>
<dt>Šku ški ķgī ške tn</dt>
<dd>X / What thing? / Z / Z</dd>
<dt>Šku ški ķgī ške tn psu</dt>
<dd>X / Z / Z / What thing?</dd>
<dt>Šku ški ķgī ške tn psu per</dt>
<dd>X / Z / What Z-ish thing?</dd>
<dt>Šku ški ķgī ške tn psu per fe</dt>
<dd>X / What Z-ish thing? / Z</dd>
<dt>Šku ški ķgī ške tn psu per fe pse</dt>
<dd>What Z-ish thing? / Z / X</dd>
<dt>Šku ški ķgī ške tn psu per fe pse spü-dþuy</dt>
<dd>What Z-ish thing? / Z / X / youth</dd>
<dt class="highlight">Šku ški ķgī ške tn psu per fe pse spü-dþuy gē</dt>
<dd>What young thing? / youth / X</dd>
<dt>Šku ški ķgī ške tn psu per fe pse spü-dþuy gē pir</dt>
<dd>What young thing? / young X</dd>
<dt>Šku ški ķgī ške tn psu per fe pse spü-dþuy gē pir tē</dt>
<dd>What young thing? / young X / us</dd>
<dt>Šku ški ķgī ške tn psu per fe pse spü-dþuy gē pir tē gī</dt>
<dd>What young thing? / we, who are young</dd>
<dt>Šku ški ķgī ške tn psu per fe pse spü-dþuy gē pir tē gī fabūr.</dt>
<dd>Some young thing (what?) chased us, who are young.</dd>
</dl>

Note, in particular, the effect of the word _gē_ in the highlighted line.
It binds Z, the most-recently-created free variable,
even though X was above Z in the stack, and it binds both instances
of Z at once.

Perhaps, at this point, you would like another drink.
