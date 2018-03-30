.. index:: file

.. _Files:
   
Files
=====

This section fits here logically (as an important built-in type of
object) but it is not needed for the next chapter, :ref:`More-On-Flow`.

Thus far you have been able to save programs, but anything produced
during the execution of a program has been lost when the program
ends. Data has not *persisted* past the end of execution. Just as
programs live on in files, you can generate and read data files in
Python that persist after your program has finished running.

As far as Python is concerned, a file is just a string (often very
large!) stored on your file system, that you can read or write,
gradually or all together.

.. index::
   file; write
   write a file

Writing Files
-------------
   
*Open a directory window for your Python program directory.*
First note that there is no file named sample.txt. 

*Make sure* you have started Idle so the current directory is your
Python program directory (for instance
*in Windows with the downloaded shortcut to Idle*).

Run the example program ``firstFile.py``, shown below:

.. literalinclude:: ../examples/firstFile.py

The first line creates a file object, which links Python to your
computer's file system. The first parameter in the file constructor
gives the file name, ``sample.txt``. The second parameter indicates
how you use the file. The ``'w'`` is short for **w**\ rite, so you will
be creating and *writing* to a file.

..  warning::
    If the file already existed,  the old contents are
    *destroyed*.

If you do not use
any operating system directory separators in the name (``'\'`` or ``'/'``
depending on your operating system), then the file will lie in the
current directory. The assignment statement gives the Python file
object the name ``outFile``.

The second line writes the specified string to the file.

The last line is important to clean up. Until this line, this
Python program controls the file, and nothing may be actually
written to the file yet:  Since initiating a file operation
is thousands of times
slower than memory operations, Python *buffers* data, saving small
amounts and writing a larger chunk all at once.

..  warning::
    The ``close``
    line is essential for Python to make sure everything is really
    written, and to relinquish control of the file.

It is a common bug
to write a program where you have the code to add all the data you
want to a file, but the program does not end up creating a file.
Usually this means you forgot to close the file.

Now switch focus and look at a file window for the current
directory. You should now see a file ``sample.txt``. You can open
it in Idle (or your favorite word processor) and see its contents.

Run the example program ``nextFile.py``, shown below, which has two
calls to the write method:

.. literalinclude:: ../examples/nextFile.py

Now look at the file, ``sample2.txt``. Open it in Idle. It may not
be what you expect! The write method for the file is not quite like
a ``print`` function. It does not add anything to the file except
*exactly* the data you tell it to write. If you want a newline, you
must indicate it *explicitly*. Recall the newline code
``'\n'``. Run the example program ``revisedFile.py``,
shown below, which adds newline codes:

.. literalinclude:: ../examples/revisedFile.py

Check the contents of sample3.txt.

.. index::
   file; read
   read a file

Reading Files
-------------
   
Run the example program
``printFile.py``, shown below:

.. literalinclude:: ../examples/printFile.py

Now you have come full circle: what one Python program has written
into the file ``sample3.txt``, another has read and displayed.

In the first line an operating system file (``sample3.txt``) is
associated again with a Python variable name (``inFile``). The
second parameter again gives the mode of operation, but this time
it is ``'r',`` short for **r**\ ead. This file, ``sample3.txt``, should
already exist, and the intention is to read from it. This is the
most common mode for a file, so the ``'r'`` parameter is actually
*optional*.

The ``read`` method returns all the file's data as a single string,
here assigned to ``contents``. Using the ``close`` method is
generally optional with files being read. There is nothing to lose
if a program ends without closing a file that was being read. [#]_

..  note::
    There are three related but distinct concepts related to files.
    Beginners often try to merge several in their head or substitute 
    one for another:
    
    #.  The *file name*  is a string that identifies the file in your
        computer's file system.
    #.  You need the file name to ``open`` a file creating a *file* object,
        but the file object (that I tend to call ``inFile`` or ``outFile``)
        is not the same as the name of the file on your hard drive.
    #.  There is still one more step to the most important part, the *contents*
        of the file.  The ``read`` and ``write`` methods for a file object read 
        existing content or write new content.   

PrintUpper Exercise
~~~~~~~~~~~~~~~~~~~

Make the following programs in sequence. Be sure to save the
programs in the same directory as where you start the idle shortcut
and where you have all the sample text files:

a.  printUpper.py: read the contents of the sample2.txt file
    and print the contents out in upper case. (This should use file
    operations and should work no matter what the contents are in
    sample2.txt. Do not assume the particular string written by
    ``nextFile.py``!)

b.  fileUpper.py: prompt the user for a file name, read and
    print the contents of the requested file in upper case.

c.  \* copyFileUpper.py: modify fileUpper.py to write the upper
    case contents string to a new file rather than printing it. 
    Have the name of
    the new file be dynamically derived from the old name by prepending
    'UPPER' to the name. For example, if the user specified the file
    ``sample.txt`` (from above), the program would create a file
    ``UPPERsample.txt``, containing 'MY FIRST OUTPUT FILE!'. When the
    user specifies the file name ``stuff.txt``, the resulting file
    would be named ``UPPERstuff.txt``.

.. _Write-madlib3.py:

Mad Lib File Exercise
~~~~~~~~~~~~~~~~~~~~~

Write ``madlib3.py``, a small modification
of ``madlib2.py``, requiring only a modification to the ``main``
function of ``madlib2.py``.  (Even better is to start from
``madlib2a.py`` if you did the exercise in :ref:`unique-list-ex`).
Also create a file :file:`myMadlib.py`, as described below.

Your ``madlib3.py`` should

* prompt the user for the name of a file that should contain a madlib format
  string as text (with no quotes around it).
* Read in this file and use it as the format string in the ``tellStory``
  function.

This is unlike in :file:`madlib2.py`, where the story is a literal string coded
directly into the program called ``originalStory``. The ``tellstory``
function and particularly the ``getKeys`` function were developed
and described in detail in this tutorial, but for this exercise
there is no need to follow their inner workings - you are just a
*user* of the ``tellstory`` function (and the functions that it
calls). You do not need to mess with the code for the definition of
``tellStory`` or any of the earlier supporting functions. The
original madlib string is already placed in a file :file:`jungle.txt`
as an example of the story file format expected. With the Idle editor, write
another madlib format string into a file :file:`myMadlib.txt`. If you
earlier created a file :file:`myMadlib.py`, then you can easily extract
the story from there (without the quotes around it). Test your
program both with :file:`myMadlib.py`, and your new madlib story file.

.. [#]
   If, for some reason, you want to reread this same file while the
   same program is running, you need to close it and reopen it.

