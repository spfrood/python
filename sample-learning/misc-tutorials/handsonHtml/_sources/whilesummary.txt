.. whilesummary:
   
Summary
=======

#. Comparison operators produce a Boolean result (type ``bool``,
   either ``True`` or ``False``):
   [:ref:`More-Conditional-Expressions`]

   =====================  ===========  ==============
   Meaning                Math Symbol  Python Symbols
   =====================  ===========  ==============
   Less than              <            ``<`` 
   Greater than           >            ``>``
   Less than or equal     ≤            ``<=``
   Greater than or equal  ≥            ``>=``
   Equals                 =            ``==``
   Not equal              ≠            ``!=``
   =====================  ===========  ============== 

   Comparisons may be chained as in ``a < b <= c < d != e``.
   [:ref:`Multiple-Tests`]

#. The ``in`` operator: [:ref:`Arbitrary-Types-Bool`]

       *value* ``in`` *sequence*

   is True if *value* is one of the elements in the
   *sequence*.

#. Interpretation as Boolean (``True``, ``False``):
   All Python data may be converted to Boolean (type ``bool``). The
   only built-in data that have a Boolean meaning of ``False``,
   in addition to
   ``False`` itself, are ``None``, numeric values equal to 0, and
   empty collections or sequences, like the empty list {[]}and the
   empty string ``''``. [:ref:`Arbitrary-Types-Bool`]

#. Operators on Boolean expressions
   [:ref:`Compound-Boolean-Expressions`]

   #.
      | *condition1* ``and`` *condition2*
      | ``True`` only if both conditions are ``True``

   #. 
      | *condition1* ``or`` *condition2*
      | ``True`` only if at least one condition is ``True``

   #.
      | ``not`` *condition*
      | ``True`` only when *condition* is ``False``

   This description is sufficient if the result is used as a Boolean
   value (in an ``if`` or ``while`` condition). See 
   :ref:`Arbitrary-Types-Bool` for the advanced use when operands are
   not explicitly Boolean, and the result is not going to be
   interpreted as Boolean.

#. ``if`` Statements
   
   #. Simple ``if`` statement [:ref:`Simple-if-Statements`]

      | ``if`` *condition* ``:`` 
      |       indentedStatementBlockForTrueCondition
           
      If the condition is ``True``, then do the indented statement block. If
      the condition is not ``True``, then skip it.

   #. ``if-else`` statement [:ref:`if-else-Statements`]

      | ``if`` *condition* ``:`` 
      |     indentedStatementBlockForTrueCondition
      | ``else:`` 
      |     indentedStatementBlockForFalseCondition


      If the condition is ``True,`` then do the first indented block only. If
      the condition is not ``True``, then skip the first indented block and
      do the one after the ``else:``.

   #. The most general syntax for an if statement,
      |if-elif-else| [:ref:`Multiple-Tests`]

      | ``if`` *condition1* ``:`` 
      |    indentedStatementBlockForTrueCondition1 
      | ``elif`` *condition2* ``:`` 
      |     indentedStatementBlockForFirstTrueCondition2 
      | ``elif`` *condition3* ``:`` 
      |     indentedStatementBlockForFirstTrueCondition3 
      | ``elif`` *condition4* ``:`` 
      |     indentedStatementBlockForFirstTrueCondition4 
      | ``else:`` 
      |     indentedStatementBlockForEachConditionFalse 


      The ``if``, each ``elif``, and the final ``else`` line are all
      aligned. There can be any number of ``elif`` lines, each followed
      by an indented block. (Three happen to be illustrated above.) With
      this construction exactly *one* of the indented blocks is executed.
      It is the one corresponding to the *first* ``True`` condition, or,
      if all conditions are ``False``, it is the block after the final
      ``else`` line.

   #. |if-elif| [:ref:`Multiple-Tests`]
      The ``else:`` clause above may also be omitted. In that case, if
      none of the conditions is true, no indented block is executed.

#. ``while`` statements [:ref:`Simple-while-Loops`]

   | ``while`` *condition* ``:`` 
   |     indentedStatementBlock

   Do the indented block if *condition* is ``True``, and at the
   end of the indented block loop back and test the *condition* again,
   and continue repeating the indented block as long as the condition
   is ``True`` *after* completing the indented block. Execution does
   not stop in the middle of the block, even if the
   *condition* becomes ``False`` at that point.

   A ``while`` loop can be used to set up an (intentionally)
   apparently infinite loop by making *condition* be just
   ``True``. To end the loop in that case, there can be a test inside
   the loop that sometime becomes True, allowing the execution of a
   ``return`` statement to break out of the loop.
   [:ref:`Fancier-Animation-Loop`]

#. ``range`` function with three parameters
   [:ref:`Simple-while-Loops`]

       ``range(`` *start* ``,``  *pastEnd* ``,`` *step* ``)``

   Return a list of elements

       ``[`` *start* ``,`` *start* ``+`` *step* ``,`` ... ``]``

   with each element *step* from the previous one, ending just *before*
   reaching *pastEnd*. If  *step* is positive,
   *pastEnd* is larger than the last element. If
   *step* is negative,  *pastEnd* is smaller than the
   last element.

#. Type ``tuple``

   | ``(`` *expression* ``,`` *expression* ``,`` and so on ``)``
   | ``(`` *expression* ``, )``
   | ``( )``
   
   #. A literal tuple, with two or more elements, consists of a comma
      separated collection of values all enclosed in parentheses. A
      literal tuple with only a single element *must* have a comma after
      the element to distinguish from a regular parenthesized expression.
      [:ref:`Loops-and-Tuples`]

   #. A tuple is a kind of sequence.

   #. Tuples, unlike lists, are immutable (may not be altered).

#. Additional programming techniques
   
   #. These techniques extend the techniques listed in the summary of
      the previous chapter. [:ref:`objectSummary`]

   #. The basic pattern for programming with a while loop is
      [:ref:`Simple-while-Loops`] 

      | initialization 
      | ``while`` *continuationCondition* ``:`` 
      |     main action to repeat 
      |     prepare variables for next time through loop

   #. Interactive while loops generally follow the pattern
      [:ref:`Interactive-while-Loops`]

      | input first data from user
      | ``while`` *continationConditionBasedOnTestOfUserData* ``:`` 
      |     process user data 
      |     input *next* user data 

      Often the code to input the first data and the later data is the
      same, but it must appear in both places!

   #. Sentinel Loops [:ref:`Interactive-while-Loops`]

      Often the end of the repetition of a data-reading loop is indicated
      by a *sentinel* in the data: a data value known to both the user
      and the program to not be regular data, that is specifically used
      to signal the end of the data.

   #. Nesting Control Flow Statements
      [:ref:`Nesting-Control-Flow-Statements`]
      
      #. ``If`` statements may be nested inside loops, so the loop does
         not have to execute all the same code each time; it just needs
         to start with the same *test*.

      #. Loops may be nested. The inner loop completes its repetitions
         each time before going back to the outer loop heading.

   #. Breaking a repeating pattern into a loop
      [:ref:`Graphical-Applications`]

      Since a loop is basically circular, there may be several choices of
      where to split it to list it in the loop body. The split point
      needs to be where the continuation test is ready to be run, but
      that may still allow flexibility. When you choose to change the
      starting point of the loop, and rotate statements between the
      beginning and the end of the loop, you change what statements need
      to be included before and after the loop, sometimes repeating or
      undoing actions taken in the loop.

   #. Tuples in lists [:ref:`Loops-and-Tuples`]
      A list may contain tuples. A |for-each| loop may process tuples in a
      list, and the ``for`` loop heading can do multiple assignments to
      variables for each element of the next tuple.

   #. Tuples as return values [:ref:`Loops-and-Tuples`]
      A function may return more than one value by wrapping them in a
      tuple. The function may then be used in a multiple assignment
      statement to extract each of the returned variables.

#. Graphics
   
   #. Zelle's Graphics GraphWin method ``checkMouse()`` allows mouse
      tests without stopping animation, by testing the last mouse click,
      not waiting for a new one. [:ref:`Graphical-Applications`]

   #. The most finished examples of using Zelle's graphics are in
      [:ref:`Loops-and-Tuples`] and [:ref:`Graphical-Applications`].
