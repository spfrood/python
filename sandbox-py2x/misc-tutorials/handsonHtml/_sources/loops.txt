
.. _Loops-and-Sequences:

Loops and Sequences
===================

Modern computers can do millions or even billions of instructions a
second. With the techniques discussed so far, it would be hard to
get a program that would run by itself for more than a fraction of
a second.  [#recursion]_

Practically, we cannot write millions of instructions to keep
the computer busy. To keep a computer doing useful work we need
*repetition*, looping back over the same block of code again and
again. There are two Python statement types to do that: the simpler
``for`` loops, which we take up shortly, and ``while`` loops, which
we take up later, in :ref:`While-Statements`.

Two preliminaries: 

#.  The value of already defined variables can be
    updated. This will be particularly important in loops. To prepare for that we
    first follow how variables can be updated in an even simpler, *sequential*
    situation. 
#.  Sequence types are used in ``for`` loops.  We will
    look at a basic sequence type: ``list``. 
    
Then we put this all together.  This is a long
section. Go slowly and carefully.

.. [#recursion]
   It is possible with function recursion, but we will avoid that
   advanced topic in this introduction.


.. match ]]

.. index::
   single: variable; update

.. _Updating-Variables:

Updating Variables
------------------

The programs so far have defined and used variables, but other than
in early shell examples we have not changed the value of existing
variables. For now consider a particularly simple example, just
chosen as an illustration, in the example file ``updateVar.py``:

.. literalinclude:: ../examples/updateVar.py
   :linenos:
       
Can you *predict* the result? Run the program and check.
Particularly if you did not guess right, it is important to
understand what happens, one step at a time. That means keeping
track of what changes to variables are made by each statement.

In the table below, statements are referred to by the numbers labeling
the lines in the code above. We can track the state of each
variable after each line is executed. A dash is shown where a
variable is not defined. For instance after line 1 is executed, a
value is given to x, but y is still undefined. Then y gets a value
in line 2. The comment on the right summarizes what is happening.
Since x has the value 3 when line 2 starts, x+2 is the same as 3+2.
In line three we use the fact that the right side of an assignment
statement uses the values of variables when the line starts
executing (what is left after the previous line of the table
executed), but the assignment to the variable y on the left causes
a change to y, and hence the updated value of y, 10, is shown in
the table. Line 4 then changes x, using the *latest* value of y
(10, not the initial value 5!). The result from line 5 confirms the
values of x and y.

====  ==  ==  =======================================
Line  x   y   Comment
====  ==  ==  =======================================
1     3   \-  
2     3   5   5=3+2, using the value of x from the previous line
3     3   10  10=2*5 on the right, use the value of y from the
              previous line
4     7   10  7=10-3 on the right, use the value of x and y from the
              previous line
5     7   10  print: 7 10
====  ==  ==  =======================================

The order of execution will always be the order of the lines in the
table. In this simple *sequential* code, that *also* follows the
textual order of the program. Following each line of execution of a
program in the proper order of execution, carefully, 
keeping track of the current values of
variables, will be called *playing computer*. A table like the one
above is an organized way to keep track.

.. index::
   double: list; type

.. _The-list-Type:

The ``list`` Type
-----------------

Lists are ordered sequences of arbitrary data. Lists are the first
kind of data discussed so far that are *mutable*: the length of the
sequence can be changed and elements substituted. We will delay the
discussion of changes to lists until a further introduction to
objects. Lists can be written explicitly. *Read* the following
examples ::

    ['red', 'green', 'blue'] 
    [1, 3, 5, 7, 9, 11] 
    ['silly', 57, 'mixed', -23, 'example'] 
    [] # the empty list 


The basic format is a square-bracket-enclosed, comma-separated list
of arbitrary data.

.. index::
   single: function; range, one parameter
   single: range; one parameter

.. _The-range-Function-I:

The ``range`` Function, Part 1
------------------------------

There is a built-in function ``range``, that can be used to
automatically generate regular arithmetic sequences. Try the
following in the *Shell*::

    list(range(4)) 
    list(range(10)) 


The general pattern for use is

    ``range(``\ *sizeOfSequence*\ ``)``

This syntax will generate the integers, one at a time, *as needed* [#lazy]_. If
you want to see all the results at once as a list, you can convert
to a ``list`` as in the examples above. The resulting sequence starts
at 0 and ends *before* the parameter. We will see there are good
reasons to start from 0 in Python. One important property of
sequences generated by ``range(n)`` is that the total number of
elements is ``n``. The sequence omits the number ``n`` itself, but
includes 0 instead.

With more parameters, the ``range`` function can be used to
generate a much wider variety of sequences. The elaborations are
discussed in :ref:`Random-Colors` and
:ref:`The-general-range-function`.

..  [#lazy]
    In computer jargon, producing values of a sequence only as needed is called
    *lazy* evaluation.

.. index::
   loop; for statement
   for; statement
   statement; for loop
   single: :; end of heading

.. _Basic-for-Loops:

Basic ``for`` Loops
-------------------

Try the following in the *Shell*. You get a sequence of
continuation lines before the Shell responds. Be sure to indent the
second and third lines. (In an
edit window the indentation is automatic).
*Be sure to enter another empty line.* (Just press :kbd:`Enter`.)
*at the end to get the Shell to respond.* :

.. literalinclude:: ../examples/firstloop.py
   :linenos:
       
This is a ``for`` loop. It has the heading starting with ``for``,
followed by a variable name (``count`` in this case), the word
``in``, some sequence, and a final colon. As with function
definitions and other heading lines, the colon
at the end of the line indicates that a consistently indented block
of statements follows to complete the ``for`` loop. 

| ``for`` **item** ``in`` *sequence*\ ``:``
|     indented statements to repeat; may use **item**

The block of lines is repeated once for each element of the
sequence, so in this example the two lines in the indented block
are repeated three times. Furthermore the variable in the heading
(``count`` here) may be used in the block, and each time through it
takes on the *next* value in the sequence, so the first time
through the loop ``count`` is 1, then 2, and finally 3. Look again
at the output and see that it matches this sequence.  A more detailed
sequence is given, playing computer, in the table:
    
====  =====  =======================
Line  count  comment
====  =====  =======================
1     1      start with the first element of the list
2     1      print 1
3     1      'yes' * 1 is 'yes'; print yes 
1     2      change count to the next element in the list
2     2      print 2
3     2      'yes' * 2 is 'yesyes'; print yesyes; 
1     3      change count to the next element in the list
2     3      print 3
3     3      'yes' * 3 is 'yesyesyes'; print yesyesyes; done with list
====  =====  =======================

When executing step by step, note that the ``for`` loop heading serves *two*
purposes:
    
*   Each time the heading line executes, it implicitly assigns a new value to
    the variable name you use in place of **item**.

*   After each execution of the heading line, the statements in the
    indented block are executed,
    generally making use of the the new value for the variable assigned in the
    heading.

.. note::
   When playing computer with a loop, the same line numbers can
   reappear over and over, because the ``for`` loop heading line
   and the indented body under it are each executed repeatedly,
   and each time it is executed must be listed separately, in time sequence!
   
When you used the *Shell* to enter a loop,
there was a reason that the interpreter waited to respond until after you
entered an empty line: The interpreter did not know how long the
loop block was going to be! The empty line is a signal to the
interpreter that you are done with the loop block.

Look at the following example program ``for123.py``, and run it. 

.. literalinclude:: ../examples/for123.py

In a file, where the interpreter does not need to respond
immediately, the blank line is not necessary. Instead, as with a
function definition or any other format with an indented block, you
indicate being past the indented block by **de**\ denting to line up
with the ``for``-loop heading. Hence in the code above,
"Done Counting." is printed once after the first loop completes
all its repetitions. Execution ends with another simple loop.

As with the indented block in a function, it is important to get
the indentation right. Alter the code above, so the fourth line is
indented:

.. literalinclude:: ../examples/for123a.py

Predict the change, and run the code again to test.

.. index:: 
   double: loop; for-each
    
Loops are one of the most important features in programming. While
the ``for`` loop syntax is pretty simple, using them creatively to solve
problems (rather than just look at a demonstration) is among the
biggest challenges for many learners at an introductory level. One
way to simplify the learning curve is to classify common situations
and patterns, and give them names. 
One of the simplest patterns is illustrated in all of the ``for`` loop examples
so far, a simple *for-each* loop:  **For each** element of the sequence, 
do the same sort of thing with it.  Stated as mor Pythonic pseudocode:

| ``for`` **item** ``in`` *sequence*\ ``:`` 
|     do something with the current **item** 

(It would be even more like English if ``for`` were replace by
``for each``, but the shorter version is the one used by Python.)

In the ``for`` loop examples above, something is printed that is
related to each item in the list. Printing is certainly one form of
"do something", but the possibilities for "do something" are
completely general!

We can use a for-each loop to revise our first example. *Recall*
the code from madlib.py::

        addPick('animal', userPicks)                 
        addPick('food', userPicks)                   
        addPick('city', userPicks)                   


Each line is doing exactly the same thing, except varying the
string used as the cue, while repeating the rest of the line.  This
is the for-each pattern, but we need to list the sequence that the
cues come from. *Read* the alternative::

    for cue in ['animal', 'food', 'city']:  # heading 
        addPick(cue, userPicks)             # body               

Seeing
this feature requires the ability to *abstract* the general pattern from
the group fo examples.  This is essential for using loops effectively.

If you wish to see or run the whole program with this small
modification, see the example ``madlibloop.py``.  A common naming convention is used
in the program:
Each element in the list is a ``cue``, while the list with all the elements is 
named with the plural ``cues``.  In later situations I make a list name be the
plural of the variable name used for an individual item of the list.

Note the logic of the transformation between the two program versions:
The alternative pieces of data are collected in the list in the
``for`` loop heading.
A single
variable name (here I chose ``cue``) is used in the heading as a placeholder
to refer to the *current* choice being handled, and the body refers to this 
variable ``cue`` in place of the explicit data values included each time
in the original no-loop version.

.. index::
   for; execution sequence
   sequence; for loop
   execution; sequence with for loop

It is important to understand the sequence of operations, how
execution goes back and forth between the heading and the body.
Here are the details:

#. heading first time: variable ``cue`` is set to the first element
   of the sequence, ``'animal'``

#. body first time: since ``cue`` is now ``'animal'``, effectively
   execute ``addPick('animal', userPicks)`` (Skip the details of the
   function call in this outline.)

#. heading second time: variable ``cue`` is set to the next element
   of the sequence, ``'food'``

#. body second time: since ``cue`` is now ``'food'``, effectively
   execute ``addPick('food', userPicks)``

#. heading third time: variable ``cue`` is set to the next (last)
   element of the sequence, ``'city'``

#. body third time: since ``cue`` is now ``'city'``, effectively
   execute ``addPick('city', userPicks)``

#. heading done: Since there are no more elements in the sequence,
   the entire ``for`` loop is done and execution would continue with
   the statement after it (not indented).

In this example the data values are just a few given literals,
and there is only one line in the repeated pattern.  Hence the use of a ``for`` loop
is not a big deal, but it makes a simple example!
This looping construction would be much handier if you were to
modify the original mad lib example, and had a story with many more
cues. Also this revision will allow for further improvements in
:ref:`The-Revised-Mad`, after we introduce more about string
manipulation.

Pattern Loop Exercise 
~~~~~~~~~~~~~~~~~~~~~

Write a two-line for-each loop in a file ``types2.py``
containing a call to the ``type`` function
that will have the same effect as this code in example file ``types1.py``:

.. literalinclude:: ../examples/types1.py
   :lines: 1-5
   
Execute both versions to check yourself.  Hint1: [#type2Hint1]_  Hint2: [#type2Hint2]_

.. match ]]
       
 
Triple Exercise 
~~~~~~~~~~~~~~~

Complete the following function. This starting code is in
``tripleStub.py``. Save it to the *new* name ``triple.py``. Note
the way an example is given in the documentation string. It
simulates the use of the function in the Shell. This is a common
convention:

.. literalinclude:: ../examples/tripleStub.py
   :lines: 3-12
 
.. [#type2Hint1]
   The elements of the list in the ``for`` loop heading 
   are not all of the same type. 

.. [#type2Hint2]
   You need to use the loop variable twice in the loop body. 


.. index::
   loop; repeat - simple
   repeat loop - simple
   for; simple repeat loop
   simple repeat loop

.. _Simple-Repeat-Loop:

Simple Repeat Loop
-------------------

The examples above all used the value of the variable in the
``for`` loop heading. An even simpler ``for`` loop usage is when
you just want to repeat the *exact* same thing a specific number of
times. In that case only the *length* of the sequence, not the
individual elements are important. We have already seen that the
``range`` function provides an ease way to produce a sequence with
a specified number of elements. Read and run the example program
``repeat1.py``:

.. literalinclude:: ../examples/repeat1.py

In this situation, the variable ``i`` is not used inside the body
of the for-loop.

The user could choose the number of times to repeat. Read and run
the example program ``repeat2.py``:

.. literalinclude:: ../examples/repeat2.py

.. index:: loop; successive modification
   successive modification loop

.. _Successive-Modification-Loops:

Successive Modification Loops
-----------------------------

Suppose I have a list of items called ``items``, and I want to
print out each item and number them successively. For instance if
``items`` is ``['red', 'orange', 'yellow', 'green']``, I would
*like* to see the *output*::

    1 red 
    2 orange 
    3 yellow 
    4 green 

*Read about the following thought process for developing this:*

If I allow myself to omit the numbers, it is easy: For any ``item``
in the list, I can process it with ::

    print(item) 

and I just go through the list and do it *for each* one. (Copy and
run if you like.)  ::

    items = ['red', 'orange', 'yellow', 'green']  
    for item in items: 
        print(item) 

Clearly the more elaborate version with numbers has a pattern with
some consistency, each line is at least in the form:

    number item


but the number changes each time, and the numbers do *not* come
straight from the list of items.

A variable can change, so it makes sense to have a variable
``number``, so we have the potential to make it change correctly.
We could easily get it right the first time, and then repeat the
*same* number. Read and run the example program
``numberEntries1.py``:

.. literalinclude:: ../examples/numberEntries1.py

Of course this is still not completely correct, since the idea was
to *count*. After the first time number is printed, it needs to be
changed to 2, to be right the next time through the loop, as in the
following code: Read and run the example program
``numberEntries2.py``:

.. literalinclude:: ../examples/numberEntries2.py

This is closer, but still not completely correct, since we never
get to 3! We need a way to change the value of number
*that will work each time through the loop*. The pattern of
counting is simple, so simple in fact that you probably do not
think consciously about how you go from one number to the next: You
can describe the pattern by saying each successive number is
*one more than the previous number*. We need to be able to change
``number`` so it is one more than it was before. That is the
additional idea we need! Change the last line of the loop body to
get the example program numberEntries3.py. See the addition and run
it:

.. index::
   for; execution sequence
   execution; for loop sequence
   sequence; for loop

.. index:: playing computer

.. literalinclude:: ../examples/numberEntries3.py
   :linenos:

It is important to understand the step-by-step changes during
execution. Below is another table showing the results of playing
computer. The line numbers are much more important here to keep
track of the flow of control, because of the jumping around at the
end of the loop.

Again note that the program line numbers in the Line column of the
playing computer
table are *not* all sequential, because the ``for`` loop heading line
and the indented body under it are each executed repeatedly.

For compactness, the variable ``items`` does not get its own column,
since it always has the value shown in the comment in line 1:

====  =========  ======  ==================
line  item       number  comment
====  =========  ======  ==================
1     \-         \-      set items to ['red', 'orange','yellow', 'green']
2     \-         1
3     'red'      1       start with item as first in sequence
4     'red'      1       print: 1 red
5     'red'      2       2 = 1+1
3     'orange'   2       on to the next element in sequence
4     'orange'   2       print 2 orange
5     'orange'   3       3=2+1
3     'yellow'   3       on to the next element in sequence
4     'yellow'   3       print 3 yellow
5     'yellow'   4       4=3+1
3     'green'    4       on to the last element in sequence
4     'green'    4       print 4 green
5     'green'    5       5=4+1
3     'green'    5       sequence done, end loop and code
====  =========  ======  ==================

The final value of number is never used, but that is OK. What we
want gets printed.

Go through carefully and
be sure you understand the meaning of each entry in the table, and the
reason for the sequencing and the reason for the exact position of
each entry in each step where it changes!
In particular see how and why the line number for each
successive row is *not* always one more than the previous row.  In
particular, see how *the same sequence of numbered lines may be repeated*
in multiple places in the table.
Without this understanding you will not be able to play computer yourself
and really understand loops.

This short example illustrates a lot of ideas important to loops:

-  Loops may contain several variables.

-  One way a variable can change is by being the variable in a
   ``for`` loop heading, that automatically goes through the values in the
   ``for`` loop list.

-  Another way to have variables change in a loop is to have an
   explicit statement that changes the variable inside the loop,
   causing *successive modifications*.


There is a general pattern to loops with successive modification of
a variable like ``number`` above:

#. The variables to be modified need *initial* values *before* the
   loop (line 1 in the example above).

#. The loop heading causes the repetition. In a for-loop, the
   number of repetitions is the same as the size of the list.

#. The body of the loop generally "does something" (like print
   above in line 4) that you want done repeatedly.

#. There is code inside the body of the loop to set up for the
   *next* time through the loop, where the variable which needs to
   change gets transformed to its next value (line 5 in the example
   above).

.. index:: loop; outline

This information can be put in a code outline:

| Initialize variables to be modified 
| Loop heading controlling the repetition: 
|     Do the desired action with the current variables
|     Modify variables to be ready for the action the next time

If you compare this pattern to the for-each and simple repeat loops
in :ref:`Basic-for-Loops`, you see that the examples there
were simpler. There was no explicit variable modification needed to
prepare for the next time though the loop. We will refer to the
latest, more general pattern as a *successive modification* loop.

Functions are handy for encapsulating an idea for use and reuse in
a program, and also for testing. We can write a function to number
a list, and easily test it with different data. Read and run the
example program ``numberEntries4.py``:

.. literalinclude:: ../examples/numberEntries4.py

Make sure you can follow the whole sequence, step by step! This
program has the most complicated flow of control so far, changing
both for function calls and loops.


#. Execution start with the very last line, since the previous
   lines are definitions

#. Then ``main`` starts executing.

#. The first call to ``numberList`` effectively sets the formal
   parameter ::

       items = ['red', 'orange', 'yellow', 'green']
       
   and the function executes just like the flow followed in
   ``numberEntries3.py``. This time, however, execution returns to
   main.

#. An empty line is printed in the second line of main.

#. The second call to ``numberList`` has a different actual
   parameter ``['apples', 'pears', 'bananas']``, so this effectively
   sets the formal parameter this time ::
   
       items = ['apples', 'pears', 'bananas']
       
   and the function executes in a similar pattern as in
   ``numberEntries3.py``, but with different data and one less time
   through the loop.

#. Execution returns to main, but there is nothing more to do.

.. index::
   loop; accumulation
   accumulation loop
   for; accumulation loop

.. _Accumulation-Loops:

Accumulation Loops
------------------

Suppose you want to add up all the numbers in a list, ``nums``. Let
us plan this as a function from the beginning, so *read* the code
below. We can start with::

    def sumList(nums): 
        '''Return the sum of the numbers in nums.''' 

.. index:: concrete case

If you do not see what to do right away, a useful thing to do is
write down a *concrete* case, and think how you would solve it, in
complete detail. If ``nums`` is ``[2, 6, 3, 8]``, you would
likely calculate: 
     
    |    2 + 6 is 8
    |    8 + 3 is 11
    |    11 + 8 is 19
    |    19 is the answer to be returned.

Since the list may be arbitrarily long, you need a loop. Hence you
must find a *pattern* so that you can keep reusing the
*same statements* in the loop. Obviously you are using each number
in the sequence in order. You also generate a sum in each step,
which you reuse in the next step. The pattern is different,
however, in the first line, 2+6 is 8: there is no previous sum, and
you use two elements from the list. The 2 is not added to a
previous sum.

Although it is not the shortest way to do the calculation
*by hand*, 2 is a sum of 0 + 2: We can make the pattern consistent
and calculate:
     
    |    start with a sum of 0
    |    0 + 2 is 2
    |    2 + 6 is 8
    |    8 + 3 is 11
    |    11 + 8 is 19
    |    19 is the answer.

Then the second part of each sum is a number from the list,
``nums``. If we call the number from the list ``num``, the main
calculation line in the loop could be ::

    nextSum = sum + num

The trick is to use the same line of code the next time through the
loop. That means what *was* ``nextSum`` in one pass becomes the
``sum`` in the next pass. One way to handle that is::

    sum = 0 
    for num in nums: 
        nextSum = sum + num 
        sum = nextSum 

Do you see the pattern? Again it is

    | initialization 
    | loop heading: 
    |     main work to be repeated 
    |     preparation for the next time through the loop 

Sometimes the two general loop steps can be combined. This is such
a case. Since ``nextSum`` is only used once, we can just substitute
its value (``sum``) where it is used and simplify to::

    sum = 0 
    for num in nums: 
        sum = sum + num 

so the whole function, with the ``return`` statement is:

.. literalinclude:: ../examples/sumNums.py
   :linenos:
   :lines: 1-6

The example program :file:`sumNums.py` has the code above with
the following line added at the end to test the
function (not indented). *Run* :file:`sumNums.py`.  ::

    print(sumList([5, 2, 4, 7]))

The pattern used here is certainly successive modification (of the
``sum`` variable). It is useful to give a more specialized name for
this version of the pattern here. It follows an *accumulation*
pattern:

| initialize the *accumulation* to include none of the *sequence* (``sum = 0`` here) 
| ``for`` *item* ``in`` *sequence* ``:`` 
|     new value of *accumulation* = result of combining *item* with last value of *accumulation* 

This pattern will work in many other situations besides adding
numbers.

Play Computer sumList Exercise 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose the function ``sumList``, defined above,
is called with the parameter
``[5, 2, 4, 7]``. Play computer on this call, using the file
:file:`playComputerSumStub.rtf`, opened
from an *operating system* window
for the examples directory. Do *not* open in Idle.
The file should come up in your usual word processor.
Immediately save the file as
:file:`playComputerSum.rtf`, and fill in blank cells in the table.

Make sure there is a
row in the table for each line executed in the program,
with a *separate* line entry for *each time a line is executed*.
In each row enter which program line is being
executed, and show all changes caused to variables by the execution
of that one line.
Display line numbers as shown in the margin beside the example code
*in the Tutorial*.
(The separate Python files themselves do not show the line numbers.)
A table is started for you below. The final row that you enter in your
your table should be for an execution of line numbered 6 in the code,
and your comment can be, "return 18".

If the same variable value in one column repeats through several rows,
it is more convenient just leave the later entries blank, rather than
keep copying.  With this convention, the current value of a variable
is the last value recorded in a previous line in the table.

This is the first "Play Computer" exercise with a loop.
Be sure to look back at the earlier play computer examples. The lines
in the loop (and hence their line numbers) repeat multiple times
as rows in the table, as you follow
the loop one time through after another!

The original parameter, which does not change, does not have a
column in the table,
for compactness.  The start of the table is shown below.
As shown in the first comment,
throughout the function call, ``nums`` is ::

    [5, 2, 4, 7]
    
====  ===  ===  =========
Line  sum  num  comment
====  ===  ===  =========
1     \-   \-   set nums to [5, 2, 4, 7]; skip line 2 doc string
3        
====  ===  ===  =========
 
Test sumList Exercise 
~~~~~~~~~~~~~~~~~~~~~

Write a program ``testSumList.py`` which includes a ``main``
function to test the sumList function several times. Include a test
for the extreme case, with an empty list.


Join All Exercise 
~~~~~~~~~~~~~~~~~

\* Complete the following function. This starting code is in
``joinAllStub.py``. Save it to the *new* name ``joinAll.py``. Note
the way an example is given in the documentation string. It
simulates the use of the function in the Shell. This is a common
convention:

.. literalinclude:: ../examples/joinAllStub.py
   :lines: 3-10
 
**First Hint**: [#accum]_  **Second Hint**: [#nothing]_

.. match ]]]

.. index:: playing computer

.. _Playing-Computer:

More Playing Computer
---------------------

Testing code by running it is fine, but looking at the results does
not mean you really understand what is going on, particularly if
there is an error! People who do not understand what is happening
are likely to make random changes to their code in an attempt to
fix errors. This is a *very bad*, increasingly self-defeating
practice, since you are likely to never learn where the real
problem lies, and the same problem is likely to come back to bite
you.

It is important to be able to predict accurately what code will do.
We have illustrated playing computer on a variety of small chunks
of code.

Playing computer can help you find bugs (errors in your code). Some
errors are syntax errors caught by the interpreter in translation.
Some errors are only caught by the interpreter during execution,
like failing to have a value for a variable you use. Other errors
are not caught by the interpreter at all - you just get the wrong
answer. These are called *logical* errors. Earlier logical errors
can also trigger an execution error later. This is when playing
computer is particularly useful.

A common error in trying to write the ``numberList`` function would
be to have the following code
(extracted from ``numberEntriesWRONG.py``):

.. literalinclude:: ../examples/numberEntriesWRONG.py
   :linenos:
   :lines: 1-6
 
You can run this code in  and see that it
produces the wrong answer. If you play computer on the call to
``numberList(['apples', 'pears', 'bananas'])``, you can see the
problem:

====  ========  ======  ===============================
Line  item      number  comment
====  ========  ======  ===============================
1     \-        \-      set items to ['apples', 'pears', 'bananas']
3     'apples'  \-      start with item as first in sequence
4     'apples'  1
5     'apples'  1       1   print: 1 apples
6     'apples'  2       2 = 1+1
3     'pears'   2       on to the next element in sequence
4     'pears'   1
5     'pears'   1       print: 1 pears *OOPS!*
====  ========  ======  ===============================

If you go step by step you should see where the incorrect 1 came
from: the initialization is repeated each time in the loop at line
4, undoing the incrementing of ``number`` in line 6, messing up
your count.

.. warning::
   Always be careful that your *one-time* initialization
   for a loop goes *before* the loop, not in it!

.. index:: playing computer; function returning a value

Functions can also return values. Consider the Python for this
mathematical sequence: define the function m(x) = 5x, let y = 3;
find m(y) + m(2y-1):

.. literalinclude:: ../examples/mathfunc.py
   :linenos:

This code is in example ``mathfunc.py``.
A similar example was considered in :ref:`Returned-Function-Values`,
but now add the idea of playing
computer and recording the sequence in a table. Like when you
simplify a mathematical expression, Python must complete the
innermost parts first. Tracking the changes means following the
function calls carefully and using the values returned. Again a
dash '-' is used in the table to indicate an undefined variable.
Not only are local variables like formal parameters undefined
before they are first used, they are also undefined after the
termination of the function,

====  ==  =  =====================
Line  x   y  Comment
====  ==  =  =====================
1-3          Remember definition of m
4     \-  3  
5     \-  3  start on: print(m(y) + m(2*y-1)); first want m(y), which is m(3)
1     3   3  pass 3 to function m, so x =3
2     3   3  return 5*3 = 15
5     \-  3  substitute result: print(15 + m(2*y-1)), want m(2*y-1), which is m(2*3-1) = m(5)
1     5   3  pass 5 to function m, so x=5
2     5   3  return 5*5 = 25
5     \-  3  substitute result: print(15 + 25), so calculate and print 40
====  ==  =  =====================

Thus far most of the code given has been motivated first, so you
are likely to have an idea what to expect. You may need to read
code written by someone else (or even yourself a while back!) where
you are not sure what is intended. Also you might make a mistake
and accidental write code that does something unintended! If you
really understand how Python works, one line at a time, you should
be able to play computer and follow at least short code sequences
that have not been explained before. It is useful to read another
person's code and try to follow it. The next exercises also
provides code that has not been explained first, or has a mistake.

Play Computer Odd Loop Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\* Work in a word processor (not Idle!),
starting from example :file:`playComputerStub.rtf`, and save the file as
:file:`playComputer.rtf`.  The file has
tables set up for this and the following two exercise. 

Play computer on the following code:

.. literalinclude:: ../examples/playcomploop.py
   :linenos:
      
Reality check: 31 is
printed when line 6 finally executes.
The start of the table for this exercise is shown below.  

====  =  =  =  =======
Line  x  y  n  Comment
====  =  =  =  =======
1     0     
====  =  =  =  =======

Play Computer Error Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\* In a word processor  
add to the file :file:`playComputer.rtf`, started in the previous exercise. 

The following code is supposed to compute the product of
the numbers in a list. For instance ``product([5, 4, 6])`` should
calculate and return 5*4*6=120 in steps, calculating 5,
5*4=20 and 20*6=120.

.. literalinclude:: ../examples/playcomperror.py
   :linenos:

The code for this exercise
appears in the example file :file:`numProductWrong.py`.
      
A major use of playing computer is to see exactly where the
data that you expect gets messed up.  Play computer on a call to
``product([5, 4, 6])`` *until* you see that it makes a mistake.
Then you can stop and fix it:  First copy :file:`numProductWrong.py` to
:file:`numProduct.py`, and fix the new file.

The table
headings and the first row of the table for this exercise are shown below. 

====  ===  ====  =======   
Line  n    prod  Comment
====  ===  ====  =======   
1     \-   \-    Set nums to [5, 4, 6]
2  
====  ===  ====  =======   

Save it as
:file:`numProduct.py` 
and fix the error you found (and save again!).


Play Computer Functions Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\* In a word processor once again 
add to the file :file:`playComputer.rtf`, started in the previous exercises. 

Play computer on the following code: 

.. literalinclude:: ../examples/playcompfunc.py
   :linenos:

Reality check: 70 is printed.

The table
headings  and the first row of the table for this exercise are shown below. 

====  =  =======
Line  x  Comment
====  =  =======
1-2      Remember f definition
3
====  =  =======

Look at the example above with a table showing a function returning a value!

.. index::
   print; end keyword parameter
   end keyword parameter
   keyword parameter; end

.. _print-end:
   
The ``print`` function keyword ``end``
--------------------------------------
   
By default the print function adds a newline to the end of the
string being printed. This can be overridden by including the
keyword parameter ``end``. The keyword end can be set equal to any
string. The most common replacements are the empty string or a
single blank. If you also use the keyword parameter ``sep``, these
keyword parameters may be in either order, but they must come at the
end of the parameter list. Read the illustrations::

    print('all', 'on', 'same', 'line') 
    print('different line') 

is equivalent to

.. code-block:: python3

    print('all', 'on' , end=' ') 
    print('same', end=' ') 
    print('line') 
    print('different line') 

This does not work directly in the shell (where you are always
forced to a new line at the end). It does work in a program, but it
is not very useful except in a loop!

Suppose I want to print a line
with all the elements of a list, separated by spaces, but not on
separate lines. I can use the ``end`` keyword set to a space in the
loop. Can you figure out in your head what this example file
``endSpace1.py`` does? Then try it:

.. literalinclude:: ../examples/endSpace1.py
   :language: python3

If you still want to go on to a new line at the *end* of the loop,
you must include a print function that does advance to the next
line, once, *after* the loop. Try this variation, ``endSpace2.py``

.. literalinclude:: ../examples/endSpace2.py
   :language: python3

.. [#accum]
   This is a form of accumulation, but not quite the same as adding
   numbers.

.. [#nothing]
   "Start with nothing accumulated" does not mean 0, here. Think
   what is appropriate.

