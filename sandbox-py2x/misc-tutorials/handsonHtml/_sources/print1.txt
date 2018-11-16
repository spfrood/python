
.. index:: print

.. _Print-Statements-I:
   
Print Function, Part I
======================
   
In interactive use of the Python interpreter, you can type an
expression and immediately see the result of its evaluation. This
is fine to test out syntax and maybe do simple calculator
calculations. In a program run from a file like the first sample
program, Python does not display expressions this way. If you want
your program to display something, you can give explicit
instructions with the print function. Try in the *Shell*::

    x = 3 
    y = 5 
    print('The sum of', x, 'plus', y, 'is', x+y)  

The print function will prints as strings everything in a
comma-separated sequence of expressions, and it will separate the
results with single blanks by default. Note that you can mix types:
anything that is not already a string is automatically converted to
its string representation.

.. index::  newline; print

You can also use it with no parameters::

    print()

to just advance to the next line.

