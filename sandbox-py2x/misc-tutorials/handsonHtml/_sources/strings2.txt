
.. _Strings-Part-II:
   
Strings Part II
===============

.. index:: 
   single: '''
   single: """
   string; triple quote
   triple quoted string

.. _Triple-Quoted-String:
   
Triple Quoted String Literals
-----------------------------
   
Strings delimited by one quote character, like ``'``,
are required to lie within
a single Python line. It is sometimes convenient to have a
multi-line string, which can be delimited with triple quotes,
``'''``. Try
typing the following. You will get continuation lines until the
closing triple quotes. Try in the *Shell*::

    sillyTest = '''Say,  
    "I'm in!" 
    This is line 3''' 
    print(sillyTest) 

The line structure is preserved in a multi-line string. As you can
see, this also allows you to embed both single and double quote
characters!

.. index::
   string; escape codes \\ \n
   escape codes \\ \n 
   newline; \n
   single: \n newline
   single: \; escape code

.. _Escape-Codes:

Escape Codes
------------

Continuing in the *Shell* with ``sillyTest``, enter just ::

    sillyTest

The answer looks strange! It indicates an alternate way to encode
the string internally in Python using *escape codes*. Escape codes
are embedded inside string literals and start with a backslash
character ``\``. They are used to embed characters
that are either unprintable or have a special syntactic meaning to
Python that you want to suppress. In this example you see the most
common ones:

+-------------+----------------------+
| Escape code | Meaning              |
+=============+======================+
| ``\\``      | ``\`` (backslash)    |
+-------------+----------------------+
| ``\n``      | newline              |
+-------------+----------------------+
| ``\'``      | ``'`` (single quote) |
+-------------+----------------------+

The newline character indicates further text will appear on a new
line when *printed*. When you use a print function, you get the
actual printed meaning of the escape coded character.

Predict the result, and try in the *Shell*::

    print('a\nb\n\nc')

Did you guess the right number of lines splitting in the right
places?
