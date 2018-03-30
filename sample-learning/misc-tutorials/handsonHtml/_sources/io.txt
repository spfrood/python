
Input and Output
================

.. index::
   input function with prompt
   function; input with prompt
   prompt in input function

.. _The-input-Function:

The ``input`` Function
----------------------

The hello program of :ref:`The-Classic-First` always does the
same thing. This is not very interesting. Programs are only going
to be reused if they can act on a variety of data. One way to get
data is directly from the user. Modify the hello.py program as
follows in the editor, and save it with
:menuselection:`File --> Save As....``, using the name
``hello_you.py``.  ::

    person = input('Enter your name: ') 
    print('Hello', person)  

Run the program. In the Shell you should see ::

    Enter your name:

.. index:: shell; program input

Follow the instruction (and press Enter). Make sure the typing
cursor is in the Shell window, at the end of this line. After you
type your response, you can see that the program has taken in the
line you typed. That is what the built-in function ``input`` does:
First it prints the string you give as a parameter (in this case
``'Enter your name: '``), and then it waits for a line to be typed
in, and returns the string of characters you typed. In the
``hello_you.py`` program this value is assigned to the variable
person, for use later.

The parameter inside the parentheses after ``input`` is important.
It is a *prompt*, prompting you that keyboard input is expected at
that point, and hopefully indicating what is being requested.
Without the prompt, the user would not know what was happening, and
the computer would just sit there waiting!

Open the example program, ``interview.py``. Before running it (with
any made-up data), see if you can figure out what it will do:

.. index::
   example program; interview
   interview example program

.. literalinclude:: ../examples/interview.py

The statements are executed in the order they appear in the text of
the program: *sequentially*. This is the simplest way for the
execution of the program to flow. You will see instructions later
that alter that natural flow.

If we want to reload and modify the ``hello_you.py`` program to put
an exclamation point at the end, you could try::

    person = input('Enter your name: ') 
    print('Hello', person, '!') 

Run it and you see that it is not spaced right. There should be no
space after the person's name, but the default behavior of the
print function is to have each field printed separated by a space.
There are several ways to fix this. You should know one. Think
about it before going on to the next section. Hint: [#]_

.. [#]
   The + operation on strings adds no extra space.

.. match ]]

.. index:: sep
   print; sep keyword parameter
   keyword parameter; sep

Print with Keyword Parameter ``sep``
------------------------------------

One way to put punctuation but no space after the person in
``hello_you.py`` is to use the plus operator, +. Another approach is
to change the default *separator* between fields in the print
function. This will introduce a new syntax feature,
*keyword parameters*. The print function has a keyword parameter
named ``sep``. If you leave it out of a call to print, as we have so
far, it is set equal to a space by default. If you add a final
field, ``sep=''``, in the print function in ``hello_you.py``, you get the
following example file, hello_you2.py:

.. literalinclude:: ../examples/hello_you2.py
   :language: python3

Try the program.

Keyword paramaters must be listed at the end of the parameter
list.

.. index::
   int; digit string
   string; digits

.. _Numbers-and-Digit-Strings:

Numbers and Strings of Digits
-----------------------------

Consider the following problem: Prompt the user for two numbers,
and then print out a sentence stating the sum. For instance if the
user entered 2 and 3, you would print 'The sum of 2 and 3 is 5.'

You might imagine a solution like the example file
``addition1.py``, shown below. There is a problem. Can you figure
it out before you try it? Hint: [#]_  

.. literalinclude:: ../examples/addition1.py
   :language: python3
                        
End up running it in any case.

We do not want string concatenation, but integer addition. We need
integer operands. Briefly mentioned in
:ref:`Whirlwind-Introduction-To` was the fact that we can use
type names as functions to convert types. One approach would be to
do that. Further variable names are also introduced in the example
``addition2.py`` file below to emphasize the distinctions in types.
Read and run:

.. literalinclude:: ../examples/addition2.py
   :language: python3

Needing to convert string input to numbers is a common situation,
both with keyboard input and later in web pages. While the extra
variables above emphasized the steps, it is more concise to write
as in the variation in example file, ``addition3.py``, doing the
conversions to type ``int`` immediately:

.. literalinclude:: ../examples/addition3.py
   :language: python3

The simple programs so far have followed a basic
*programming pattern*: input-calculate-output. Get all the data
first, calculate with it second, and output the results last. The
pattern sequence would be even clearer if we explicitly create a
named result variable in the middle, as in ``addition4.py``

.. literalinclude:: ../examples/addition4.py
   :language: python3

We will see more complicated patterns, which involve repetition, in
the future.

.. [#]
   The input function produces values of string type.

.. match ]]

.. _AdditionProblem:

Exercise for Addition
~~~~~~~~~~~~~~~~~~~~~~

Write a version, :file:`add3.py`, that
asks for three numbers, and lists all three, and their sum, in
similar format to :file:`addition4.py` displayed above.

.. _QuotientProblem:

Exercise for Quotients
~~~~~~~~~~~~~~~~~~~~~~~

Write a program, ``quotient.py``, that
prompts the user for two integers, and then prints them out in a
sentence with an integer division problem like ::

   The quotient of 14 and 3 is 4 with a remainder of 2

Review :ref:`Division-and-Remainders` if you forget the integer
division or remainder operator.

.. index:: 
   format; string and method
   object; string
   method; string format

.. _Format-Strings:

String Format Operation
-----------------------

In grade school quizzes a common convention is to use fill-in-the blanks. For instance,

    Hello _____!


and you can fill in the name of the person greeted, and combine
given text with a chosen insertion. *We use this as an analogy:*  
Python has a similar
construction, better called fill-in-the-braces. There is a
particular operation on strings called ``format``, that makes
substitutions into places enclosed in braces. For instance the
example file, hello_you3.py, creates and prints the same
string as in hello_you2.py from the previous section:

.. literalinclude:: ../examples/hello_you3.py

There are several new ideas here!

First *method* calling syntax for *objects* is used. You will see this 
very important modern syntax in more
detail at the beginning of the next chapter in :ref:`Object-Orientation`. 
All data in Python are objects, including strings. 
Objects have a special syntax for functions, called *methods*,
associated with the *particular type of object*. In particular
``str`` objects have a method called ``format``. The syntax for
methods has the object followed by a period followed by the method
name, and further parameters in parentheses.

    *object*.\ *methodname*\ ``(``\ *parameters*\ ``)``

In the example above, the object is the string ``'Hello {}!'``.
The method is named ``format``. There is one further parameter,
``person``.

The string for the ``format`` method has a special form, with braces embedded.
Places where
braces are embedded are replaced by the value of an expression
taken from the parameter list for the ``format`` method. There are many
variations on the syntax between the braces. In this case we use
the syntax where the first (and only) location in the string with
braces has a substitution made from the first (and only) parameter.

.. index:: 
   braces; format string
   single: {}; format string
   format string

In the code above, this new string is assigned to the identifier
``greeting``, and then the string is printed. 

The identifier
``greeting`` was introduced to break the operations into a clearer
sequence of steps. However, since the value of ``greeting`` is only
referenced once, it can be eliminated with the more concise
version::

    person = input('Enter your name: ') 
    print('Hello {}!'.format(person)) 

Consider the interview program. Suppose we want to add a period at
the end of the sentence (with no space before it). One approach
would be to combine everything with plus signs. Another way is
printing with keyword ``sep=''``. Another approach is with string
formatting. Using our grade school analogy, the idea is to fill in the blanks in

    _____ will interview _____ at _____. 


There are multiple places to substitute, and the format approach
can be extended to multiple substitutions: Each place in the format
string where there is ``'{}'``, the ``format`` operation will
substitute the value of the next parameter in the format parameter
list.

Run the example file ``interview2.py``, and check that the results
from all three methods match.  

.. literalinclude:: ../examples/interview2.py
   :language: python3

Sometimes you want a single string,
but not just for printing.  You can combine pieces with the ``+`` operator,
but then all pieces must be strings or *explicitly converted to strings*.
An advantage of the format method is that it will convert types to string
automatically, like the print function. Here is another variant of our
addition sentence example, :file:`addition4a.py`, using the format method.

.. literalinclude:: ../examples/addition4a.py
   :language: python3

Conversion to strings was not needed in interview2.py.
(Everything started out as a string.)
In :file:`addition4a.py`, however,
the automatic conversion of the integers to strings is useful.


So far there is no
situation that requires a format string instead of using other approaches.
Sometimes a format string provides a shorter and simpler expression.  
Except where specifically instructed in an exercise for practice, use whatever
approach to combining strings and data that you like.
There are many elaborations to the fields in braces to control formatting.  
We will look at one later, :ref:`Precision-Formats`, where format strings
are particularly useful.  

A technical point: Since braces have special meaning in a format
string, there must be a special rule if you want braces to actually
be included in the final *formatted* string. The rule is to double
the braces: ``'{{'`` and ``'}}'``. The example code
``formatBraces.py``, shown below, makes ``setStr`` refer to the
string ``'The set is {5,9}.'``. The initial and final doubled
braces in the format string generate literal braces in the
formatted string:

.. literalinclude:: ../examples/formatBraces.py
   :language: python3

This kind of format string depends directly on the order of the
parameters to the format method. There is another approach with a
dictionary, that was used in the first sample program, ``madlib.py``, and will be
discussed more in :ref:`Dictionaries-and-String`.
The dictionary approach is probably the best in many
cases, but the count-based approach is an easier start,
particularly if the parameters are just used once, in order.

Optional elaboration with explicitly numbered entries
    Imagine the format parameters numbered in
    order, starting from 0. In this case 0, 1, and 2. The number of the
    parameter position may be included inside the braces, so an
    alternative to the last line of interview2.py is (added in
    example file :file:`interview3.py`)::

        print('{0} will interview {1} at {2}.'.format(interviewer, applicant, time)) 

    This is more verbose than the previous version, with no obvious
    advantage. However, if you desire to use some of the parameters more than
    once, then the approach with the numerical identification with the
    parameters is useful. Every place the string includes ``'{0}'``,
    the ``format`` operation will substitute the value of the initial
    parameter in the list. Wherever ``'{1}'`` appears, the next format
    parameter will be substituted....

    Predict the results of the example file :file:`arith.py` shown
    below, if you enter 5 and 6.  Then check yourself by running it. In this case the
    numbers referring to the parameter positions are necessary. They
    are both repeated and used out of order:

    .. literalinclude:: ../examples/arith.py

    Try the program with other data.

Now that you have a few building blocks, you will see more exercises where you need to
start to do creative things.  You are encouraged to go back and reread 
:ref:`learning-to-problem-solve`.

Addition Format Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~

Write a version of :ref:`AdditionProblem`,
:file:`add3f.py`, that uses the string format method to construct the
same final string as before.

.. _QuotientFormatProblem:

Quotient Format Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~

Write a version of the quotient problem in :ref:`QuotientProblem`,
:file:`quotientformat.py`, that uses the string format method to
construct the same final string as before.  Again be sure to give a full sentence
stating both the integer quotient and the remainder.

