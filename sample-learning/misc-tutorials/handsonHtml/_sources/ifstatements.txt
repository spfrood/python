.. index:: if statement
   statement; if

.. _If-Statements:
    
If Statements
=============

.. _Simple-Conditions:

Simple Conditions
-----------------

The statements introduced in this chapter will involve tests or
*conditions*. More syntax for conditions will be introduced later,
but for now consider simple arithmetic comparisons that directly
translate from math into Python. Try each line separately in the
*Shell* ::

    2 < 5 
    3 > 7 
    x = 11 
    x > 10 
    2 * x < x 
    type(True) 

You see that conditions are either ``True`` or ``False`` (with no
quotes!). These are the only possible *Boolean* values (named after
19th century mathematician George Boole). In Python the name
Boolean is shortened to the type ``bool``. It is the type of the
results of true-false conditions or tests.

.. _Simple-if-Statements:
    
Simple ``if`` Statements
------------------------

Run this example program, suitcase.py. Try it at least twice, with
inputs: 30 and then 55. As you an see, you get an extra result,
depending on the input. The main code is:

.. literalinclude:: ../examples/suitcase.py
   :start-after: main
   :end-before: main

The middle two line are an ``if`` statement. It reads pretty much
like English. If it is true that the weight is greater than 50,
then print the statement about an extra charge. If it is not true
that the weight is greater than 50, then don't do the indented
part: skip printing the extra luggage charge. In any event, when
you have finished with the ``if`` statement (whether it actually does
anything or not), go on to the next statement that is *not*
indented under the ``if``. In this case that is the statement
printing "Thank you".

The general Python syntax for a simple ``if`` statement is

    | ``if`` *condition* ``:`` 
    |     indentedStatementBlock 

If the condition is true, then do the indented statements. If the
condition is not true, then skip the indented statements.

Another fragment as an example::

    if balance < 0: 
        transfer = -balance 
        # transfer enough from the backup account: 
        backupAccount = backupAccount - transfer
        balance = balance + transfer 


As with other kinds of statements with a heading and an indented
block, the block can have more than one statement. The assumption
in the example above is that if an account goes negative, it is
brought back to 0 by transferring money from a backup account in
several steps.

In the examples above the choice is between doing something (if the
condition is ``True``) or nothing (if the condition is ``False``).
Often there is a choice of two possibilities, only one of which
will be done, depending on the truth of a condition.


.. index:: if-else

.. _if-else-Statements:
    
|if-else| Statements
----------------------------

Run the example program, ``clothes.py``. Try it at least twice, with
inputs 50 and then 80. As you can see, you get different results,
depending on the input. The main code of ``clothes.py`` is:

.. literalinclude:: ../examples/clothes.py
   :start-after: main
   :end-before: main

The middle four lines are an if-else statement. Again it is
close to English, though you might say "otherwise" instead of
"else" (but else is shorter!). There are two indented blocks:
One, like in the simple ``if`` statement, comes right after the
``if`` heading and is executed when the condition in the ``if``
heading is true. In the |if-else| form this is followed by an
``else:`` line, followed by another indented block that is only
executed when the original condition is *false*. In an |if-else|
statement exactly one of two possible indented blocks is executed.

A line is also shown **out**\ dented next, about getting exercise.
Since it is outdented, it is not a part of the if-else statement:
It is always executed in the normal forward flow of statements,
after the |if-else| statement (whichever block is selected).

The general Python |if-else| syntax is

    | ``if`` *condition* : 
    |     indentedStatementBlockForTrueCondition 
    | ``else:``
    |    indentedStatementBlockForFalseCondition


These statement blocks can have any number of statements, and can
include about any kind of statement.

See :ref:`graduateEx`

.. index:: boolean; comparison operators
   comparison; operators
   single: <
   single: >
   single: <=
   single: >=
   single: ==
   single: !=
   
.. _More-Conditional-Expressions:
    
More Conditional Expressions
----------------------------

All the usual arithmetic comparisons may be made, but many do not
use standard mathematical symbolism, mostly for lack of proper keys
on a standard keyboard.
 
=====================  ===========  ==============
Meaning                Math Symbol  Python Symbols
=====================  ===========  ==============
Less than              <            ``<`` 
Greater than           >            ``>``
Less than or equal     ≤            ``<=``
Greater than or equal  ≥            ``>=``
Equals                 =            ``==``
Not equal              ≠            ``!=``
=====================  ===========  ============== 

There should not be space between the two-symbol Python
substitutes.

Notice that the obvious choice for *equals*, a single equal sign,
is *not* used to check for equality. An annoying second equal sign
is required. This is because the single equal sign is already used
for *assignment* in Python, so it is not available for tests.

.. warning::
   It is a common error to use only one equal sign when you mean to *test*
   for equality, and not make an assignment!

Tests for equality do not make an assignment, and they do not
require a variable on the left. Any expressions can be tested for
equality or inequality (!=). They do not need to be numbers!
Predict the results and try each line in the *Shell*::

    x = 5 
    x 
    x == 5 
    x == 6 
    x 
    x != 6 
    x = 6 
    6 == x 
    6 != x 
    'hi' == 'h' + 'i' 
    'HI' != 'hi' 
    [1, 2] != [2, 1] 

An equality check does not make an assignment. Strings are case
sensitive. Order matters in a list.

Try in the *Shell*::

    'a' > 5

When the comparison does not make sense, an Exception is caused. [#]_

Following up on the discussion of the *inexactness* of float
arithmetic in :ref:`Precision-Formats`, confirm that Python
does not consider .1 + .2 to be equal to .3: Write a simple
condition into the Shell to test.

Here is another example: Pay with Overtime. Given a person's work
hours for the week and regular hourly wage, calculate the total pay
for the week, taking into account overtime. Hours worked over 40
are overtime, paid at 1.5 times the normal rate. This is a natural
place for a function enclosing the calculation.

*Read* the setup for the function:

.. literalinclude:: ../examples/wages.py
   :lines: 3-6

The problem clearly indicates two cases: when no more than 40
hours are worked or when more than 40 hours are worked. In case
more than 40 hours are worked, it is convenient to introduce a
variable overtimeHours. You are encouraged to think about a
solution before going on and examining mine.

You can try running my complete example program, wages.py, also
shown below. The format operation at the end of the main function
uses the floating point format (:ref:`Precision-Formats`) to
show two decimal places for the cents in the answer:

.. literalinclude:: ../examples/wages.py
   :lines: 2-
   
Here the input was intended to be numeric, but it could be decimal
so the conversion from string was via ``float``, not ``int``.

Below is an equivalent alternative version of the body of
``calcWeeklyWages``, used in ``wages1.py``. It uses just one
general calculation formula and sets the parameters for the formula
in the ``if`` statement. There are generally a number of ways you might
solve the same problem!

.. literalinclude:: ../examples/wages1.py
   :lines: 7-13


.. _graduateEx:
   
Graduate Exercise
~~~~~~~~~~~~~~~~~
   
Write a program, ``graduate.py``, that prompts students for how
many credits they have. Print whether of not they have enough
credits for graduation. (At Loyola University Chicago 120 credits
are needed for graduation.)


Head or Tails Exercise
~~~~~~~~~~~~~~~~~~~~~~

Write a program ``headstails.py``. It should include a function ``flip()``,
that simulates a *single* flip of a coin: It randomly prints either 
``Heads`` or ``Tails``.
Accomplish this by choosing 0 or 1 arbitrarily with ``random.randrange(2)``,
and use an |if-else|
statement to print ``Heads``
when the result is 0, and ``Tails`` otherwise.

In your main program have a simple repeat loop that calls ``flip()``
10 times to test it, so you generate a random sequence of 10 ``Heads`` and
``Tails``.

.. _Strange-Func-Ex:

Strange Function Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~

Save the example program ``jumpFuncStub.py`` as ``jumpFunc.py``,
and complete the definitions of functions ``jump`` and ``main`` as
described in the function documentation strings in the program.
In the ``jump`` function definition use an |if-else|
statement (hint [#]_).
In the ``main`` function definition
use a |for-each| loop, the range function, and the jump function.
    
The ``jump`` function is introduced for use in
:ref:`Strange-Seq-Ex`, and others after that.

.. comment
   ]]

.. index:: if-elif
        
.. _Multiple-Tests:

Multiple Tests and |if-elif| Statements
---------------------------------------

Often you want to distinguish between more than two distinct cases,
but conditions only have two possible results, ``True`` or ``False``,
so the only direct choice is between two options. As anyone who has
played "20 Questions" knows, you can distinguish more cases by
further questions. If there are more than two choices, a single
test may only reduce the possibilities, but further tests can
reduce the possibilities further and further. Since most any kind
of statement can be placed in an indented statement block, one
choice is a further ``if`` statement. For instance consider a
function to convert a numerical grade to a letter grade, 'A', 'B',
'C', 'D' or 'F', where the cutoffs for 'A', 'B', 'C', and 'D' are
90, 80, 70, and 60 respectively. One way to write the function
would be test for one grade at a time, and resolve all the
remaining possibilities inside the next ``else`` clause::

    def letterGrade(score): 
        if score >= 90: 
            letter = 'A' 
        else:   # grade must be B, C, D or F 
            if score >= 80: 
                letter = 'B' 
            else:  # grade must be C, D or F 
                if score >= 70: 
                    letter = 'C' 
                else:    # grade must D or F 
                    if score >= 60:
                        letter = 'D' 
                    else: 
                        letter = 'F' 
        return letter 


This repeatedly increasing indentation with an ``if`` statement as
the ``else`` block can be annoying and distracting. A preferred
alternative in this situation, that avoids all this indentation, is
to combine each ``else`` and ``if`` block into an ``elif`` block:

.. literalinclude:: ../examples/grade1.py
   :lines: 3-14

The most elaborate syntax for an 
|if-elif-else| statement is indicated in general below:

    | ``if`` *condition1* ``:`` 
    |     indentedStatementBlockForTrueCondition1 
    | ``elif`` *condition2* ``:`` 
    |     indentedStatementBlockForFirstTrueCondition2 
    | ``elif`` *condition3* ``:`` 
    |     indentedStatementBlockForFirstTrueCondition3 
    | ``elif`` *condition4* ``:`` 
    |     indentedStatementBlockForFirstTrueCondition4 
    | ``else:`` 
    |    indentedStatementBlockForEachConditionFalse 


The ``if``, each ``elif``, and the final ``else`` line are all
aligned. There can be any number of ``elif`` lines, each followed
by an indented block. (Three happen to be illustrated above.) With
this construction *exactly* *one* of the indented blocks is
executed. It is the one corresponding to the *first* ``True``
condition, or, if all conditions are ``False``, it is the block
after the final ``else`` line.

Be careful of the strange Python contraction. It is ``elif``, not
``elseif``. A program testing the letterGrade function is in
example program ``grade1.py``.

See :ref:`gradeEx`.

A final alternative for ``if`` statements: |if-elif|\ -....
with *no* ``else``. This would mean changing the syntax for
|if-elif-else| above so the final ``else:`` and the block after it
would be omitted. It is similar to the basic ``if`` statement
without an ``else``, in that it is possible for *no* indented block
to be executed. This happens if *none* of the conditions in the
tests are true.

With an ``else`` included, *exactly* one of the indented blocks is
executed. Without an ``else``, at *most* one of the indented blocks
is executed. ::

    if weight > 120: 
        print('Sorry, we can not take a suitcase that heavy.') 
    elif weight > 50: 
        print('There is a $25 charge for luggage that heavy.') 

This |if-elif| statement only prints a line if there is a
problem with the weight of the suitcase.

Sign Exercise
~~~~~~~~~~~~~             
   
Write a program ``sign.py`` to ask the user for a number. Print out
which category the number is in: ``'positive'``, ``'negative'``, or
``'zero'``.


.. _gradeEx:

Grade Exercise
~~~~~~~~~~~~~~              

In Idle, load ``grade1.py`` and save it as ``grade2.py`` Modify
``grade2.py`` so it has an equivalent version of the letterGrade
function that tests in the opposite order, first for F, then D, C,
.... Hint: How many tests do you need to do? [#]_

Be sure to run your new version and test with different
inputs that test all the different paths through the program.

Wages Exercise
~~~~~~~~~~~~~~              
   
\* Modify the ``wages.py`` or the ``wages1.py`` example to create a
program ``wages2.py`` that assumes people are paid double time for
hours over 60. Hence they get paid for at most 20 hours overtime at
1.5 times the normal rate. For example, a person working 65 hours
with a regular wage of $10 per hour would work at $10 per hour for
40 hours, at 1.5 * $10 for 20 hours of overtime, and 2 * $10 for
5 hours of double time, for a total of

    10*40 + 1.5*10*20 + 2*10*5 = $800.

You may find ``wages1.py`` easier to adapt than ``wages.py``.




.. index:: nested control statements

.. _Nesting-Control-Flow-Statements:

Nesting Control-Flow Statements
-------------------------------

The power of a language like Python comes largely from the variety
of ways basic statements can be *combined*. In particular, ``for``
and ``if`` statements can be nested inside each other's indented
blocks. For example, suppose you want to print only the positive

numbers from an arbitrary list of numbers in a function with the
following heading. *Read* the pieces for now.  ::

    def printAllPositive(numberList): 
        '''Print only the positive numbers in numberList.''' 

For example, suppose ``numberList`` is ``[3, -5, 2, -1, 0, 7]``.
You want to process a list, so that suggests a |for-each| loop, ::

    for num in numberList:
   
but a |for-each| loop runs the *same* code body for each element
of the list, and we only want ::

    print(num)

for *some* of them.  That seems like
a major obstacle, but think closer at what needs to happen concretely.
As a human, who has eyes of amazing capacity, you are drawn
immediately to the actual correct numbers, 3, 2, and 7, but clearly
a computer doing this systematically will have to check *every*
number. In fact,
there is a *consistent* action required: Every number must be
tested to see *if* it should be printed. This suggests an ``if``
statement, with the condition ``num > 0``. Try loading into Idle
and running the example program ``onlyPositive.py``, whose code is
shown below. It ends with a line testing the function:

.. literalinclude:: ../examples/onlyPositive.py
   :lines: 3-

This idea of nesting ``if`` statements enormously expands the
possibilities with loops. Now different things can be done at
different times in loops, as long as there is a *consistent test*
to allow a choice between the alternatives.  Shortly, ``while`` loops
will also be introduced, and you will see ``if`` statements nested inside
of them, too.

-----------
   
The rest of this section deals with graphical examples.

Run example program ``bounce1.py``. It has a red ball moving and
bouncing obliquely off the edges. If you watch several times, you
should see that it starts from random locations. Also you can
repeat the program from the Shell prompt after you have run the
script. For instance, right after running the program, try in the
*Shell* ::

    bounceBall(-3, 1)

The parameters give the amount the shape moves in each animation
step. You can try other values in the *Shell*, preferably with
magnitudes less than 10.

For the remainder of the description of this example, *read* the
extracted text pieces.

The animations before this were totally scripted, saying exactly
how many moves in which direction, but in this case the direction
of motion changes with every bounce. The program has a graphic
object ``shape`` and the central animation step is ::

    shape.move(dx, dy)

but in this case, dx and dy have to change when the ball gets to a
boundary. For instance, imagine the ball getting to the left side
as it is moving to the left and up. The bounce obviously alters the
horizontal part of the motion, in fact reversing it, but the ball
would still continue up. The reversal of the horizontal part of the
motion means that the horizontal shift changes direction and
therefore its sign::

    dx = -dx

but ``dy`` does not need to change. This switch does not happen at
each animation step, but only when the ball reaches the edge of the
window. It happens only some of the time - suggesting an ``if``
statement. Still the condition must be determined. Suppose the
center of the ball has coordinates (x, y). When x reaches some
particular x coordinate, call it xLow, the ball should bounce.

.. figure:: images/BallBounce.*
   :align: center
   :alt: image
   :width: 46.5 pt

The edge of the window is at coordinate 0, but ``xLow`` should not
be 0, or the ball would be half way off the screen before bouncing!
For the edge of the ball to hit the edge of the screen, the x
coordinate of the center must be the length of the radius away, so
actually ``xLow`` is the radius of the ball.

Animation goes quickly in small steps, so I cheat. I allow the ball
to take one (small, quick) step past where it really should go
(``xLow``), and then we reverse it so it comes back to where it
belongs. In particular ::

    if x < xLow: 
        dx = -dx 

There are similar bounding variables ``xHigh``, ``yLow`` and
``yHigh``, all the radius away from the actual edge coordinates,
and similar conditions to test for a bounce off each possible edge.
Note that whichever edge is hit, one coordinate, either dx or dy,
reverses. One way the collection of tests could be written is ::

    if x < xLow: 
        dx = -dx 
    if x > xHigh: 
        dx = -dx 
    if y < yLow: 
        dy = -dy 
    if y > yHigh: 
        dy = -dy 

This approach would cause there to be some extra testing: If it is
true that ``x < xLow``, then it is impossible for it to be true
that ``x > xHigh``, so we do not need both tests together. We avoid
unnecessary tests with an elif clause (for both x and y):

.. literalinclude:: ../examples/bounce1.py
   :start-after: getY
   :end-before: sleep

Note that the middle ``if`` is *not* changed to an ``elif``,
because it is possible for the ball to reach a *corner*, and need
both ``dx`` and ``dy`` reversed.

The program also uses several accessor methods for graphics objects
that we have not used in examples yet. Various graphics objects,
like the circle we are using as the shape, know their center point,
and it can be accessed with the ``getCenter()`` method. (Actually a
clone of the point is returned.) Also each coordinate of a
``Point`` can be accessed with the ``getX()`` and ``getY()``
methods.

This explains the new features in the central function defined for
bouncing around in a box, ``bounceInBox``. The animation
arbitrarily goes on in a simple repeat loop for 600 steps. (A later
example will improve this behavior.)

.. literalinclude:: ../examples/bounce1.py
   :start-after: random
   :end-before: getRandom

The program starts the ball from an arbitrary point inside the
allowable rectangular bounds. This is encapsulated in a utility
function included in the program, ``getRandomPoint``. The
getRandomPoint function uses the ``randrange`` function from the
module ``random``. Note that in parameters for both the functions
``range`` and ``randrange``, the end stated is *past* the last
value actually desired:

.. literalinclude:: ../examples/bounce1.py
   :start-after: sleep
   :end-before: def makeDisk

The full program is listed below, repeating ``bounceInBox`` and
``getRandomPoint`` for completeness. Several parts that may be
useful later, or are easiest to follow as a unit, are separated out
as functions. Make sure you see how it all hangs together or ask
questions!

.. literalinclude:: ../examples/bounce1.py

Short String Exercise
~~~~~~~~~~~~~~~~~~~~~

Write a program ``short.py`` with a function ``printShort`` with heading::

    def printShort(strings):
        '''Given a list of strings,
        print the ones with at most three characters.
        >>> printShort(['a', 'long', one'])
        a
        one
        '''

In your main program, test the function, calling it several times
with different lists of strings.  Hint:  Find the length of each string
with the ``len`` function.

.. index:: shell; sequence in doc string

The function documentation here models a common
approach:  illustrating the behavior of the function with a Python Shell
interaction.  This begins with a line starting with ``>>>``.
Other exercises and examples will also document behavior in the Shell.

Even Print Exercise
~~~~~~~~~~~~~~~~~~~

Write a program ``even1.py`` with a function ``printEven`` with heading::

    def printEven(nums):
        '''Given a list of integers nums,
        print the even ones.
        
        >>> printEven([4, 1, 3, 2, 7])
        4
        2
        '''

In your main program, test the function, calling it several times
with different lists of integers.  Hint:  A number is even if its
remainder, when dividing by 2, is 0.
    
Even List Exercise
~~~~~~~~~~~~~~~~~~~

Write a program ``even2.py`` with a function ``chooseEven`` with heading::

    def chooseEven(nums):
        '''Given a list of integers, nums,
        return a list containing only the even ones.

        >>> chooseEven([4, 1, 3, 2, 7])
        [4, 2]
        '''

In your main program, test the function, calling it several times
with different lists of integers and printing the results.  Hint:
Create a new list, and append the appropriate numbers to it.

.. _unique-list-ex:

Unique List Exercise
~~~~~~~~~~~~~~~~~~~~~~~

\* The ``madlib2.py`` program has its ``getKeys`` function, which first generates
a list of each occurrence of a cue in the story format.  This gives the 
cues in order, but likely includes repetitions.  The original version of ``getKeys``
uses a quick method to remove duplicates, forming a **set** from the list.
There is a disadvantage in the conversion, though:  Sets are not ordered, so
when you iterate through the resulting set, the order of the cues will likely bear no
resemblance to the order they first appeared in the list.  That issue
motivates this problem:

Copy ``madlib2.py`` to ``madlib2a.py``, and add a function with this heading::

    def uniqueList(aList):
        ''' Return a new list that includes the first occurrence of each value
        in aList, and omits later repeats.  The returned list should include 
        the first occurrences of values in aList in their original order.
        
        >>> vals = ['cat', 'dog', 'cat', 'bug', 'dog', 'ant', 'dog', 'bug'] 
        >>> uniqueList(vals)
        ['cat', 'dog', 'bug', 'ant']
        '''

.. index::
   in boolean operator on sequence
   not in
   boolean; operations in + not in
        
A useful Boolean operator is ``in``, checking membership in a sequence::

   >>> vals = ['this', 'is', 'it]
   >>> 'is' in vals
   True
   >>> 'was' in vals
   False         

It can also be used with ``not``, as ``not in``, to mean the opposite::

   >>> vals = ['this', 'is', 'it]
   >>> 'is' not in vals
   False
   >>> 'was' not in vals
   True         

In general the two versions are:

    | *item* ``in`` *sequence*
    | *item* ``not in`` *sequence*
    
Hint: Process ``aList`` in order.  Use the new syntax to
only append elements to a new list that are not 
already in the new list.    

After perfecting the ``uniqueList`` function, replace the last line of ``getKeys``,
so it uses  ``uniqueList`` to remove duplicates in ``keyList``. 

Check that your ``madlib2a.py`` prompts you for cue values in the order that 
the cues first appear in the madlib format string.

    
.. index::
   and
   boolean operation; and

.. _Compound-Boolean-Expressions:
   
Compound Boolean Expressions
----------------------------

To be eligible to graduate from Loyola University Chicago, you must
have 120 credits *and* a GPA of at least 2.0. This
translates directly into Python as a *compound condition*::

    credits >= 120 and GPA >=2.0      

This is true if both ``credits >= 120`` is true and
``GPA >= 2.0`` is
true. A short example program using this would be::

    credits = float(input('How many units of credit do you have? ')) 
    GPA = float(input('What is your GPA? ')) 
    if credits >= 120 and GPA >=2.0: 
        print('You are eligible to graduate!') 
    else: 
        print('You are not eligible to graduate.') 


The new Python syntax is for the operator ``and``:

    *condition1* ``and`` *condition2*

The compound condition is true if both of the component conditions
are true. It is false if at least one of the conditions is false.

See :ref:`congressEx`.

.. index:: or
   boolean operation; or
   

In the last example in the previous section, there was an |if-elif|
statement where both tests had the same block to be done if the
condition was true::

    if x < xLow: 
        dx = -dx 
    elif x > xHigh: 
        dx = -dx 


There is a simpler way to state this in a sentence: If x < xLow or
x > xHigh, switch the sign of dx. That translates directly into
Python::

    if x < xLow or x > xHigh: 
        dx = -dx 

The word ``or`` makes another compound condition:

    *condition1* ``or`` *condition2*

is true if *at least* one of the conditions is true. It is false if
both conditions are false. This corresponds to *one* way the word
"or" is used in English. Other times in English "or" is used to
mean *exactly one* alternative is true.

.. warning::
   When translating a problem stated in English using "or", be careful
   to determine whether the meaning matches Python's ``or``.

-------
   
It is often convenient to encapsulate complicated tests inside a
function. Think how to complete the function starting::

    def isInside(rect, point): 
        '''Return True if the point is inside the Rectangle rect.'''         
        pt1 = rect.getP1() 
        pt2 = rect.getP2() 

Recall that a ``Rectangle`` is specified in its constructor by two
diagonally oppose ``Point``\ s. This example gives the first use in
the tutorials of the ``Rectangle`` methods that recover those two
corner points, ``getP1`` and ``getP2``. The program calls the
points obtained this way ``pt1`` and ``pt2``. The x and y coordinates
of ``pt1``, ``pt2``, and ``point`` can be recovered with the
methods of the ``Point`` type, ``getX()`` and ``getY()``.

.. index:: chaining comparisons
   comparison; chaining 


Suppose that I introduce variables for the x coordinates of ``pt1``,
``point``, and ``pt2``, calling these x-coordinates ``end1``,
``val``, and ``end2``, respectively. On first try you might decide
that the needed mathematical relationship to test is ::

    end1 <= val <= end2

Unfortunately, this is not enough: The only requirement for the two
corner points is that they be diagonally opposite, not that the
coordinates of the second point are higher than the corresponding
coordinates of the first point. It could be that ``end1`` is 200;
``end2`` is 100, and ``val`` is 120. In this latter case ``val``
*is* between ``end1`` and ``end2``, but substituting into the
expression above ::

    200 <= 120 <= 100

is False. The 100 and 200 need to be reversed in this case. This
makes a complicated situation.  Also this is an issue which must be revisited
for both the x and y coordinates. I introduce an auxiliary function
``isBetween`` to deal with one coordinate at a time. It starts::

    def isBetween(val, end1, end2): 
        '''Return True if val is between the ends. 
        The ends do not need to be in increasing order.'''     

Clearly this is true if the original expression,
``end1 <= val <= end2``, is true. You must also consider the possible
case when the order of the ends is reversed:
``end2 <= val <= end1``. How do we combine these two possibilities?
The Boolean connectives to consider are ``and`` and ``or``.
Which applies? You only need one to be true, so ``or`` is the
proper connective:

A correct but redundant function body would be::

    if end1 <= val <= end2 or end2 <= val <= end1: 
        return True 
    else: 
        return False 

Check the meaning: if the compound expression is ``True``, return ``True``.
If the condition is ``False``, return ``False`` - in either case return the
*same* value as the test condition. See that a much simpler and
neater version is to just return the value of the condition
itself!  ::

    return end1 <= val <= end2 or end2 <= val <= end1

.. note::
   In general you should *not* need an |if-else| statement to
   choose between true and false values!  Operate directly on
   the boolean expression.

A side comment on expressions like ::

    end1 <= val <= end2

Other than the two-character operators, this is like standard math
syntax, *chaining* comparisons. In Python any number of comparisons
can be *chained* in this way, closely approximating mathematical
notation. Though this is good Python, be aware that if you try
other high-level languages like Java and C++, such an expression is
gibberish. Another way the expression can be expressed (and which
translates directly to other languages) is::

    end1 <= val and val <= end2

So much for the auxiliary function ``isBetween``. Back to the
``isInside`` function. You can use the ``isBetween`` function to check
the x coordinates, ::

   isBetween(point.getX(), p1.getX(), p2.getX())

and to check the y coordinates, ::

    isBetween(point.getY(), p1.getY(), p2.getY())

Again the question arises: how do you combine the two tests?

In this case we need the point to be both between the sides *and*
between the top and bottom, so the proper connector is *and*.

Think how to finish the ``isInside`` method. Hint: [#]_

.. index::
   not
   boolean operation; not

Sometimes you want to test the opposite of a condition. As in
English you can use the word ``not``. For instance, to test if a
Point was not inside Rectangle Rect, you could use the condition ::

    not isInside(rect, point)


In general,

    ``not`` *condition*

is ``True`` when *condition* is ``False``, and ``False`` when
*condition* is ``True``.

The example program ``chooseButton1.py``, shown below, is a complete
program using the ``isInside`` function in a simple application,
choosing colors. Pardon the length. Do check it out. It will be the
starting point for a number of improvements that shorten it and
make it more powerful in the next section. First a brief overview:

The program includes the functions ``isBetween`` and ``isInside`` that have
already been discussed. The program creates a number of colored
rectangles to use as buttons and also as picture components. Aside
from specific data values, the code to create each rectangle is the
same, so the action is encapsulated in a function,
``makeColoredRect``. All of this is fine, and will be preserved in
later versions.

The present main function is long, though. It has the usual
graphics starting code, draws buttons and picture elements, and
then has a number of code sections prompting the user to choose a
color for a picture element. Each code section has a long
|if-elif-else| test to see which button was clicked, and sets the
color of the picture element appropriately.

.. literalinclude:: ../examples/chooseButton1.py

.. index::
   line continuation \
   single: \; line continuation

The only further new feature used is in the long return statement
in ``isInside``. ::

    return isBetween(point.getX(), pt1.getX(), pt2.getX()) and \ 
           isBetween(point.getY(), pt1.getY(), pt2.getY()) 

Recall that Python is smart enough to realize that a statement
continues to the next line if there is an unmatched pair of
parentheses or brackets. Above is another situation with a long
statement, but there are no unmatched parentheses on a line. For
readability it is best *not* to make an enormous long line that
would run off your screen or paper. Continuing to the next line is
recommended. You can make the *final* character on a line be a
backslash (\\) to indicate the statement continues on the next
line. This is not particularly neat, but it is a rather rare
situation. Most statements fit neatly on one line, and the creator
of Python decided it was best to make the syntax simple in the most
common situation. (Many other languages require a special statement
terminator symbol like ';' and pay no attention to newlines).
Extra parentheses here would not hurt, so an alternative would be ::

    return (isBetween(point.getX(), pt1.getX(), pt2.getX()) and 
            isBetween(point.getY(), pt1.getY(), pt2.getY()) ) 

The chooseButton1.py program is long partly because of repeated
code. The next section gives another version involving lists.

.. _congressEx:

Congress Exercise
~~~~~~~~~~~~~~~~~
   
A person is eligible to be a US Senator who is at least 30 years
old and has been a US citizen for at least 9 years. Write an initial version
of a program ``congress.py`` to obtain age and length of
citizenship from the user and print out if a person is eligible to
be a Senator or not. 

A person is eligible to be a US Representative
who is at least 25 years old and has been a US citizen for at least
7 years. Elaborate your program ``congress.py`` so it obtains age
and length of citizenship and prints out just the *one* of the following
three statements that is accurate:

#. You are eligible for both the House and Senate.
#. You eligible only for the House.
#. You are ineligible for Congress.



.. index::
   string; startswith + endswith + replace 
   startswith string method
   endswith string method
   replace string method
   
.. _More-String-Methods:
   
More String Methods
-----------------------

Here are a few more string methods useful in the next exercises:

* *s*\ ``.startswith(`` *pre* ``)``

  returns ``True`` if string *s* starts with string *pre*:
  Both ``'-123'.startswith('-')`` and ``'downstairs'.startswith('down')``
  are ``True``, but ``'1 - 2 - 3'.startswith('-')`` is ``False``.

* *s*\ ``.endswith(`` *suffix* ``)``

  returns True if string *s* ends with string *suffix*:
  Both ``'whoever'.endswith('ever')`` and ``'downstairs'.endswith('airs')``
  are ``True``, but ``'1 - 2 - 3'.endswith('-')`` is ``False``.

* *s*\ ``.replace(`` *sub* ``,`` *replacement* ``,`` *count* ``)``

  returns a new string with up to the first *count* occurrences of string
  *sub* replaced by *replacement*.  The *replacement* can be the empty 
  string to delete *sub*.  For example::

	  s = '-123'
	  t = s.replace('-', '', 1) # t equals '123'
	  t = t.replace('-', '', 1) # t is still equal to '123'
	  u = '.2.3.4.'
	  v = u.replace('.', '', 2) # v equals '23.4.'

.. _Article-Start-Ex:

Article Start Exercise
~~~~~~~~~~~~~~~~~~~~~~

In library alphabetizing, if the initial word is an *article* ("The", "A", "An"),
then it is ignored when ordering entries.  Write a program completing this
function, and then testing it::

    def startsWithArticle(title):
        '''Return True if the first word of title is "The", "A" or "An".'''
        
Be careful, if the title starts with "There", it does not start with an article.
What should you be testing for?


.. _Is-Number-String-Ex:

Is Number String Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~

\*\* In the later :ref:`Safe-Num-Input-Ex`, it will be important to know if
a string can be converted to the desired type of number.  Explore that here.
Save example ``isNumberStringStub.py`` as ``isNumberString.py`` and complete
it.  It contains headings and documentation strings
for the functions in both parts of this exercise.

A legal whole number string consists entirely of digits.
Luckily strings have an
``isdigit`` method, which is true when a nonempty string consists
entirely of digits, so
``'2397'.isdigit()`` returns ``True``, and ``'23a'.isdigit()``
returns ``False``, exactly corresponding to the situations when the string
represents a whole number!

In both parts be sure to test carefully.  Not only confirm that all
appropriate strings return ``True``.
Also be sure to test that you return ``False`` for *all* sorts of bad strings.

a.  Recognizing an integer string is more involved,
    since it can start with a minus sign (or not).
    Hence the ``isdigit`` method is not enough by itself.
    This part is the most straightforward if you have worked on
    the sections :ref:`string-indices` and :ref:`string-slices`.
    An alternate approach works if you use 
    the count method from :ref:`object-orientation`, and some 
    methods from this section.
    
    Complete the function ``isIntStr``.      

b.  Complete the function ``isDecimalStr``, which introduces the possibility
    of a decimal point.  The string methods mentioned
    in the previous part remain useful.


.. [#]
   This is an improvement that is new in Python 3.0

.. [#]
   If you divide an even number by 2, what is the remainder?  Use this idea
   in your ``if`` condition.
   
.. [#]
   4 tests to distinguish the 5 cases, as in the previous version

.. [#]
   Once again, you are calculating and returning a Boolean result. You
   do not need an |if-else| statement.

