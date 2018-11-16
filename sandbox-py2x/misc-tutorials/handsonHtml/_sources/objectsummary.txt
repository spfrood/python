.. _objectSummary:

Summary
=======

The same typographical conventions will be used as in :ref:`introSummary`.

#. Object notation
   
   #. When the name of a type of object is used as a function call, it
      is called a *constructor*, and a new object of that type is
      constructed and implicitly returned (no return statement).
      The meanings of any parameters to the
      constructor depend on the type. [:ref:`Constructors`]

   #. *object*\ ``.methodName(`` parameters ``)``
   
      Objects have special operations associated with them, called
      methods. They are functions automatically applied to the *object*
      before the dot. Further parameters may be expected, depending on
      the particular method. [:ref:`Object-Orientation`]


#. String (``str``) indexing and methods

   See :ref:`introSummary` for string literals
   and symbolic string operations.
   
   #. String Indexing. [:ref:`String-Indices`]
   
      *stringReference* ``[`` *intExpression* ``]``

      Individual characters in a string may be chosen. If the string has
      length L, then the indices start from 0 for the initial character
      and go to L-1 for the rightmost character. Negative indices may
      also be used to count from the right end, -1 for the rightmost
      character through -L for the leftmost character. Strings are
      immutable, so individual characters may be read, but not set.

   #. String Slices [:ref:`String-Slices`]
   
      | *stringReference* ``[`` *start* ``:`` *pastEnd* ``]``
      | *stringReference* ``[ :`` *pastEnd* ``]``
      | *stringReference* ``[`` *start* ``: ]``
      | *stringReference* ``[ : ]``

      A substring or *slice* of 0 or more consecutive characters of a
      string may be referred to by specifying a starting index and the
      index one *past* the last character of the substring. If the
      starting or ending index is left out Python uses 0 and the length
      of the string respectively. Python assumes indices that would be
      beyond an end of the string actually mean the end of the string.

   #. String Methods: Assume *s* refers to a string
      
      #. *s*\ ``.upper()``
   
         Returns an uppercase version of the string *s*.
         [:ref:`Object-Orientation`]

      #. *s*\ ``.lower()``

         Returns a lowercase version of the string
         *s*. [:ref:`Object-Orientation`]

      #. *s*\ ``.count(`` *sub* ``)``

         Returns the number of repetitions of the substring *sub* inside
         *s*. [:ref:`Object-Orientation`]

      #.
         | *s*\ ``.find(`` *sub* ``)``
         | *s*\ ``.find(`` *sub* ``,`` *start* ``)``
         | *s*\ ``.find(`` *sub* ``,`` *start* ``,`` *end* ``)``

         Returns the index in *s* of the first character of the first
         occurrence of the substring *sub* within the part of the string *s*
         indicated, respectively the whole string *s*,
         *s*\ ``[`` *start* ``: ]``, or
         *s*\ ``[`` *start* ``:`` *end* ``]``, where
         *start* and *end* have integer values. [:ref:`Object-Orientation`]

      #.
         | *s*\ ``.split()``
         | *s*\ ``.split(`` *sep* ``)``

         The first version splits *s* at any sequence of whitespace (blanks,
         newlines, tabs) and returns the remaining parts of *s* as a list.
         If a string *sep* is specified, it is the separator that
         gets removed from between the parts of the list. [:ref:`split`]

      #. *sep*\ ``.join(`` *sequence* ``)``
   
         Return a new string obtained by joining together the
         *sequence* of strings into one string, interleaving the
         string *sep* between *sequence* elements.
         [:ref:`join`]

      #. Further string methods are discussed in the Python Reference
         Manual, Section 2.3.6.1, String Methods.
         [:ref:`Further-Exploration`]

#. Sets

   A ``set`` is a collection of elements with no repetitions. It can
   be used as a sequence in a ``for`` loop. A ``set`` constructor can
   take any other sequence as a parameter, and convert the sequence to
   a ``set`` (with no repetitions). Nonempty ``set`` literals are enclosed
   in braces. [:ref:`Sets`]

#. List method ``append`` 
   
   *aList*\ ``.append(`` *element* ``)``

   Add an arbitrary *element* to the end of the ``list``
   *aList*, *mutating* the list, not returning any list.
   [:ref:`Appending-to-a-list`]

#. Files [:ref:`Files`]

   #.
       | ``open(`` *nameInFileSystem* ``)``
       | ``open(`` *nameInFileSystem* ``, 'r' )``

       returns a file
       object for reading, where *nameInFileSystem* must be a
       string referring to an existing file. 

   #.  ``open(`` *nameInFileSystem* ``, 'w')``

       returns a file object for writing, where the string
       *nameInFileSystem* will be the name of the file. If it did
       not exist before, it is created. If it *did* exist before,
       all previous contents are **erased**. 

   #.  If *infile* is a file opened for reading, and *outfile* is
       a file opened for writing, then

           ..
   
               *infile*\ ``.read()``

           returns the entire file contents of the file as a string.

               *infile*\ ``.close()``

           closes the file in the operating system
           (generally not needed, unless the file is going to be modified
           later, while your program is *still* running).

               *outfile*\ ``.write(`` *stringExpression* ``)``

           writes the string to the file, with no extra newline.

               *outfile*\ ``.close()``

           closes the file in the operating system
           (*important* to make sure the whole file gets written and to allow
           other access to the file).

#. Mutable objects [:ref:`Issues-with-Mutable`]
   Care must be taken whenever a second name is assigned to a mutable
   object. It is an *alias* for the original name, and refers to the
   exact same object. A mutating method applied to either name changes
   the one object referred to by *both* names.
   Many types of mutable object have ways to make a copy that is a
   distinct object. Zelle's graphical objects have the ``clone``
   method. A copy of a list may be made with a full slice:
   *someList*\ ``[:]``. Then direct mutations to one list (like
   appending an element) do not affect the other list, but still, each
   list is indirectly changed if a common mutable element in the lists
   is changed.

#. Graphics
   
   A systematic reference to Zelle's graphics package, graphics.py, is
   at
   http://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html.

   
   #. Introductory examples of using graphics.py are in
      [:ref:`Graphics-Introduction`], [:ref:`Sample-Graphics`], and
      [:ref:`Entry-Objects`]

   #. Windows operating system .pyw

      In windows, a graphical program that take no console input and
      generates no console output, may be given the extension .pyw to
      suppress the generation of a console window. [:ref:`pyw`]

   #. Event-driven programs
   
      Graphical programs are typically event-driven, meaning the next
      operation done by the program can be in response to a large number
      of possible operations, from the keyboard or mouse for instance,
      without the program knowing which kind of event will come next. For
      simplicity, this approach is pretty well hidden under Zelle's
      graphics package, allowing the illusion of simpler sequential
      programming. [:ref:`EventDriven`]

   #. Custom computer colors are expressed in terms of the amounts of
      red, green, and blue. [:ref:`Custom-Colors`]

   #. See also Animation under the summary of Programming
      Techniques.

#. Additional programming techniques
   
   These techniques extend those listed in the summary of the
   previous chapter. [:ref:`introSummary`]

   #. Sophisticated operations with substrings require careful setting
      of variables used as an index. [:ref:`Index-Variables`]

   #. There are a number of techniques to assist creative programming,
      including pseudo-code and gradual generalization from concrete
      examples. [:ref:`Creative-Problem-Solving`]

   #. Animation: a loop involving small moves followed by a short
      delay (assumes the time module is imported): [:ref:`Animation`]

          | loop heading ``:`` 
          |     move all objects a small step in the proper direction 
          |     ``time.sleep(`` *delay* ``)`` 

   #. Example of a practical successive modification loop:
      [:ref:`Ease-madLibCreation`]

   #. Examples of encapsulating ideas in functions and reusing them:
      [:ref:`Ease-madLibCreation`], [:ref:`The-Revised-Mad`],
      [:ref:`Animation`]

   #. Random results can be introduced into a program using the random
      module. [:ref:`Random-Colors`]
