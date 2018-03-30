
.. _Loops-and-Tuples:
   
Loops and Tuples
================

This section will discuss several improvements to the
``chooseButton1.py`` program from the last section that will turn it
into example program ``chooseButton2.py``.

First an introduction to *tuples*, which we will use for the first
time in this section:

.. index:: tuple

A tuple is similar to a list except that a literal tuple is
enclosed in parentheses rather than square brackets, and a tuple is
immutable. In particular you cannot change the length or substitute
elements, unlike a list. Examples are ::

    (1, 2, 3)
    ('yes', 'no')

.. index::
   double:  tuple; multiple assignment

They are another way to make several items into a single object.
You can refer to individual parts with indexing, like with lists,
but a more common way is with multiple assignment. A silly simple
example::

    tup = (1, 2) 
    (x, y) = tup 
    print(x)  # prints 1 
    print(y)  # prints 2 

Now back to improving the chooseButton1.py program, which has
similar code repeating in several places. Imagine how much worse it
would be if there were more colors to choose from and more parts to
color!

First consider the most egregious example::

        if isInside(pt, redButton): 
            color = 'red' 
        elif isInside(pt, yellowButton): 
            color = 'yellow' 
        elif isInside(pt, blueButton): 
            color = 'blue' 
        else : 
            color = 'white' 

.. index::
   for-each; multiple assignment with tuples
   multiple assignment; for with tuples
   tuple; for-each multiple assignment

Not only is this exact ``if`` statement repeated several times, all
the conditions within the ``if`` statement are very similar! Part
of the reason I did not put this all in a function was the large
number of separate variables. On further inspection, the particular
variables ``redButton``, ``yellowButton``, ``blueButton``, all play
a similar role, and their names are not really important, it is
their *associations* that are important: that redButton goes with
'red', .... When there is a sequence of things all treated
similarly, it suggests a list and a loop. An issue here is that the
changing data is *paired*, a rectangle with a color string. There
are a number of ways to handle such associations. A very neat way
in Python to package a pair (or more things together) is a *tuple*,
turning several things into one object, as in (redButtton, 'red').
Objects such are this tuple can be put in a larger list::

    choicePairs = [(redButtton, 'red'), (yellowButton, 'yellow'),
                   (blueButton, 'blue')]

Such tuples may be neatly handled in a ``for`` statement. You can
imagine a function to encapsulate the color choice starting::

    def getChoice(choicePairs, default, win): 
        '''Given a list choicePairs of tuples, with each tuple in the form  
        (rectangle, choice), return the choice that goes with the rectangle  
        in win where the mouse gets clicked, or return default if the click  
        is in none of the rectangles.''' 
     
        point = win.getMouse() 
        for (rectangle, choice) in choicePairs: 
            #.... 

This is the first time we have had a ``for`` loop going through a
list of *tuples*. Recall that we can do multiple assignments at
once with tuples. This also works in a ``for`` loop heading. The
``for`` loop goes through one tuple in the list choicePairs at a
time. The first time through the loop the tuple taken from the list
is (redButtton, 'red'). This ``for`` loop does a multiple
assignment to ``(rectangle, choice)`` each time through the loop, so
the first time ``rectangle`` refers to ``redButton`` and ``choice``
refers to ``'red'``. The next time through the loop, the second
tuple from the list is used, ``(yellowButton, 'yellow')`` so this time
inside the loop ``rectangle`` will refer to ``yellowButton`` and
``choice`` refers to ``'yellow'``....  This is a neat Python
feature. [#]_

.. ]]]]]]]]

.. index::
   single:  loop; return from inside
   single:  return; from inside loop

There is still a problem. We could test each rectangle in the
|for-each| loop, but the original |if-elif| ... statement in
``chooseButton1.py`` stops when the *first* condition is true.
However |for-each|
statements are designed to go all the way *through* the sequence.
There is a simple way out of this in a function: A ``return``
statement always stops the execution of a function. When we have
found the rectangle containing the point, the function can
``return`` the desired choice immediately!   ::

    def getChoice(choicePairs, default, win): 
        '''Given a list of tuples (rectangle, choice), return the choice 
        that goes with the rectangle in win where the mouse gets clicked, 
        or return default if the click is in none of the rectangles.''' 
     
        point = win.getMouse() 
        for (rectangle, choice) in choicePairs: 
            if isInside(point, rectangle): 
                return choice 
        return default 

Note that the ``else`` part in ``chooseButton1.py`` corresponds to the
statement *after* the loop above. If execution gets past the loop,
then none of the conditions tested in the loop was true.

With appropriate parameters, the looping function is a complete
replacement for the original |if-elif| statement! The
replacement has further advantages.

-  There can be an arbitrarily long list of pairs, and the exact
   same code works.

-  This code is clearer and easier to read, since there is no need
   to read through a long sequence of similar |if-elif|
   clauses.

-  The names of the rectangles in the tuples in the list are never
   referred to. They are unnecessary here. Only a list needs to be
   specified. That could be useful earlier in the program ....

Are individual names for the rectangles needed earlier? No, the
program only need to end up with the pairs of the form
``(rectangle, color)`` in a list.
The statements in the original program, below,
have a similar form which will allow them to be rewritten::

        redButton = makeColoredRect(Point(310, 350), 80, 30, 'red', win) 
        yellowButton = makeColoredRect(Point(310, 310), 80, 30, 'yellow', win) 
        blueButton = makeColoredRect(Point(310, 270), 80, 30, 'blue', win) 

As stated earlier, we could use the statements above and then make
a list of pairs with the statement ::

    choicePairs = [(redButtton, 'red'), (yellowButton, 'yellow'),
                   (blueButton, 'blue')]

Now I will look at an alternative that would be particularly useful
if there were considerably more buttons and colors.

All the assignment statements with ``makeColorRect`` have the same
format, but differing data for several parameters. I use that fact
in the alternate code::

        choicePairs = list() 
        buttonSetup = [(310, 350, 'red'), (310, 310, 'yellow'),
                       (310, 270, 'blue')] 
        for (x, y, color) in buttonSetup: 
           button = makeColoredRect(Point(x, y), 80, 30, color, win) 
           choicePairs.append((button, color)) 

I extract the changing data from the creation of the rectangles
into a list, ``buttonSetup``. Since more than one data items are
different for each of the original lines, the list contains a tuple
of data from each of the original lines. Then I loop through this
list and not only create the rectangles for each color, but also
accumulates the (rectangle, color) pairs for the list
``choicePairs``.

Note the double parentheses in the last line of the code. The outer
ones are for the method call. The inner ones create a single tuple
as the parameter.

Assuming I do not need the original individual names of the
Rectangles, this code with the loop will completely substitute for
the previous code with its separate lines with the separate named
variables and the recurring formats.

This code has advantages similar to those listed above for the
``getChoice`` code.

Now look at what this new code means for the interactive part of
the program. The interactive code directly reduces to ::

        msg = Text(Point(win.getWidth()/2, 375),'Click to choose a house color.') 
        msg.draw(win) 
        color = getChoice(colorPairs, 'white', win) 
        house.setFill(color) 
         
        msg.setText('Click to choose a door color.') 
        color = getChoice(colorPairs, 'white', win) 
        door.setFill(color) 

In the original version with the long |if-elif| statements,
the interactive portion only included portions for the user to set
the color of two shapes in the picture (or you would have been
reading code forever). Looking now at the similarity of the code
for the two parts, we can imagine another loop, that would easily
allow for many more parts to be colored interactively.

There are still several differences to resolve. First the message
``msg`` is *created* the first time, and only the text is *set* the
next time. That is easy to make consistent by splitting the first
part into an initialization and a separate call to ``setText`` like
in the second part::

        msg = Text(Point(win.getWidth()/2, 375),'') 
        msg.draw(win) 
     
        msg.setText('Click to choose a house color.')


Then look to see the differences between the code for the two
choices. The ``shape`` object to be colored and the name used to
describe the shape change: two changes in each part. Again tuples
can store the changes of the form (shape, description). This is
another place appropriate for a loop driven by tuples.. The (shape,
description) tuples should be explicitly written into a list that
can be called ``shapePairs``. We could easily extend the list
shapePairs to allow more graphics objects to be colored. In the
code below, the roof is added.

The new interactive code can start with::

    shapePairs = [(house, 'house'), (door, 'door'), (roof, 'roof')]  
    msg = Text(Point(win.getWidth()/2, 375),'') 
    msg.draw(win) 
    for (shape, description) in shapePairs: 
        prompt = 'Click to choose a ' + description + ' color.' 
        # .... 

Can you finish the body of the loop? Look at the original version
of the interactive code. When you are done thinking about it, go on
to my solution. The entire code is in example program
``chooseButton2.py``, and also below. The changes from
chooseButton1.py are in three blocks, each labeled #NEW in the
code. The new parts are the ``getChoice`` function and the two new
sections of ``main`` with the loops:

.. literalinclude:: ../examples/chooseButton2.py

Run it.

With the limited number of choices in ``chooseButton1.py``, the change
in length to convert to ``chooseButton2.py`` is not significant, but
the change in organization is significant if you try to extend the
program, as in the exercise below. See if you agree!

Exercises
---------

Choose Button Exercise
~~~~~~~~~~~~~~~~~~~~~~
   
a.  Write a program ``chooseButton3.py``, modifying
    ``chooseButton2.py``. Look at the format of the list
    ``buttonSetup``, and extend it so there is a larger choice of
    buttons and colors. Add at least one button and color.

b.  Further extend the program ``chooseButton3.py`` by adding some
    further graphical object shape to the picture, and extend the list
    ``shapePairs``, so they can all be interactively colored.

c.  (Optional) If you would like to carry this further, also add a
    prompt to change the outline color of each shape, and then carry
    out the changes the user desires.

d.  (Optional Challenge) ** Look at the pattern within the list
    ``buttonSetup``. It has a consistent x coordinate, and there is a
    regular pattern to the change in the y coordinate (a consistent
    decrease each time). The only data that is arbitrary each time is
    the sequence of colors. Write a further version
    ``chooseButton4.py`` with a function ``makeButtonSetup``, that takes a
    list of color names as a parameter and uses a loop to create the
    list used as ``buttonSetup``. End by returning this list. Use the
    function to initialize ``buttonSetup``. If you like, make the
    function more general and include parameters for the x coordinate,
    the starting y coordinate and the regular y coordinate change.

.. [#]
   Particularly in other object-oriented languages where lists and
   tuples are way less easy to use, the preferred way to group
   associated objects, like rectangle and choice, is to make a custom
   object type containing them all. This is also possible and often
   useful in Python. In some relatively simple cases, like in the
   current example, use of tuples can be easier to follow, though the
   approach taken is a matter of taste. The topic of creating custom
   type of objects will not be taken up in this tutorial.

