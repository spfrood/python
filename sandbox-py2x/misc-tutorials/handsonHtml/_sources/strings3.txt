Strings, Part III
====================

.. index::
   object orientation
   string; object

.. _Object-Orientation:
    
Object Orientation
------------------

Python is an *object-oriented* language. Every piece of data and
even functions and types are objects. The term object-oriented is
used to distinguish Python from earlier languages, classified as
*procedural* languages, where types of data and the operations on
them were not connected in the language. The functions we have used
so far follow the older procedural programming syntax. In the newer
paradigm of object-oriented programming, all data are in objects,
and a core group of operations that can be done on some particular
type of object are tightly bound to the object and called the
object's *methods*.

.. index::
   string; upper
   upper string method

For example, strings are objects, and strings "know how" to
produce an uppercase version of themselves. Try in the *Shell*::

    s = 'Hello!' 
    s.upper() 

Here ``upper`` is a *method* associated with strings. This means
``upper`` is a function that is bound to the string before the dot.
This function is bound both logically, and as we see in the new
notation, also syntactically. One way to think about it is that
each type of data knows operations (methods) that can be applied to
it. The expression ``s.upper()`` calls the method ``upper`` that is
bound to the string ``s`` and returns a *new* uppercase string
result based on ``s``.

Strings are immutable, so no string method can change the original
string, it can only return a new string. Confirm this by entering
each line individually in the *Shell* to see the original s is
unchanged::

    s 
    s2 = s.upper() 
    s2 
    s 

We are using the new object syntax:

    *object*\ ``.``\ *method*\ ``( )``

meaning that the *method* associated with the object's type is
applied to the *object*. This is just a special syntax for a
function call with an object.

.. index::
   string; lower
   lower string method

Another string method is ``lower``, analogous to upper, but
producing a lowercase result.

*Test yourself*: How would you write the expression to produce a
lowercase version of the string ``s``? Answer: [#]_

Try it in the *Shell*. 

*Test yourself in the Shell*: How would you use this string
``s`` and both the ``lower`` and ``upper`` methods to create
the string ``'hello!HELLO!'``? Hint: [#]_  Answer: [#]_

.. index::
   method; . syntax
   single: .; method syntax

Many methods also take additional parameters between the
parentheses, using the more general syntax:

    *object*\ ``.``\ *method*\ ``(``\ parameters\ ``)``

The first of many such methods we will introduce is ``count``:

.. index::
   string; count
   count string method

Syntax for ``count``:

    *s*.count(*sub*)

Count and return the number of repetitions of a string *sub* that
appear as substrings inside the string ``s``.

*Read* and make sure you see the answers are correct::

    >>> tale = 'This is the best of times.' 
    >>> tale.count('i') 
    3
    >>> tale.count('is') 
    2 
    >>> tale.count('That') 
    0 
    >>> tale.count(' ')  
    5 

There is a blank between the quotes in the line above. Blanks are
characters like any other (except you can't see them)!

Just as the parameter can be replaced by a literal or any
expression, the object to which a method is bound with the dot may
also be given by a literal, or a variable name, or any expression
that evaluates to the right kind of object in its place. This is
true for any method call.

.. index::
   single: .; method precedence
   precedence; . for method

Technically the dot between the object and the method name is an
operator, and operators have different levels of precedence. It is
important to realize that this dot operator has the *highest*
*possible* precedence. *Read* and see the difference parentheses
make in the expressions::

    >>> 'hello ' + 'there'.upper() 
    'hello THERE'
    >>> ('hello ' + 'there').upper() 
    'HELLO THERE' 

To see if you understand this precedence, predict the results of
each line and then test in the *Shell*::

    3 * 'X'.count('XXX') 
    (3 * 'X').count('XXX') 

There are 0 'XXX's in 'X', but 1 'XXX' in 'XXX'.

.. index::
   method; dir
   dir for method list

Python lets you see all the methods that are bound to an object
(and any object of its type) with the built-in function ``dir``. To
see all string methods, supply the ``dir`` function with any
string. For example, try in the *Shell*::

    dir('')

Many of the names in the list start and end with two underscores,
like __add__. These are all associated with methods
and pieces of data used internally by the Python interpreter. You
can ignore them for now. The remaining entries in the list are all
user-level methods for strings. You should see ``lower`` and
``upper`` among them. Some of the methods are much more commonly
used than others.

Object notation

    *object*\ ``.``\ *method*\ ``(``\ parameters\ ``)``

has been illustrated so far with just the object type ``str``, but
it applies to all types. Later in the tutorial methods such as the
following will be discussed:

If ``seq`` is a ``list``, ``seq.append(element)`` appends
``element`` to the end of the list.

If ``myData`` is a ``file``, ``myData.read()`` will read and return
the entire contents of the file....

.. index::
   string; index
   index; string [ ]
   single: []; string indexing
                           
.. _String-Indices:

String Indices
--------------

A string is a sequence of smaller components (individual
characters), and it is often useful to deal with parts of strings.
Python *indexes* the characters in a string, starting from 0, so
for instance, the characters in the string ``'computer'`` have
indices:

+-----------+----+----+----+----+----+----+----+----+
| character |  c | o  |  m |  p |  u |  t |  e | r  |
+-----------+----+----+----+----+----+----+----+----+
| index     |  0 | 1  |  2 |  3 |  4 |  5 |  6 | 7  |
+-----------+----+----+----+----+----+----+----+----+
| index     |  0 | 1  |  2 |  3 |  4 |  5 |  6 | 7  |
+-----------+----+----+----+----+----+----+----+----+

Each index is associated with a character, and you reference the
individual characters much like in a dictionary. Try the following.
(You can skip the comments that make the indices explicit.) Enter
in the *Shell*::

    #    01234567 
    s = 'computer' 
    s[0] 
    s[5] 
    s[8] 

You cannot refer directly to a character that is not there. Indices
only go to 7 in the example above.

.. index::
   len function
   sequence; len function

Recall the ``len`` function, which gives the length of a sequence.
It works on strings. Guess the following value, and test in the
*Shell*::

    len(s)

A common error is to think the last index will be the same as the
length of the string, but as you saw above, that leads to an
execution error. If the length of some string is 5, what is the
index of its last character? What if the length is 35?

Hopefully you did not count by ones all the way from 0. The indices
for a string of length n are the elements of the sequence
``range(n)``, which goes from 0 through n-1, or the length of the
string minus one, which is 5-1=4 or 35-1 = 34 in these examples.

Sometimes you are interested in the last few elements of a string
and do not want to do calculations like this. Python makes it easy.
You can index from the *right* end of the string. Since positive
integers are used to index from the front, negative integers are
used to index from the right end, so the more complete table of
indices for ``'computer'`` gives two alternatives for each
character:

+-----------------+----+----+----+----+----+----+----+----+
| character       |  c | o  |  m |  p |  u |  t |  e |  r |
+-----------------+----+----+----+----+----+----+----+----+
| index           |  0 | 1  |  2 |  3 |  4 |  5 |  6 | 7  |
+-----------------+----+----+----+----+----+----+----+----+
| index from the  | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
| right end       |    |    |    |    |    |    |    |    |
+-----------------+----+----+----+----+----+----+----+----+

Predict and test each individual line, continuing in the *Shell*::

    s[-1] 
    s[-3] 
    s[-10] 
     
    it = 'horse' 
    len(it) 
    it[-1] 
    it[1]  

Be careful - remember what the initial index is!

.. index::
   string; slice [ : ]
   single: :; string slice 
   single: [ : ]; string slice
   slice [ : ];  string 
                           
.. _String-Slices:
                           
String Slices
-------------

It is also useful to extract larger pieces of a string than a
single character. That brings us to *slices*. Try this expression
using slice notation, continuing in the *Shell*::

    s[0:4]

Note that s[4] is the first character *past* the slice. The
simplest syntax for a slice of a string ``s`` is:

    ``s[`` *startIndex* ``:`` *pastIndex* ``]`` 
                           
This refers to the substring of ``s`` starting at index
startIndex and stopping just *before* index pastIndex.

.. warning::
   It confuses many people that the index after the colon is *not* the
   index of the final character in the slice.  The second index is
   *past* the end of the slice.

Predict and try each line individually in the *Shell*::

    s[2:5]  
    s[1:3] 

If you omit the first index, the slice starts from the beginning.
If you omit the second index, the slice goes all the way to the
end. Predict and try each line individually in the *Shell*::

    s[:3] 
    s[5:] 
    s[:]

Predict and try each line individually in the *Shell*::

    word = 'program'
    word[2:4]
    word[1:-3]
    word[3:]
    word[3:3]
    word[:1] + word[4:]

Python evaluates slices in a more forgiving manner than when
indexing single characters. In a slice, if you give an index past a
limit of where it could be, Python assumes you mean the actual end.
Predict and try each line individually in the *Shell*::

    word[:9] 
    word[8:10] 

Enter a slice expression using the variable ``word`` from above
that produces ``'gra'``.

.. index::
   string; find method
   find string method

A useful string method that uses the ideas of indices and slices is
``find``.

Syntax options for ``find``:

    | *s*\ ``.find(``\ *sub*) 
    | *s*\ ``.find(``\ *sub*, *start*) 
    | *s*\ ``.find(``\ *sub*, *start*, *end*) 

Return the integer index in the string *s* of the beginning of
first complete occurrence of the substring *sub*. If *sub* does not
appear inside s, return -1. The value -1 would be an impossible
result if ``sub`` were found, so if -1 is returned, *sub* must
not have been found. If parameters ``start`` and
``end`` are not included in the parameter list, the search is
through the whole string ``s``. If an integer value is given
for *start*, the search starts at index *start*. If an integer
value is given for *end*, the search ends *before* index *end*. In
other words if *start* and *end* appear, then the search is through
the slice *s*\ [\ *start* : *end*], but the index returned is still
counted from the beginning of ``s``.

For example, check that the following make sense. The comment line
is just there to help you count::

    >>> #    01234567890 
    >>> s = 'Mississippi' 
    >>> s.find('i') 
    1 
    >>> s.find('si') 
    3 
    >>> s.find('sa') 
    -1 
    >>> s.find('si', 4) 
    6 

Predict and try each line in the *Shell*::

    #       0123456789012 
    line = 'Hello, there!' 
    line.find('e') 
    line.find('he') 
    line.find('e', 10) 
    line.find('he', 10)

We will consider more string methods later, but we can already do
useful things with the ones introduced.

.. index::
   help function
   function; help

Inside the Shell, you can look up documentation on any of the
methods listed with the ``dir`` function. Here is a place that you
want to *refer* to the method itself, not *invoke* the method, so
note that you get ``help`` for ``s.find`` not for ``s.find()``.
Assuming you defined the string s in the Shell earlier, try in the
*Shell* ::

    help(s.find)

The Python documentation uses square brackets to indicate optional
elements which get a default value if you leave them out. This
shortens the syntax descriptions.

If you want method documentation when you do not have a variable of
the type created, you can also use the type name. Try in the
*Shell*::

    dir(str) 
    help(str.capitalize) 

.. index::
   list; [ ] index + [ : ] slice
   single: [ : ]; list slice
   single: []; list indexing
   single: :; list slice
   slice [ : ]; list

Indexing and slicing works on any kind of Python sequence, so you
can index or slice lists also.* Read* this *Shell* session::

    >>> vals = [5, 7, 9, 22, 6, 8] 
    >>> vals[1] 
    7 
    >>> vals[-2] 
    6 
    >>> vals[1:4] 
    [7, 9, 22] 


Unlike strings, lists are mutable, as you will see in 
:ref:`Appending-to-a-list`. Indices and slices can also be used in
assignment statements to change lists, but in this tutorial we not
need list indexing, and we will not discuss this subject further.

.. index::
   index; variable
                           
.. _Index-Variables:

Index Variables
---------------

All the concrete examples in the last two sections used literal
numbers for the indices. That is fine for learning the idea, but in
practice, variables or expressions are almost always used for
indices. As usual the variable or expression is evaluated before
being used. Try in Idle and see that the example program
``index1.py`` makes sense::

    s = 'word' 
    print('The full string is: ', s) 
    n = len(s) 
    for i in range(n): 
        print() 
        print('i =', i) 
        print('The letter at index i:', s[i]) 
        print('The part before index i (if any):', s[:i]) 
        print('The part before index i+2:', s[:i+2]) 


We will use index variables in more practical situations as we
explain more operations with strings.

.. index::
   string; split method
   split; string method
   list; from string split
                           
.. _split:
                           
``split``
---------

Syntax options for the ``split`` method with a string *s*:

    | *s*\ ``.split()`` 
    | *s*\ ``.split(``\ *sep*\ ``)`` 

The first version splits *s* at any sequence of whitespace (blanks,
newlines, tabs) and returns the remaining parts of *s* as a list.
If a string *sep* is specified, it is the separator that
gets removed from between the parts of the list.

For example, read and follow::

    >>> tale = 'This is the best of times.' 
    >>> tale.split() 
    ['This', 'is', 'the', 'best', 'of', 'times.'] 
    >>> s = 'Mississippi' 
    >>> s.split('i') 
    ['M', 'ss', 'ss', 'pp', ''] 
    >>> s.split()  # no white space 
    ['Mississippi'] 

Predict and test each line in the *Shell*::

    line = 'Go:  Tear some strings apart!' 
    seq = line.split() 
    seq 
    line.split(':') 
    line.split('ar') 
    lines = 'This includes\\nsome new\\nlines.' 
    lines.split() 

.. index::
   string; join method
   join string method for list
   list; join strings
                           
.. _join:
                           
``join``
---------

Join is roughly the reverse of split. It joins together a sequence
of strings. The syntax is rather different. The separator
*sep* comes first, since it has the right type (a string).

Syntax for the ``join`` method:

    *sep*\ ``.join(``\ *sequence*\ ``)``

Return a new string obtained by joining together the
*sequence* of strings into one string, interleaving the
string *sep* between *sequence* elements.

For example (continuing in the Shell from the previous section,
using ``seq``), follow::

    >>> ' '.join(seq) 
    'Go: Tear some strings apart!' 
    >>> ''.join(seq) 
    'Go:Tearsomestringsapart!' 
    >>> '//'.join(seq) 
    'Go://Tear//some//strings//apart!' 

Predict and try each line, continuing in the *Shell*::

    '##'.join(seq) 
    ':'.join(['one', 'two', 'three']) 


The methods ``split`` and ``join`` are often used in sequence:

Underscore Exercise
~~~~~~~~~~~~~~~~~~~

Write a program ``underscores.py`` that would input a phrase
from the user and print out the phrase with the white space between
words replaced by an underscore. For instance if the input is ``the
best one``, then it would print ``the_best_one``. The conversion
can be done in one or two statements using the recent string
methods.

Acronym Exercise
~~~~~~~~~~~~~~~~
                           
\* An *acronym* is a string of capital letters formed by
taking the first letters from a phrase. For example, SADD is an
acronym for 'students against drunk driving'. Note that the acronym
should be composed of all capital letters even if the original
words are not. Write a program ``acronym.py`` that has the user
input a phrase and then prints the corresponding acronym.

To get you started, here are some things you will need to do. First
check that you understand the basic syntax to accomplish the
different individual tasks: Indicate the proper syntax using a
Python function or operation will allow you to accomplish each
task. Invent appropriate variable names for the different parts.
This is not complete instructions! the idea is to make sure you
know the basic syntax to use in all these situations. See the
questions after the list to help you put together the final
program.


#. What type of data will the input be? What type of data will the
   output be?

#. Get the phrase from the user.

#. Convert to upper case.

#. Divide the phrase into words.

#. Initialize a new empty list, ``letters``.

#. Get the first letter of each word.

#. Append the first letter to the list ``letters``.

#. Join the letters together, with no space between them.

#. Print the acronym.

Which of these steps is in a loop? What ``for`` statement controls
this loop?

Put these ideas together and write and test your program
``acronym.py``. Make sure you use names for the objects that are
consistent from one line to the next! (You might not have done that
when you first considered the syntax and ideas needed for 1-9 above
individually.)

.. _Further-Exploration:
                           
Further Exploration
-------------------

As the ``dir('')`` list showed, there are many more operations on
strings than we have discussed, and there are further variations of
the ones above with more parameters. 
Methods ``startswith``, ``endswith``, and ``replace`` 
are discussed later in :ref:`More-String-Methods`.
If you want to reach a
systematic reference from inside Idle, go to
:menuselection:`Help --> Python Docs --> Library Reference`,
and (for Python 3.4 at least) Section 4 Built-in Types, and then
Section 4.7.1, String Methods. (This depends on you being
attached to the Internet, or having idle configured to look at a
local copy of the official Python documentation.) Many methods use
features we have not discussed yet, but currently accessible
methods are ``capitalize``, ``title``, ``strip``, ``rfind``, ....

.. [#]
   ``s.lower()``

.. [#]
   Use a plus sign to concatenate the pieces.

.. [#]
   ``s.lower() + s.upper()``
