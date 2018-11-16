
.. index::
   double:  while; statement

.. _While-Statements:
   
While Statements
================

.. _Simple-while-Loops:
   
Simple ``while`` Loops
----------------------

Other than the trick with using a ``return`` statement inside of a
``for`` loop, all of the loops so far have gone all the way through
a *specified* list. In any case the ``for`` loop has required the
use of a specific list. This is often too restrictive. A Python
``while`` loop behaves quite similarly to common English usage. If
I say

    While your tea is too hot, add a chip of ice.

Presumably you would test your tea. If it were too hot, you would
add a little ice. If you test again and it is still too hot, you
would add ice again. *As long as* you tested and found it was true
that your tea was too hot, you would go back and add more ice.
Python has a similar syntax:

    ``while`` *condition* ``:`` 
        indentedBlock 

Setting up the English example in a similar format would be:

    while *your tea is too hot* : 
        add a chip of ice 

To make things concrete and numerical, suppose the following: The
tea starts at 115 degrees Fahrenheit. You want it at 112 degrees. A
chip of ice turns out to lower the temperature one degree each
time. You test the temperature each time, and also print out the
temperature before reducing the temperature. In Python you could
write and run the code below, saved in example program cool.py:

.. literalinclude:: ../examples/cool.py
   :linenos:

I added a final line after the while loop to remind you that
execution follows sequentially after a loop completes.

If you play computer and follow the path of execution, you could
generate the following table. Remember, that each time you reach
the end of the indented block after the ``while`` heading,
execution returns to the ``while`` heading for another test:

====  ===========  =======
Line  temperature  Comment
====  ===========  =======
1     115
2                  115 > 112 is true, do loop
3                  prints 115
4     114          115 - 1 is 114, loop back
2                  114 > 112 is true, do loop
3                  prints 114
4     113          114 - 1 is 113, loop back
2                  113 > 112 is true, do loop
3                  prints 113
4     112          113 - 1 is 112, loop back
2                  112 > 112 is false, skip loop
6                  prints that the tea is cool
====  ===========  =======

Each time the end of the indented loop body is reached, execution
returns to the ``while`` loop heading for another test. When the
test is finally false, execution jumps past the indented body of
the ``while`` loop to the next sequential statement.

A ``while`` loop generally follows the pattern of the successive
modification loop introduced with |for-each| loops:

    | initialization
    | ``while`` *continuationCondition* ``:`` 
    |     do main action to be repeated 
    |     prepare variables for the next time through the loop

Test yourself: Following the code.  Figure out what is printed. :

.. literalinclude:: ../examples/testWhile.py
   :lines: 3-

Check yourself by running the example program ``testWhile.py``.

.. note::
   In Python, ``while`` is not used *quite* like in English. In
   English you could mean to stop *as soon as* the condition you want
   to test becomes false. In Python the test is *only* made when
   execution for the loop starts, *not* in the middle of the loop.

*Predict* what will happen with this slight variation on the
previous example, switching the order in the loop body. Follow it
carefully, one step at a time.

.. literalinclude:: ../examples/testWhile2.py
   :linenos:

Check yourself by running the example program ``testWhile2.py``.

The sequence order is important. The variable ``i`` is increased before
it is printed, so the first number printed is 6. Another common
error is to assume that 10 will *not* be printed, since 10 is
*past* 9, but the test that may stop the loop is *not* made in the
middle of the loop. Once the body of the loop is started, it
continues to the end, even when ``i`` becomes 10.
 
====  ==  ======= 
Line   i  Comment
====  ==  ======= 
1      4
2         4 < 9 is true, do loop
3      6  4+2=6
4         print 6
2         6 < 9 is true, do loop
3      8  6+2= 8
4         print 8
2         8 < 9 is true, do loop
3     10  8+2=10  *No test here*
4         print 10 
2         10 < 9 is false, skip loop
====  ==  ======= 

Predict what happens in this related little program:

.. literalinclude:: ../examples/testWhile3.py
   :lines: 3-

Check yourself by running the example program ``testWhile3.py``.


.. index::
   single:  range; three parameter

.. _The-general-range-function:
    
The Most General ``range`` Function
-----------------------------------

There is actually a much simpler way to generate the previous
sequences like in ``testWhile3.py``,
using a further variation of the ``range`` function.
Enter these lines separately in the *Shell*. As in the simpler
applications of ``range``, the values are only generated one at a
time, as needed. To see the entire sequence at once, convert the
sequence to a list before printing::

    nums = range(4, 9, 2)
    print(list(nums))

The third parameter for the range function is the step size.
It is needed when the step size from one element
to the next is not 1.

The most general syntax is

    ``range(`` *start* ``,`` *pastEnd* ``,`` *step* ``)``

The value of the second parameter is always *past* the final
element of the list. Each element after the first in the list is
*step* more than the previous one. Predict and try in the *Shell*::

    list(range(4, 10, 2))

Actually the range function is even more sophisticated than
indicated by the ``while`` loop above. The step size can be negative.
Try in the *Shell*::

    list(range(10, 0, -1))

Do you see how 0 is *past* the end of the list?

**Try it:**  Make up a ``range`` function call to generate the list of
temperatures printed in the tea example, ``115, 114, 113``. Test it
in the *Shell*.

These ranges, like the simpler ranges that we used earlier,
are most often used as the sequence in a ``for`` loop heading::

    for i in range(10, 0, -1):  # countdown...
        print(i)
    print('Blastoff!')

.. index::
   interactive while loop
   while; interactive
   loop; interactive

.. _Interactive-while-Loops:
    
Interactive ``while`` Loops
---------------------------

The earlier examples of while loops were chosen for their
simplicity. Obviously they could have been rewritten with range
function calls. Now lets try a more interesting example. Suppose
you want to let a user enter a sequence of lines of text, and want
to remember each line in a list. This could easily be done with a
simple repeat loop if you knew the number of lines to enter. For
example, in ``readLines0.py``, the user is prompted for the exact
number of lines to be entered:

.. literalinclude:: ../examples/readLines0.py
   :lines: 3-

The user may want to enter a bunch of lines and not count them all
ahead of time. This means the number of repetitions would not be
known ahead of time. A ``while`` loop is appropriate here. There is
still the question of how to test whether the user wants to
continue. An obvious but verbose way to do this is to ask before
every line if the user wants to continue, as shown below and in the
example file ``readLines1.py``. Read it and then run it:

.. literalinclude:: ../examples/readLines1.py
   :lines: 3-

See the *two* statements setting ``testAnswer``:  
one before the ``while`` loop and one at the bottom of the loop body.

.. note::
   The data must be initialized *before* the loop, in order for the
   first test of the while condition to work. Also the test must work
   when you loop back from the end of the loop body. This means the
   data for the test must also be set up a second time, *in* the loop
   body.  It is easy to forget the second time!

The ``readLines1.py`` code works, but it may be more annoying than
counting ahead! Two lines must be entered for every one you
actually want! A practical alternative is to use a *sentinel*: a
piece of data that would *not* make sense in the regular sequence,
and which is used to indicate the *end* of the input. You could
agree to use the line ``DONE!`` Even simpler: if you assume all the
real lines of data will actually have some text on them, use an
*empty* line as a sentinel. (If you think about it, the Python
Shell uses this approach when you enter a statement with an
indented body.) This way you only need to enter one extra (very
simple) line, no matter how many lines of real data you have.

What should the while condition be now? Since the sentinel is an
empty line, you might think ``line == ''``, but that is the
*termination* condition, not the *continuation* condition: You need
the *opposite* condition. To negate a condition in Python, you may
use ``not``, like in English,  ::

    not line == ''

Of course in this situation there is a shorter way, ::

    line != ''
    
Run the example program ``readLines2.py``, shown below:

.. literalinclude:: ../examples/readLines2.py
   :lines: 3-

Again the data for the test in the while loop heading must be
initialized before the first time the ``while`` statement is
executed and the test data must *also* be made ready inside the
loop for the test after the body has executed. Hence you see the
statements setting the variable ``line`` both before the loop and
at the end of the loop body. It is easy to forget the second place
inside the loop!

*After* reading the rest of this paragraph,
comment the last line of the loop out, and run it again:
It will never stop! The
variable ``line`` will forever have the initial value you gave it!
You actually can stop the program by entering :kbd:`Ctrl-C`. That means
hold the :kbd:`Ctrl` key and press :kbd:`c`.

.. note::
   As you finish coding a ``while`` loop, it is good practice to
   always double-check: Did I make a change to the variables, *inside*
   the loop, that will eventually make the loop condition ``False``?

The earliest ``while`` loop examples had numerical tests and the code
to get ready for the next loop just incremented a numerical variable
by a fixed amount.  Those were simple examples but ``while`` loops
are much more general!  In the interactive loop we have seen a continuation
condition with a string test, and getting ready for the next time through
the loop involves input from the user.

Some of the exercises that follow involve interactive while loops.
Others were delayed until here just because they have a wider variety of
continuation condition tests and ways to prepare for the next time through
the loop.  What is *consistent* is the general steps to think of and
questions to ask yourself.  They keep on applying!  Keep these in mind!

  * the need to see whether there *is* a kind of
    repetition, even without a fixed collection of values to work through

  * to think from the specific situation and figure out the
    continuation condition that makes sense for your loop

  * to think what specific processing or results you want each time through
    the loop, using the *same* code

  * to figure out what supporting code you need to make you ready for the
    next time through the loop:  how to make the *same* results code
    have *new* data values to process each time through, and eventually reach
    a stopping point.
    

.. _interactive-sumEx:
    
Interactive Sum Exercise
~~~~~~~~~~~~~~~~~~~~~~~~

Write a program ``sumAll.py`` that prompts the user to enter
numbers, one per line, ending with a line containing 0, and keep a
running sum of the numbers. Only print out the sum after all the
numbers are entered (at least in your *final* version).
Do *not* create a list!  Each time you read in a number, you can
immediately use it for your sum, and then be done with the number
just entered.

.. _Safe-Num-Input-Ex:

Safe Number Input Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~

\* There is an issue with reading in numbers with the input statement.
If you make a typo and enter something that cannot be converted from a
string to the right kind of number, a naive program will bomb.
This is avoidable if you test the string and repeat if the string is illegal.
In this exercise write safe utility function replacements
for the input function that work to read in a whole number, an integer or
a decimal number.

All parts refer to the previous
:ref:`Is-Number-String-Ex`.  Part a. refers to the introduction in the
previous exercise.
Parts b. and c. refer to functions in the solution, ``isNumberStr.py``, of
the previous exercise.
Make sure you look back at these first.

Save the example ``safeNumberInputStub.py`` as ``safeNumberInput.py``,
and complete it.
It contains headings and documentation strings
for the functions in each part of this exercise.

a.  This part considers the simplest case,
    where you are trying to enter a whole number.
    Complete the definition of the function ``safeWholeNumber``.

b.  Complete the function ``safeInt``.  This easily parallels part a.
    if you copy in and use the function (not method) ``isIntegerStr``.

c.  Complete the function ``safeDecimal``.  This easily parallels part b.
    if you copy in and use the function ``isDecimalStr``.

Savings Exercise
~~~~~~~~~~~~~~~~

The idea here is to see how many years it will take a bank account to grow
to at least a given value, assuming a fixed annual interest.
Write a program ``savings.py``.
Prompts the user for three numbers: an initial balance, the annual percentage
for interest as a decimal. like .04 for 4%, and the final balance desired.
Print the initial balance, and the balance each year until
the desired amount is reached. Round displayed amounts
to two decimal places, as usual.

The math:  The amount next year is the amount now times
(1 + interest fraction),
so if I have $500 now and the interest rate is .04,
I have $500*(1.04) = $520 after one year and after two years I have,
$520*(1.04) = $540.80.
If I enter into the program a $500 starting balance, .04 interest rate and
a target of $550, the program prints::

   500.00
   520.00
   540.80
   562.43

.. _Strange-Seq-Ex:   

Strange Sequence Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~

\* Recall :ref:`Strange-Func-Ex` and its ``jumpFunc.py`` 
which contains the function ``jump``:
For any integer n, jump(n) is n//2 if n is even, and 3*n+1 if n is odd.

You can start with one number, say n = 3, and *keep* applying the
jump function to the *last* number given, and see how the numbers jump around!
::

    jump(3) = 3*3+1 = 10; jump(10) = 10//2 = 5;
    jump(5) = 3*5+1 = 16; jump(16) = 16//2 = 8;
    jump(8) = 8//2 = 4; jump(4) = 4//2 = 2;
    jump(2) = 2//2 = 1

This process of repeatedly applying the same function to the most recent result
is called function *iteration*.  In this case you see that iterating the
jump function, starting from n=3, eventually reaches the value 1.

It is an open research question whether iterating the jump function
from an integer n will eventually reach 1,
for *every* starting integer n greater than 1.
Researchers have only found examples of n where it is true.
Still, no general argument has been made to apply to the
*infinite* number of possible starting integers.

In this exercise you iterate the jump function for specific
starting values n, until the result is 1.

a.  Save example ``jumpSeqStub.py`` as ``jumpSeq.py`` and complete the missing
    function bodies.  If you coded the function ``jump`` before in
    ``jumpFunc.py``, you can copy it.
    You can complete either ``printJumps`` or
    ``listJumps`` first, and test before completing the other. Hint [#]_


b.  After you have finished and saved ``jumpSeq.py`` copy it and save
    the file as ``jumpSeqLengths.py``.

    First modify the main method so it prompts the user
    for a value of n, and then prints just the length of the iterative sequence
    from listJumps(n).  Hint [#]_

    Then elaborate the program so it prompts the user for two integers:
    a lowest starting value of n
    and a highest starting value of n.
    For all integers n in the range from the lowest start through
    the highest start, including the highest,
    print a sentence giving the starting value of n
    and the length of the list from ``listJumps(n)``.  An example run::

        Enter lowest start: 3
        Enter highest start: 6
        Starting from 3, jump sequence length 8.
        Starting from 4, jump sequence length 3.
        Starting from 5, jump sequence length 6.
        Starting from 6, jump sequence length 9.
    



.. _Graphical-Applications:
    
Graphical Applications
----------------------

Another place where a ``while`` loop could be useful is in
interactive graphics. Suppose you want the user to be able to
create a Polygon by clicking on vertices they choose interactively,
but you do not want them to have to count the number of vertices
ahead of time. A ``while`` loop is suggested for such a repetitive
process. As with entering lines of text interactively, there is the
question of how to indicate that you are done (or how to indicate to
continue). If you make only a certain region be allowed for the
Polygon, then the sentinel can be a mouse click outside the region.
The earlier interactive color choice example already has a method
to check if a mouse click is inside a Rectangle, so that method can
be copied and reused.

Creating a polygon is a unified activity with a clear result, so
let's define a function. It involves a boundary rectangle and mouse
clicks in a GraphWin, and may as well return the Polygon
constructed. *Read* the following start:

.. literalinclude:: ../examples/makePoly.py
   :start-after: getY
   :end-before: setOutline
   
It is useful to start by thinking of the objects needed, and give
them names.

-  A Polygon is needed. Call it ``poly``.

-  A list of vertices is needed. Call it ``vertices``. I need to
   append to this list. It must be initialized first.

-  The latest mouse click point is needed. Call it ``pt``.

Certainly the overall process will be repetitious, choosing point
after point. Still it may not be at all clear how to make an
effective Python loop. In challenging situations like this it is
often useful to imagine a concrete situation with a limited number
of steps, so each step can be written in sequence without worrying
about a loop.

For instance to get up to a triangle (3 vertices in our list and a
fourth mouse click for the sentinel), you might imagine the
following sequence, undrawing each old polygon before the next is
displayed with the latest mouse click included::

        rect.setOutline('red')   
        rect.draw(win) 
        vertices = list()         
        pt = win.getMouse() 
        vertices.append(pt)   
        poly = Polygon(vertices)   
        poly.draw(win)          # with one point 
        pt = win.getMouse() 
        poly.undraw()           # missing latest point 
        vertices.append(pt)    
        poly = Polygon(vertices)   
        poly.draw(win)          # with two points 
        pt = win.getMouse() 
        poly.undraw()           # missing latest point 
        vertices.append(pt)    
        poly = Polygon(vertices)   
        poly.draw(win)          # with three points 
        pt = win.getMouse()  # assume outside the region 
         
        rect.undraw() 
        return poly 

There is a fine point here that *I* missed the first time. The
vertices of an existing Polygon do not get mutated in this system. A new
Polygon gets created each time with the new vertex list. The old
Polygon does not go away automatically, and extraneous lines appear
in the picture if the old polygon is not explicitly undrawn each
time before a new version is redrawn with an extra vertex.
The last Polygon you draw should be visible at the end, so in the example
above where I was assuming the third click was the last for the triangle,
I did not ``undraw`` the Polygon.  

The timing for each ``undraw`` needs to be after the next mouse click
and presumably before the next Polygon is created, so it could be
before or after the line ``vertices.append(pt)``. I arbitrarily
chose for it to go before the vertices list is changed. The rest
of the order of the lines is pretty well fixed by the basic logic.

If you think of the repetitions through a large number of loops,
the process is essentially circular (as suggested by the word
'loop'). The body of a loop in Python, however, is written as a
*linear* sequence: one with a first line and a last line, a
beginning and an end. We can cut a circular loop *anywhere* to get a piece
with a beginning and an end. In practice, the place you cut the
loop for Python has one main constraint: The processing in
Python from the end of one time through the loop to the beginning
of the next loop is
separated by the test of the condition in the heading.
The *continuation condition*
*in the* ``while`` *heading must make sense where you cut the loop.* 

.. index::
   double:  while; loop
   double:  while; split
   double:  loop; split
   
.. _where-split-loop: 

It can help to look at a concrete example sequence, like the steps
listed above for creating a triangle, only now assuming we do not know
how many vertices will be chosen. The continuation condition is
for ``pt`` to be in the rectangle, so using the previously written
function ``isInside``, the loop heading will be ::

    while isInside(pt, rect):

With this condition in mind, look for where to split to loop. It
needs to be after a new ``pt`` is clicked (so it can be tested) and
before the next Polygon is created (so it does not include the
sentinel point by mistake). In particular, with the sequence above,
look and see that the split could go before or after the
``poly.undraw()`` line. :ref:`Move-undrawEx` considers
the case where the split goes before this line. I will proceed with
the choice of splitting into a Python loop *after* the ``undraw`` line.
This makes the loop be ::

        while isInside(pt, rect): 
            vertices.append(pt)   
            poly = Polygon(vertices)   
            poly.draw(win) 
            pt = win.getMouse() 
            poly.undraw()

If you follow the total sequence of required steps above for making
the concrete triangle, you see that this *full* sequence for the
loop is only repeated twice. The last time there is no
``poly.undraw()`` step. I could redo the loop moving the undraw
line to the top, which caused different issues
(:ref:`Move-undrawEx` below). Instead *think* how to make it work at the
end of the final time through the loop....

There are several possible approaches. You want the ``undraw`` line
every time except for the last time. Hence it is a statement you
want sometimes and not others. That suggests an ``if`` statement.
The times you want the ``undraw`` are when the loop will repeat
again. This is the same as the continuation condition for the loop,
and you have just read the next value for ``pt``! You could just
add a condition in front of the last line of the loop::

            if isInside(pt, rect): 
                poly.undraw() 

I find this option unaesthetic: it means duplicating the
continuation test twice in every loop.

Instead of *avoiding* the ``undraw`` as you exit the loop, another
option in this case is to *undo* it: just **re**\ draw the polygon one
final time *beyond* the loop. This only needs to be done once, not
repeatedly in the loop. Then the repetitious lines collapse neatly
into the loop.  If you look at the overall concrete sequence for the triangle,
not all the lines are in the loop.  You must carefully include the lines
both that come before the loop and those that come after the loop.
Make sure these lines are not put *in* the loop, but before or after,
as indicated by the concrete sequence in the example.
In the end the entire function is:

.. literalinclude:: ../examples/makePoly.py
   :start-after: getY
   :end-before: main
   
Make sure you understand:
Follow this code through, imagining three mouse clicks inside rect
and then one click outside of rect. Compare the steps to the ones
in the concrete sequence written out above and see that the match
(aside from the last canceling ``undraw`` and ``draw`` of ``poly``).

This function is illustrated in the example program
``makePoly.py``. Other than standard graphics example code, the
main program contains:

.. literalinclude:: ../examples/makePoly.py
   :start-after: instructions.draw
   :end-before: promptClose
   
As you can see, the returned polygons are used to make color
changes, just as an illustration.

--------

.. index::
   double:  animation; while
   double:  animation; checkMouse
   
In earlier animation examples a ``while`` loop would also have been
useful. Rather than continuing the animation a fixed number of
times, it would be nice for the user to indicate by a mouse click
when she has watched long enough. Thus far the only way to use the
mouse has been with ``getMouse()``. This is not going to work in an
animation, because the computer stops and *waits* for a click with
``getMouse()``, whereas the animation should *continue until* the
click.

In full-fledged graphical systems that respond to events, this is
no problem. Zelle's graphics is built on top of a capable
event-driven system, and in fact, all mouse clicks are registered,
even outside calls to ``getMouse()``.

As an example, run example program ``randomCirclesWhile.py``. Be
sure to follow the prompt saying to click to start *and* to end.

Aside from the prompts, the difference from the previous
``randomCircles.py`` program is the replacement of the original
simple repeat loop heading ::

        for i in range(75): 

by the following initialization and while loop heading::

        while win.checkMouse() == None:      #NEW* 

The graphics module remembers the last mouse click, whether or not
it occurred during a call to ``getMouse()``. A way to
check if the mouse has been clicked since the last call to ``getMouse()``
is ``checkMouse()``. It does not *wait* for the mouse as in
``getMouse()``. Instead it returns the *remembered* mouse click -
the most recent mouse click in the *past*, unless there has been no
mouse click since the last call to getMouse or checkMouse. In that
case ``checkMouse()`` returns None (the special object used to
indicate the lack of a regular object).

The ``checkMouse`` method allows for a loop that does not stop
while waiting for a mouse click, but goes on until the heading test
detects that the mouse *was* clicked.

A similar elaboration can be made for the other examples of
animation, like ``bounce1.py``. In ``bounceWhile.py`` I modified
``bounce1.py`` to have a while loop in place of the for-loop
repeating 600 times. Run it. The only slight added modification
here was that ``win`` was not originally a parameter to
``bounceInBox``, so I included it. Look at the source code for
``bounceWhile.py``, with the few changes marked NEW.

In ``bounce2.py`` I also made a more interesting change to the
initialization, so the initial direction and speed of the mouse are
determined graphically by the user, with a mouse click. Try example
program ``bounce2.py``.

The program includes a new utility function to help determine the
initial (dx, dy) for the animation. This is done by calculating the
move necessary to go from one point (where the ball is in this
program) to another (specified by a user's mouse click in this
program). :

.. literalinclude:: ../examples/bounce2.py
   :start-after: return disk
   :end-before: getUserShift

Since the function calculates both a change in x and y, it returns
a ``tuple``.

A straightforward interactive method, ``getUserShift``, is wrapped
around this function to get the user's choice, which ultimately
returns the same tuple:

.. literalinclude:: ../examples/bounce2.py
   :start-after: return (dx, dy)
   :end-before: bounceBall

In the new version of the main driver, ``bounceBall``, excerpted
below, this interactive setting of (dx, dy) is used. Note the
multiple assignment statement to both dx and dy, set from the tuple
returned from ``getUserShift``. This shift would generally be much
too much for a single animation step, so the actual values passed
to bounceBall are scaled way down by a factor ``scale``.

.. literalinclude:: ../examples/bounce2.py
   :start-after: win.getHeight()
   :end-before: win.close()

The ``bounceInBox`` method has the same change to the loop as in
the randomCircles.py example. The method then requires the
``GraphWin``, ``win``, as a further parameter, since ``checkMouse``
is a ``GraphWin`` method.

You can look in Idle at the full source code for ``bounce2.py`` if
you like. The changes from ``bounce1.py`` are all marked with a
comment starting with ``#NEW``, and all the major changes have been
described above.

In the examples so far of the use of ``checkMouse()``, we have only
used the fact that a point was clicked, not *which* point. The next
example version, ``bounce3.py``, does use the location of mouse
clicks that are read with ``checkMouse()`` to change the direction
and speed of the ball. Try it.

This version only slightly modifies the central animation function,
``bounceInBox``, but wraps it in another looping function that
makes the direction and speed of the ball change on *each* mouse
click. Hence the mouse clicks detected in ``bounceInBox`` need to
be remembered and then returned after the main animation loop
finishes. That requires a name, ``pt``, to be given to the last
mouse click, so it can be remembered. This means modifying the main
animation loop to initialize the variable ``pt`` before the loop
and reset it at the end of the loop, much as in the use of
getMouse() for the interactive polygon creation. That explains the
first three NEW lines and the last two NEW lines in the revised
``bounceInBox``:

.. literalinclude:: ../examples/bounce3.py
   :start-after: random
   :end-before: moveOInBox

I initially made only the changes discussed so far (not the ones
involving the new variable ``isInside``). The variable ``isInside``
was in response to a bug that I will discuss after introducing the
simple function that wraps around ``bounceInBox``:

Each time the mouse is clicked, the ball is to switch direction and
move toward the last click, until the stopping condition occurs,
when there is a click above the stop line. This is clearly
repetitive and needs a while loop. The condition is simply to test
the y coordinate of the mouse click against the the height of the
stop line. The body of the loop is very short, since we already
have the utility function ``getShift``, to figure out (dx, dy)
values.

.. literalinclude:: ../examples/bounce3.py
   :start-after: return pt
   :end-before: makeDisk

The variable ``pt`` for the last mouse click needed to be
initialized some way. I chose to make the value be the same as the
initial position of the ball, so both dx and dy are initially 0,
and the ball does not start in motion. (Alternatives are in
:ref:`random-start` below.)

I occasionally detected a bug when using the program. The ball
would get stuck just outside the boundary and stay there. The fact
that it was slightly beyond the boundary was a clue: For simplicity
I had cheated, and allowed the ball to go just one animation step
beyond the intended boundary. With the speed and small step size
this works visually. The original code was *sure* to make an
opposite jump back inside at the next step.

After some thought, I noticed that the initial version of the
bounce3.py code for ``bounceInBox`` broke that assumption. When the
ball was where a bounce-back is required, a mouse click could
change (dx, dy) and mess up the bounce. The idea for a fix is not
to let the user change the direction in the moment when the ball
needs to bounce back.

Neither of the original boundary-checking ``if`` statements, by
*itself*, always determines if the ball is in the region where it
needs to reverse direction. I dealt with this situation by
introducing a *Boolean variable* ``isInside``. It is initially set
as ``True``, and then either of the ``if`` statements can correct
it to False. Then, at the end of the loop, ``isInside`` is used to
make sure the ball is safely inside the proper region when there is
a check for a new mouse click and a possible user adjustment to
(dx, dy).


.. _Move-undrawEx:

Exercise Moving Undraw
~~~~~~~~~~~~~~~~~~~~~~

\*\* As discussed above at :ref:`Where to split the loop <where-split-loop>`,
the basic loop logic
works whether the ``poly.undraw()`` call is at the beginning or end
of the loop. Write a variation ``makePoly2.py`` that makes the code
work the other way, with the ``poly.undraw()`` at the beginning of
the loop. The new place to cut the loop *does* affect the code
before and after the loop. In particular, the extra statement
drawing ``poly`` is not needed after the loop is completed. Make
other changes to the surrounding code to make this work. Hints: [#]_


Make Path Exercise
~~~~~~~~~~~~~~~~~~

\*\* Write a program very similar to ``makePoly.py``, and call it
``makePath.py``, with a function ``pathHere``. The only outward
difference between ``polyHere`` and ``pathHere`` is that while the
first creates a closed polygon, and returns it, and the new one
creates a polygonal path, without the final point being
automatically connected to the first point, and a list of the lines
in the path is returned. Internally the functions are quite
different. The change simplifies some things: no need to undraw
anything in the main loop - just draw the latest segment each time
going from the previous point to the just clicked point. There is a
complication however, you do need deal specially with the first
point. It has no previous point to connect to. I suggest you handle
this *before* the main loop, and draw the point so it is a visible
guide for the next point. After your main loop is finished undraw
this initial point. (The place on the screen will still be visible
if an initial segment is drawn. If no more points were added, the
screen is left blank, which is the way it should be.) You also need
to remember the previous point each time through the main loop.

In your main program, test the ``makePath`` function several times.
Use the list of lines returned to loop and change the color in one
path and the width of the lines in another path. A portion of a
sample image is shown below after all this is done.

.. figure:: images/polylines.*
   :align: center
   :alt: image
   :width: 231.75 pt

.. _random-start:
    
Random Start Exercise
~~~~~~~~~~~~~~~~~~~~~

\* (Optional) I chose to have the ball
start motionless, by making the initial value of ``pt`` (which
determines the initial (dx, dy) ) be the center of the ball. Write
a variation ``startRandom.py`` so ``pt`` is randomly chosen. Also
make the initial location of the ball be random. You can copy the
function ``getRandomPoint`` from bounce1.py.

.. index:: madlib; while exercise
   exercise; madlib while
   
.. _mad-lib-while-exercise:

Mad Lib While Exercise
~~~~~~~~~~~~~~~~~~~~~~

\*\* Write a program ``madlib4.py`` that modifies the
``getKeys`` method of ``madlib2.py`` to use a ``while`` loop. (This
is not an animation program, but this section is where you have had
the most experience with while loops!) 

Hints:  This is actually the most natural approach. I avoided ``while``
loops initially, when only ``for`` loops had been discussed. It is
redundant in the original approach, however, to find every instance
of ``'{'`` to *count* the number of repetitions and then *find* them
all again when extracting the cue keys. A more natural way to
control the loop is a ``while`` loop stopping when there are no
further occurrences of ``'{'`` to ``find``. This involves some further
adjustments. You must cut the loop in a different place (to end
after searching for ``'{'``). As discussed before, cutting a loop
in a different place may require changes before and after the loop,
too.

Find Hole Game Exercise
~~~~~~~~~~~~~~~~~~~~~~~

\*\* Write a graphical game program, ``findHole.py``,
"Find the Hole". The program should use a random number generator
to determine a circular "hole", selecting a point and a perhaps the
radius around that point. These
determine the target and are not revealed to the player initially.
The user is then prompted to click around on the screen to
"find the hidden hole". You should show the points the user has
tried. Once the user selects a point that is within the chosen
radius of the mystery point, the mystery circle should appear. There
should be a message announcing how many steps it took, and the game
should end.

Hint: you have already seen the code to determine the displacement
(dx, dy) between two points: use the ``getShift`` function in
``bounce2.py``. Once you have the displacement (dx, dy) between the
hidden center and the latest mouse click, the distance between the
points is ``(dx*dx + dy*dy)**0.5``, using the Pythagorean
Theorem of geometry. If this distance is no more than the radius
you have chosen for the mystery circle, then the user has found the
circle! You can use ``getShift`` as written, or modify it into a
function ``getDistance`` that directly returns the distance between
two points.

Many elaborations on this game are possible! Have fun with it!


.. _Fancier-Animation-Loop:
    
Fancier Animation Loop Logic (Optional)
---------------------------------------

.. index::
   single:  return; without a value
   
The final variation is the example program ``bounce4.py``, which
has the same outward behavior as bounce3.py, but it illustrates a
different internal design decision. The bounce3.py version has two
levels of while loop in two methods, ``moveInBox`` for mouse clicks
and ``bounceInBox`` for bouncing. The bounce4.py version puts all
the code for changing direction inside the main animation loop in
the old outer function, ``moveInBox``. There are now three reasons
to adjust (dx, dy): bouncing off the sides, bouncing off the top or
bottom, or a mouse click. That is a simplification and unification
of the logic in one sense. The complication now is that the logic
for determining when to quit is buried deep inside the |if-else|
logic, not at the heading of the loop. The test for mouse clicks is
inside the ``while`` loop and further inside another ``if`` statement. The
test of the mouse click may merely lead to a change in (dx, dy), or
is a signal to quit. Here is the revised code, with a discussion
afterward of the return statement:

.. literalinclude:: ../examples/bounce4.py
   :start-after: random
   :end-before: makeDisk
   
Recall that a ``return`` statement immediately terminates function
execution. In this case the function returns no value, but a bare
``return`` is legal to force the exit. Since the testing is not
done in the normal ``while`` condition, the ``while`` condition is
set as permanently ``True``. This is not the most common ``while``
loop pattern! It obscures the loop exit. The choice between the
approach of ``bounce3.py`` and ``bounce4.py`` is a matter of taste in the
given situation.

.. [#]  You will need a loop.
   You can print/append almost all the numbers in the loop.
   You are likely to omit one number with just this code,
   but after looking at what you produce, it is easy to separately
   include the remaining number.  There are several ways to do this.

.. [#]  Recall the built-in ``len`` function!
   It applies to lists.

.. [#]  The basic issue is similar to the old version: the undraw is not
   always needed, at the beginning in this case. In this place it is not
   need the *first* time through the loop. The two basic approaches
   considered for the previous version still work here: break into
   cases inside the loop or make an extra compensating action outside
   the loop. Further hint: It is legal to draw a polygon with an empty
   vertex list - nothing appears on the screen.
