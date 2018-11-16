
.. _IntroSummary:
   
Summary
=======
   
Section references in square brackets indicate where an idea was first
discussed.

Where Python syntax is illustrated, the typeface continues to indicate the
category of each part:

===================  ===========================================
Typeface             Meaning
===================  ===========================================
``Typewriter font``  Text to be written *verbatim*
*Emphasized*         A place where you can use an arbitrary
                     expression. 
**Bold**             A place where you can use an arbitrary
                     identifier. 
Normal text          A description of what goes in that position,
                     without giving explicit syntax
===================  ===========================================

If there are several variations on a particular part of the syntax,
alternatives will be show on successive lines.

To emphasize the successive parts of the syntax, space will
generally be left around symbol and punctuation characters, but the
space is not required in actual use.


A. Python Shell
  
   #. A Shell window may be opened in Idle
      :menuselection:`Run --> Python Shell` [:ref:`Windows-in-Idle`]

   #. Entering commands:
      
      a. Commands may be entered at the
         ``>>>`` prompt.
         [:ref:`Addition-and-Subtraction`]

      b. If the Shell detects that a command is not finished at the end
         of the line, a continuation line is shown with no
         ``>>>``.
         [:ref:`multiplication-parentheses`]

      #. Statements with a heading ending in a colon followed by an
         indented block, must be terminated with an empty line.
         [:ref:`Basic-for-Loops`]

      #. The Shell evaluates a completed command immediately, displaying
         any result other than ``None``, starting on the next line.
         [:ref:`Addition-and-Subtraction`]

      #. The Shell remembers variable and function names.
         [:ref:`Variables-and-Assignment`]

   #. An earlier Shell line may to copied and edited by clicking
      anywhere in the previously displayed line and then pressing
      :kbd:`Enter`.

B. Idle editing
   
   #. Start a new window from the File menu by selecting New, Open...,
      or Recent Files. [:ref:`Loading-a-Program`]

   #. Make your Python file names explicitly end with '.py'
      [:ref:`Literals-and-Identifiers`]

#. To run a program from an Idle Editor Window:
   
   #. Select :menuselection:`Run -> Run Module` or press function key :kbd:`F5`.
      The program
      runs in the Shell window, after resetting the shell so all old
      names are forgotten. [:ref:`Loading-a-Program`]
      
      a. If the program is expecting keyboard input, the text cursor
         should appear at the end of the Shell history. If you somehow move
         the cursor elsewhere, you must explicitly move it back.
         [:ref:`The-Idle-Editor`]

      #. BUG WORKAROUND: If you were running a program that was expecting
         keyboard input when you terminated it to start the latest run, you
         will need to start by pressing the Enter key once or maybe twice to
         clear the old pending wait for input. [:ref:`A-Bug-Possible`]

      #. Press :kbd:`Ctrl-C` to stop a running program in a long or infinite
         loop.

      #. After a program terminates, the Shell remembers function
         definitions and variable names define outside of any function.
         [:ref:`A-First-Function`]

#. Errors come in three categories:
 
   #. Syntax errors: text that the interpreter recognizes as illegal
      when first reading it. This prevents execution of your code. Python
      lets you know where it *realized* there was an error. Sometimes
      this is the exact location, but the actual error could be anywhere
      earlier, often on the previous line.
      [:ref:`Variables-and-Assignment`]

   #. Execution errors: The first illegal action is detected while
      running your command or program. The source of the error could be
      in the line where execution fails, or it could be an earlier
      logical error that only later forces an execution error.
      [:ref:`Variables-and-Assignment`]

      *  Execution errors generate a traceback.
         [:ref:`Function-Parameters`]

   #. Logical errors: When Python detects nothing illegal, but you do
      not get the results you desire. These errors are the hardest to
      trace down. Playing computer and additional print functions help.
      [:ref:`Playing-Computer`]

#. Type ``int``, (short for integer):
   
   #. Literal integer values may not contain a decimal point.
      [:ref:`Floats-Division-Mixed`]

   #. Integers may be arbitrarily large and are stored exactly.
      [:ref:`Floats-Division-Mixed`]

   #. Integers have normal operations, with usual precedence (highest
      listed first):

      
      a. ``**``: exponentiation (5**3 means 5*5*5)
         [:ref:`Exponentiation`]

      #. ``*``, ``/``, ``//``, ``%``: multiplication, division with float
         result, integer division (ignoring any remainder), just the
         remainder from division [:ref:`Division-and-Remainders`]

      #. ``+``, ``-``: addition, subtraction
         [:ref:`Addition-and-Subtraction`]

#. Type ``float``, (short for floating point): approximations of
   real numbers
   
   #. Literal values must contain a decimal point to distinguish them
      from the int type [:ref:`Floats-Division-Mixed`]

   #. Approximates a wide range of values
      [:ref:`Floats-Division-Mixed`]

   #. Does not dependably store numbers exactly - even numbers with
      simple decimal representation [:ref:`Floats-Division-Mixed`]

   #. Has the same operation symbols as for integers, but always
      with a ``float`` result
      [:ref:`Floats-Division-Mixed`]

   #. A mixed binary operation with an integer and a ``float``
      produces a ``float`` result. [:ref:`Floats-Division-Mixed`]

#. Type ``str``, (short for string):
   Literal values contain a sequence of characters enclosed in
   matching quotes.
   
   #. Enclosed in ``'`` or ``"``: The string must be on
      one line. [:ref:`String-Delimiters-I`]

   #. Enclosed in ``'''`` or
      ``"""``: The string may
      include multiple lines in the source file.
      [:ref:`Triple-Quoted-String`]

   #. Escape codes inside literals include ``\'`` for a
      single quote and ``\n`` for a newline.
      [:ref:`Escape-Codes`]

   #. Binary operations (operation symbols have the same precedence
      order as when the symbols are used in arithmetic)
      [:ref:`String-Concatenation`]
      
      a. *stringExpression1* ``+`` *stringExpression2*

         concatenation (running together) of the two strings
         
      #.
         | *stringExpression* ``*`` *integerExpression*
         | *integerExpression* ``*`` *stringExpression*

         Repeat the string the number of times given by the integer
         expression. 

   #. string format method:
      
      a.
         | *stringFormatExpression* ``.format(``
           *parameter0* ``,`` *parameter1* ``,`` *parameter2* ``,`` ... ``)``

         [:ref:`Format-Strings`]
         where *stringFormatExpression* is any string with an arbitrary number
         of places for format substitutions in it. Formatted substitutions are
         enclosed in braces. A digit inside the braces will indicate which
         parameter value is substituted, counting from 0. If digits are left
         out, the format parameters are substituted in order. The expression
         inside the braces can end with a colon ``:`` followed by a format
         specifying string such as 
         ``.#f`` where # can be a non negative integer: substitute a
         numerical value rounded to the specified number of places beyond
         the decimal point. [:ref:`Floats-Division-Mixed`]

         Example::
         
            'word: {}, number: {}, formatted number: {:.3f}.'.format('Joe', 23, 2.1357)

         evaluates to::
         
             'word: Joe, number: 23, formatted number: 2.136.'

      #.
         | *stringFormatExpression* ``.format(`` \*\* *dictionary* ``)``

         The format expressions are the same as above except that a key name
         from a *dictionary* appears inside the braces. The
         dictionary referenced appears in the parameter list preceded by
         ``**``. Any value to be substituted is then taken from the
         dictionary by accessing the key. Example:
         If ``defs`` is a dictionary with ``defs['name']`` equaling
         ``'Joe'``, ``defs['num']`` equaling ``23``,
         ``defs['dec']`` equaling ``2.13579``, then  ::
         
             'word: {name}, number: {num}, formatted number: {dec:.3f}.'.format(**defs}
             
         evaluates to the same string as in the previous example.
         [:ref:`Dictionaries-and-String`]

         In particular, the dictionary reference can the the dictionary
         of all local variable names, by making the parameter to ``format``
         be ``**locals()``.
         [:ref:`Locals-Dict`]

   #. Strings are a kind of sequence.

#. Type ``list``

   | ``[`` *expression1* ``,`` *expression2* ``,`` and so on ``]``
   | ``[`` *expression* ``]``
   | ``[]``
   
   #. A literal list consists of a comma separated collection of
      values all enclosed in square brackets. There may be many, one, or
      no elements in the list. [:ref:`The-list-Type`]

   #. A list is a kind of sequence, so it may be used as the sequence
      in a ``for`` statement heading. [:ref:`Basic-for-Loops`]


#. Type ``dict`` (short for dictionary)

   ``dict()`` 

   returns an empty dictionary
   
   #. A dictionary provides an association of each key to its value.
      The key can be any immutable type, with includes numbers and
      strings. [:ref:`Dictionaries-I`]

   #.
      | *dictName* ``[`` *keyExpression* ``] =`` *valueExpression*
      
      associates in the dictionary *dictName* the key derived from
      evaluating *keyExpression* with the value derived from evaluating
      *valueExpression*. [:ref:`Dictionaries-I`]

   #. Used in an expression,

      | *dictName* ``[`` *keyExpression* ``]``

      evaluates to the value in the dictionary *dictName* coming from the
      key obtained by evaluating *keyExpression*.
      [:ref:`Dictionaries-I`]


#. Type of ``None``: This literal value has its own special type.
   ``None`` indicates the absence of a regular object.

#. Identifiers
   
   #. Identifiers are names for Python objects
      [:ref:`Literals-and-Identifiers`]

   #. They may only contain letters, digits, and the underscore, and
      cannot start with a digit. They are case sensitive.
      [:ref:`Literals-and-Identifiers`]

   #. You cannot use a reserved word as an identifier, nor are you
      recommended to redefine an identifier predefined by Python. In the
      Idle editor you are safe if your identifier names remain colored
      black. [:ref:`Literals-and-Identifiers`]

   #. By convention, multi-word identifiers either
      [:ref:`Literals-and-Identifiers`]
      
      a. use underscores in place of blanks (since blanks are illegal is
         identifiers), as in ``initial_account_balance``

      #. use camel-case: all lowercase except for the starting letter of
         the second and later words, as in ``initialAccountBalance``

#. Variables are identifiers used to name Python data
   [:ref:`Variables-and-Assignment`]
   
   #. When a variable is used in an expression, its latest value is
      substituted. [:ref:`Variables-and-Assignment`]

#. Statements
   
   #. Assignment statement: [:ref:`Variables-and-Assignment`]
   
      **variable** ``=`` expression

      a. The expression on the right is evaluated, using the latest
         values of all variables, and calculating all operations or
         functions specified.

      #. The expression value is associated with the variable named on
         the left, removing any earlier association with the name.

   #. For-statement

      | ``for`` **item** ``in`` *sequence* ``:`` 
      |     consistently indented statement block, which may use the variable *item* 
           
      For each element in the sequence, repeat the statement block
      substituting the next element in the sequence for the name variable
      name *item*. See Programming Patterns for patterns of use.
      [:ref:`Basic-for-Loops`]

   #. Return statement
   
      ``return`` *expression*

      This is used only in a function definition, causing the function to
      immediately terminate and return the value of expression to the
      calling code, effectively acting as if the function call was
      replaced by this returned value.
      [:ref:`Returned-Function-Values`]

#. Function calls

   *functionName* ``(`` *expression* ``,`` *expression* ``,`` and so on ``)``
   
   #. The number of expressions must correspond to a number of
      parameters allowed by the function's definition.
      [:ref:`Function-Parameters`]

   #. Even if there are no parameters, the parentheses must be
      included to distinguish the name of the function from a request to
      call the function. [:ref:`A-First-Function`]

   #. Each *expression* is called an *actual parameter*.
      Each actual parameter is evaluated and the values are passed to the
      code for the function, which executes its defined steps and may
      return a value. If the function call was a part of a larger
      expression, the returned value is used to evaluate the larger
      expression in the place where the function call was.
      [:ref:`Function-Parameters`]

   #. If nothing is returned explicitly, the function returns
      ``None``.

   #. Function calls may also be used as statements, in which case any
      value that is returned is ignored (except if entered directly into
      the shell, which prints any returned value other than ``None``).

   #. Keyword arguments are a special case. They have been used
      optionally at the end of the parameter list for print.     

#. Functions that are built-in
   
   #. Print function: [:ref:`Print-Statements-I`]
      [:ref:`print-end`]
      
      | ``print(`` *expression* ``)``
      | ``print(`` *expression* ``,`` *expression* ``,`` *expression* ``)``
      | ``print(`` *expression* ``,`` *expression* ``,`` *expression*, ``sep=``\ strVal, ``end=``\ strVal ``)``
      | ``print()``
      
      a. Print the value of each expression in the list to the standard
         place for output (usually the screen) separating each value by
         individual blanks unless the keyword argument ``sep`` is specified
         to change it. There can be any number of expressions (not just 1 or
         3 as illustrated)

      #. The string printed ends with a newline unless the keyword
         argument ``end`` is specified to change it.

      #. With no expression, the statement only advances to a new line.

   #. A type name can be used as function to do obvious conversions to
      the type, as in ``int('234')``, ``float(123)``, ``str(123)``.
      [:ref:`Numbers-and-Digit-Strings`]

   #. ``type(`` *expression* ``)``

      Return the type of the value of the *expression*.
      [:ref:`String-Delimiters-I`]

   #. ``input(`` *promptString* ``)``

      Print the promptString to the screen; wait for the user to enter a
      line from the keyboard, ending with :kbd:`Enter`. Return the character
      sequence as a string [:ref:`The-input-Function`]

   #. ``len(`` *sequence* ``)``
   
      Return the number of elements in the *sequence*
      [:ref:`Whirlwind-Introduction-To`]

   #. ``range(`` *expression* ``)``

      Require expression to have a non negative integer value, call it
      *n*. Generate a sequence with length *n*, consisting of the numbers 0
      through *n*\ -1. For example ``range(4)`` generates the sequence
      ``0, 1, 2, 3`` [:ref:`The-range-Function-I`]

   #. ``max(`` *expression* ``,`` *expression* ``,`` and so on ``)``
   
      Return the maximum of all the expressions listed.
      [:ref:`Whirlwind-Introduction-To`]

   #. ``format(`` *expression* ``,`` *formatString* ``)``
   
      If *expression* is numeric, the format string can be in the form
      ``'.#f'``, where the ``#`` gets replaced by a nonnegative integer, and
      the result is a string with the value of the expression rounded to
      the specified number of digits beyond the decimal point.
      [:ref:`Floats-Division-Mixed`]
   
#. Functions defined by a user:

   | ``def`` **functionName** ``(`` *parameter1* ``,`` *parameter2* ``,`` and so on ``) :`` 
   |     consistently indented statement block, which may include a return statement 
   
   #. There may be any number of parameters. The parentheses must be
      included even if there are no parameters.
      [:ref:`Function-Parameters`]

   #. When a function is first defined, it is only remembered: its
      lines are not executed. [:ref:`A-First-Function`]

   #. When the function is later called in other code, the actual
      parameters in the function call are used to initialize the local
      variables *parameter1*, *parameter2*, and so on in the same order
      as the actual parameters. [:ref:`Function-Parameters`]

   #. The local variables of a function are independent of the local
      names of any function defined outside of this function. The local
      variables must be initialized before use, and the names lose any
      association with their values when the function execution
      terminates. [:ref:`Local-Scope`]

   #. If a return statement is reached, any further statements in the
      function are ignored. [:ref:`Returned-Function-Values`]

   #. Functions should be used to :

      
      a. Emphasize that the code corresponds to one idea and give an
         easily recognizable name. [:ref:`A-First-Function`]

      #. Avoid repetition. If a basic idea is repeated with just the data
         changing, it will be easier to follow and use if it is coded once
         as a function with parameters, that gets called with the
         appropriate actual parameters when needed.
         [:ref:`Function-Parameters`]

      #. It is good to separate the internal processing of data from the
         input and output of data. This typically means placing the
         processing of data and the return of the result in a function.
         [:ref:`Function-Parameters`]

      #. Separate responsibilities: The consumer of a function only needs
         to know the name, parameter usage, and meaning of any returned
         value. Only the writer of a function needs to know the
         implementation of a function. [:ref:`Two-Roles`]

#. Modules (program files)

   #. A module may start with a documentation string.
      [:ref:`Program-Documentation-String`]

   #. Define your functions in your module. If the module is intended
      as a main program called only one way, a convention is make your
      execution just be calling a function called main.
      [:ref:`Multiple-Function-Definitions`]

   #. Avoid defining variable outside of your functions. Names for
      constant (unchanging) values are a reasonable exception.
      [:ref:`Global-Constants`]

#. Documentation String: A string, often a multi-line (triple
   quoted) string that may appear in two places:
   
   #. At the very beginning of a file: This should give overall
      introductory information about the file
      [:ref:`Program-Documentation-String`]

   #. As the very first entry in the body of a function: This should
      describe: [:ref:`Dictionaries-I`]

      
      a. The return value of the function (if there is one)

      #. Anything about the parameters that is not totally obvious from
         the names

      #. Anything about the results from the function that is not obvious
         from the name

#. Programming Patterns

   #. Input-calculate-Output: This is the simplest overall program
      model. First obtain all the data you need (for instance by
      prompting the user for keyboard input). Calculate what you need
      from this data. Output the data (for instance to the screen with
      print functions). [:ref:`The-input-Function`]

   #. Repetitive patterns: These patterns are all associated with
      loops. Loops are essential if the number of repetitions depends on
      dynamic data in the program. Even if you could avoid a loop by
      repeating code, a loop is usually a better choice to make the
      repetitive logic of your program clear to all.

      
      a. Exact repetition some number of times: If the number of time to
         repeat is *n*:

         | ``for`` **i** ``in range(`` *n* ``):`` 
         |     actions to be repeated 

         Here the variable **i** is included only because there must be a
         variable name in a ``for`` loop. [:ref:`Simple-Repeat-Loop`]

      #. For-each loop: Do the same sort of thing for each item in a
         specified sequence. [:ref:`Basic-for-Loops`]

         | ``for`` **item** ``in`` *sequence* ``:`` 
         |     actions to be done with each *item* 


      #. Successive modification loop: Repeat a basic idea, but where the
         data involved each time changes via a pattern that is coded in the
         loop to convert the previous data into the data needed the next
         time through the loop [:ref:`Successive-Modification-Loops`]:

         | initialize all variables that will be successively modified in the loop 
         | loop heading for the repetition ``:`` 
         |     actions to be in each loop with the current variable values 
         |     modify the variable values to prepare for the next time through the loop

      #. Accumulation loop: A sequence of items need to be combined. This
         works where the accumulation of all the items can be approached
         incrementally, combining one after another with the accumulation so
         far [:ref:`Accumulation-Loops`]:

         | initialize the **accumulation** to include none of the *sequence* 
         | ``for`` **item** ``in`` *sequence* ``:`` 
         |      new value of **accumulation** ``=`` partial result
         
         where the partial result comes from combining *item* with the current
         value of *accumulation*
         
#. Playing computer: following code line by line of execution.
   This either tests that you understand your code (and it
   works right) or it helps you find where it goes wrong.
   [:ref:`Updating-Variables`, :ref:`Successive-Modification-Loops`,
   :ref:`Playing-Computer`]
   
   #. Make sure line numbers are labeled

   #. Make a table with heading for line numbers, all variables that
      will be changing, and comments

   #. Follow the order of execution, one statement at a time, being
      careful to update variable values and only use the latest variable
      values, and carefully following the flow of control through loops
      and into and out of function calls.
