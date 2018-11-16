.. index::  mad lib
                           
Mad Libs Revisited
==================

.. _Ease-madLibCreation:
     
A Function to Ease the Creation of Mad Libs
-------------------------------------------

The versions so far of the Mad Lib program have been fairly easy to
edit to contain a different mad lib:

#. Come up with a new mad lib story as a format string

#. Produce the list of cues to prompt the user with.

The first is a creative process. The second is a pretty mechanical
process of looking at the story string and copying out the embedded
cues. The first is best left to humans. The second can be turned
over to a Python function to do automatically, as many times as we
like, with any story - if we write the code once.

Writing the Python code also takes a different sort of creativity!
We shall illustrate a creative process. This is a bigger problem
than any we have taken on so far. It is hard to illustrate a
creative process if the overall problem is too simple.

Try and follow along. *Read* the sample code and pseudocode.

*There is nothing to try in the Shell or editor until further notice.*

If we follow the last version of the mad lib program, we had a loop
iterating through the keys in the story, and making a dictionary
entry for each key. The main idea we follow here is to use the
format string to automatically generate the sequence of keys. Let
us plan this unified task as a new function::

    def getKeys(formatString): 
        '''formatString is a format string with embedded dictionary keys. 
        Return a list containing all the keys from the format string.''' 
        # more to come 

The keys we want are embedded like ``{animal}``. There may be any
number of them in the format string. This indeterminacy suggests a
loop to extract them. At this point we have only considered
``for`` loops. There is no obvious useful sequence to iterate
through in the loop.  (We are trying to *create* such a sequence!)
The only pattern we have discussed that does not actively process
each element of a significant list is a repeat-loop, where we just
use the loop to repeat the correct number of times. This will work
in this case.  (There is a more efficient approach after we introduce
:ref:`While-Statements`, suggested in :ref:`mad-lib-while-exercise`.)

First: how many times do we want to pull out a key - once for each
embedded format. So how do we count those?

The ``count`` method is obviously a way to count. However we must
count a fixed string, and the whole embedded formats vary, with
different keys in the middle. A common part is '{', and this
should not appear in the regular text of the story, so it will
serve our purpose::

    repetitions = formatString.count('{') 
    for i in range(repetitions): 
        ... 

This is certainly the most challenging code to date. Before jumping
into writing it all precisely, we can give an overall plan in
pseudo-code. For a plan we need an idea of what quantities we are
keeping track of, and name them, and outline the sequence of
operations with them.

Think about data to name:

In this case we are trying to find a list. We will need to extract
one element at a time and add it to the list, so we need a list,
say ``keyList``.

The central task is to identifying the individual keys. When we
find a key we can call it ``key``.

Think about identifying the text of individual keys. This may be
too hard to think of in the abstract, so let us use as a concrete
example, and let us keep it simple for the moment. Suppose the data
in ``formatString`` starts off as follows. The lines with numbers
are added to help us refer to the indices. *Display* of possible
data::

    #           1111111111222222222233333333 
    # 01234567890123456789012345678901234567 
     'blah {animal} blah blah {food} ...'    # start of formatString

The first key is ``'animal'`` at ``formatString[6:12]``. The next
key is ``'food'`` at ``formatString[25:29]``. To identify each
key as part of ``formatString`` we need not only the variable
``formatString``, but also index variables to locate the start and
end of the slices. Obvious names for the indices are ``start`` and
``end``. We want to keep them current so the next key slice will
always be  ::

    key = formatString[start : end]

Let us now put this all in an overall plan. We will have to
continuously modify the start and end indices, the key, and the
list. We have a basic pattern for accumulating a list, involving
initializing it and appending to it. We can organize a plan, partly
fleshed out, with a couple of approximations still to be worked out.
The parts that are not yet in Python are *emphasized*:

    | ``def getKeys(formatString):`` 
    |    ``keyList = list()`` 
    |    *?? other initializations ??* 
    |    ``repetitions = formatString.count('{')`` 
    |    ``for i in range(repetitions):`` 
    |        *find the start and end of the next key* 
    |        ``key = formatString[start : end]`` 
    |        ``keyList.append(key)``  
    |    ``return keyList`` 

We can see that the main piece left is to find the start and end
indices for each key. The important word is *find*: the method we
consider is ``find``. As with the plan for using ``count`` above,
the beginnings of keys are identified by the specific string ``'{'``.
We can look first at ::

    formatString.find('{')

but that is not the full solution. If we look at our concrete
example, the value returned is 5, not 6. How in general would we
locate the beginning of the slice we want?

We do not want the position of the '{', but the
position just *after* the '{'. Since the length of
'{' is 1, the correct position is 5+1 = 6. We can generalize
this to ::

    start = formatString.find('{') + 1

OK, what about ``end``? Clearly it is at the ``'}'``. In
this example, ::

    formatString.find('}')

gives us 12, exactly the right place for the end of the slice (one
place past the actual end).

There is a subtle issue here that will be even more important
later: We will keep wanting to find the *next* brace, and not keep
finding the *first* brace. How do we fix that?

Recall there was an alternate syntax for ``find``, specifying the
first place to search! That is what we need. Where should we start?
Well, the end must come after the start of the key, our variable
``start``::

    start = formatString.find('{') + 1 
    end = formatString.find('}', start) 

Figuring out how to find the first key is important, but we are not
home free yet. We need to come up with code that works in a loop
for the *later* keys. This code will not work for the next one.
Why?

As written, the search for '{' will again start from the beginning of the
format string, and will find the first key again. So what code will
work for the *second* search? We search for the start of the next
key going from the end of the last one::

    start = formatString.find('{', end) + 1 
    end = formatString.find('}', start) 

This code will also work for later times through the loop: each
time uses the ``end`` from the previous time through the loop.

So now what do we do for finding the first key? We could separate
the treatment of the first key from all the others, but an easier
approach would be to see if we can use the same code that already
works for the later repetitions, and initialize variables right to
make it work. If we are to find the *first* key with ::

    start = formatString.find('{', end) + 1

then what do we need? Clearly ``end`` needs to have a value. (There
will not be a *previous* loop to give it a value.) What value
should we initialize it to? The first search starts from the
beginning of the string at index 0.  The initialization goes
before the loop, so the full code for this function is ::

    def getKeys(formatString): 
        '''formatString is a format string with embedded dictionary keys. 
        Return a list containing all the keys from the format string.''' 
     
        keyList = list() 
        end = 0 
        repetitions = formatString.count('{') 
        for i in range(repetitions): 
            start = formatString.find('{', end) + 1 
            end = formatString.find('}', start) 
            key = formatString[start : end] 
            keyList.append(key) 
     
        return keyList 


Look the code over and see that it makes sense. See how we
continuously modify ``start``, ``end``, ``key``, and ``keyList``.
Since we have coded this new part as a function, it is easy to test
without running a whole revised mad lib program. We can just run
this function on some test data, like the original story, and see
what it does. Run the example program ``testGetKeys.py``:

.. literalinclude:: ../examples/testGetKeys.py

The functions should behave as advertised.

Look back on the process described to come up with the ``getKeys``
function. One way of approaching the creative process of coding
this function was provided. There are many other results and
approaches possible, but the discussion did illustrate a number of
useful ideas which you might adapt to other problems, in different
orders and proportions, that are summarized in the next section.

.. index:: problem solving
                           
.. _Creative-Problem-Solving:
                                         
Creative Problem Solving Steps
------------------------------

-  Clearly define the problem. Encapsulating the problem in a
   function is useful, with inputs as parameters and results returned.
   Include a complete documentation string, and a clear example (or
   examples) of what it is to do.

-  If the problem is too complicated to just solve easily, straight
   away, it is often useful to construct a representative *concrete*
   case and write down *concrete* steps appropriate to this problem.

-  Think of the data in the problem, and give names to the pieces
   you will need to refer to. Clearly identify the ideas that the
   names correspond to. When using sequences like lists or strings,
   you generally need names not only for the whole collection, but
   also parts like items and characters or substrings, and often
   indices that locate parts of the collection.

-  Plan the overall approach to the problem using a mixture of
   Python and suggestive phrases (called pseudo-code). The idea is to
   refine it to a place where you can fairly easily figure how to
   replace the phrases with Python.

-  Replace your pseudo-code parts with Python. If you had a
   concrete example to guide you, you may want to test with one of more further
   concrete examples with different specific data, to make sure you
   come up with code for a generalization that works in all cases.
   This is the process of *abstraction*.

-  Recognize where something is being repeated over and over, and
   think how to structure appropriate loops. Can you incorporate any
   patterns you have seen before?

-  If you need to create a successive modification loop, think of
   how to approach the first repetition and then how to modify the
   data for the later times through the loop. Usually you can make the
   first time through the loop fit the more general pattern needed for
   the repetitions by making appropriate initializations before the
   loop.

-  Check and test your code, and correct as necessary.

.. _The-Revised-Mad:
   
The Revised Mad Lib Program
---------------------------

There is still an issue for use of ``getKeys`` in the mad lib
program: the returned list has unwanted repetitions in it. 
We can easily create a collection without repetitions, how?

One approach is to make a ``set`` from the list returned. A neater
approach would be to just have the getKeys function return a
``set`` in the first place. We need to slightly change to
``getKeys``' documentation string and the final ``return`` line.
This will be included in a new version of the mad lib program,
which makes it easy to substitute a new story. We will make the
story's format string be a parameter to the central method,
``tellStory``. We will also put the clearly identified step of
filling the dictionary with the user's picks in a separate
function. We will test ``tellStory`` with the original story. Note
the changes included in ``madlib2.py`` and run:

.. literalinclude:: ../examples/madlib2.py

Does the use of well-named functions make it easier to follow this
code?  We have broken the large overall problem into many smaller steps.
Make sure you follow the flow of execution and data and see how all
the pieces fit together.

..
   ]]

After Python file manipulation is introduced, in
:ref:`Write-madlib3.py`, you can modify the program to work
on a madlib format string chosen by the user and taken from a
file.

Substring Locations Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\* Rename the example file ``locationsStub.py`` to be
``locations.py``, and complete the function ``printLocations``, to print
the index of *each* location in the string ``s`` where ``target``
is located. For example, ::

    printLocations('This is a dish', 'is')
    
would go through the string ``'This is a dish'`` looking for the
index of places where ``'is'`` appears, and would print::
   
   2
   5
   11
   
Similarly ::
    
    printLocations('This is a dish', 'h')

would print::

   1
   13
   
The program stub already uses the string method
``count``. You will need to add code using the more general form of
``find``.
