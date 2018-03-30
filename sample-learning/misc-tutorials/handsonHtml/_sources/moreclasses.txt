More Classes and Methods
========================

The classes and methods introduced here are all used in the
revised mad lib program developed in the next section.

.. index::
   list; append
   append method for list
                           
.. _Appending-to-a-list:
                           
Appending to a List
-------------------

Before making a version of the madlib program that is much easier
to use with new stories, we need a couple of facts about other
types of objects that are built into Python.

So far we have used lists, but we have not changed the contents of
lists. The most obvious way to change a list is to add a new
element onto the end. Lists have the method ``append``. It
*modifies* the original list. Another word for modifiable is
mutable. Lists are *mutable*. Most of the types of object
considered so far (int, str, float) are *immutable* or *not*
mutable. *Read* and see how the ``list`` named ``words`` changes::

    >>> words = list() 
    >>> words 
    [] 
    >>> words.append('animal') 
    >>> words 
    ['animal'] 
    >>> words.append('food') 
    >>> words 
    ['animal', 'food'] 
    >>> words.append('city') 
    >>> words 
    ['animal', 'food', 'city'] 


This is particularly useful in a loop, where we can accumulate a
new list. *Read* the start of this simple example::

    def multiplyAll(numList, multiplier): 
        '''Return a new list containing all of the elements of numList,  
        each multiplied by multiplier.  For example: 
         
        >>> print(multiplyAll([3, 1, 7], 5)) 
        [15, 5, 35]

        ''' 
        # more to come 


Clearly this will be repetitious. We will process each element of
the list numList. A for-each loop with numList is appropriate. Also
we need to create more and more elements of the new list. The
accumulation pattern will work here, with a couple of wrinkles.

*Test yourself*: If we are going to accumulate a list. How do we
initialize the list?

In earlier versions of the accumulation loop, we needed an
assignment statement to change the object doing the accumulating,
but now the method ``append`` modifies its list automatically, so
we do not need an assignment statement. Read and try the example
program ``multiply1.py``::

    def multiplyAll(numList, multiplier):    #1 
        '''Return a new list containing all 
        of the elements of numList, each 
        multiplied by multiplier.  For example: 
         
        >>> print(multiplyAll([3, 1, 7], 5)) 
        [15, 5, 35] 
        ''' 
     
        newList = list()                     #2 
        for num in numList:                  #3 
            newList.append(num*multiplier)   #4 
        return newList                       #5 
       
    print(multiplyAll([3, 1, 7], 5))         #6 


Make sure the result makes sense to you or follow the details of
playing computer below.

..
   ]]]]]]]]]]]]]]]]]]]]]]]]]]]

====  =========  ==========  ===========  ===  =======================
Line  numList    multiplier  newList      num  comment
====  =========  ==========  ===========  ===  =======================
1-5   \-         \-          \-           \-   definition
6     \-         \-          \-           \-   call function
1     [3, 1, 7]  5           \-           \-   set formal parameters
2     [3, 1, 7]  5           []
3     [3, 1, 7]  5           []           3    first in list
4     [3, 1, 7]  5           [15]         3    append 3*5 = 15
3     [3, 1, 7]  5           [15]         1    next in list
4     [3, 1, 7]  5           [15, 5]      1    append 1*5 = 5
3     [3, 1, 7]  5           [15, 5]      7    last in list
4     [3, 1, 7]  5           [15, 5, 35]  7    append 7*5 = 35
3     [3, 1, 7]  5           [15, 5, 35]  7    done with list and loop
5     [3, 1, 7]  5           [15, 5, 35]  7    return [15, 5, 35]
6     \-         \-          \-           \-   print [15, 3, 35]
====  =========  ==========  ===========  ===  =======================

Using a for-loop and ``append`` is a powerful and flexible way to
derive a new list, but not the only way.

..
   [#]_

.. index:: set
   sequence; set
   single: {}; set
   braces; set
                           
.. _Sets:
   
Sets
----
   
A list may contain duplicates, as in ``[2, 1, 3, 2, 5, 5, 2]``.
This is sometimes useful, and sometimes not. You may have learned
in math class that a *set* is a collection that does not allow
repetitions (a set automatically removes repetitions suggested).
Python has a type ``set``. Like many type names, it can be used to
convert other types. In this case it makes sense to convert any
collection, and the process removes duplicates. *Read* and see what
happens::

    >>> strList = ['z', 'zz', 'c', 'z', 'bb', 'z', 'a', 'c']
    >>> aSet = set(strList)
    >>> aSet
    {'bb', 'zz', 'a', 'c', 'z'}

(Technically, a set is unordered, so your version of Idle may list the set 
in a different order.)
Set literals are enclosed in braces. Like other collections, a set
can be used as a sequence in a ``for`` loop. *Read*, and check it
makes sense::

    >>> for s in aSet:
        print(s)

    
    bb
    zz
    a
    c
    z
     
Predict the result of the following, and then paste it into the
*Shell* and test. (You may not
guess Python's order, but see if you can get the right length and
the right elements in *some* order.)  ::

    set(['animal', 'food', 'animal', 'food', 'food', 'city'])

.. index:: constructor

.. _Constructors:
   
Constructors
------------
   
We have now seen several examples of the name of a type being used
as a function. *Read* these earlier examples::

    x = int('123')
    s = str(123)
    nums = list()
    aSet = set(numberList)

In all such cases a new object of the specified type is constructed
and returned, and such functions are called *constructors*.

..
   .. index::
      single:list; comprehension

..
    .. [#]
       There is also a concise syntax called *list comprehension* that
       allows you to derive a new list from a given sequence.  In the
       example above, we could describe what happens in English as
       "make newList contain twice each number in numList". This is
       quite directly translated into an assignment with a list
       comprehension::

           newList = [2*num for num in numList] 

       This is a lot like mathematical set definition notation, except
       without Greek symbols. List comprehensions also have fancier
       options, but they are not covered in this tutorial.   
