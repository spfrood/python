.. index::
   single: web page; dynamic

CGI - Dynamic Web Pages
=======================

*CGI* stands for *Common Gateway Interface*. This interface is used by
web servers to process information requests supplied by a browser.
Python has modules to allow programs to do this work. The
convention used by many servers is to have the server programs that
satisfy this interface end in '.cgi'. That is the convention used
below. All files below ending in '.cgi' are CGI programs on a web
server, and in this chapter, they will all be Python programs
(though there are many other languages in use for this purpose).
These programs are often called scripts, so we will be dealing with
*Python CGI scripts*.

.. _CGI-Example:

An Example in Operation
-----------------------

The first part of this section requires you to have access to the
Internet. Later you will also see that you can illustrate the exact
same actions on your own local machine.

.. index::
   single: web page; execution sequence

For a very simple but complete example, use your browser to go to
the page on the public Loyola server,
http://anh.cs.luc.edu/python/hands-on/3.1/examples/www/adder.html.
You see a web *form*. Follow the instructions, enter numbers, and click
on the :guilabel:`Find Sum` button. You get back a page that obviously used
*your* data. This is the idea that you can generalize. First
consider the basic execution steps behind the scene:

#. The data you type is handled directly by the browser. It
   recognizes forms.

#. An action instruction is stored in the form saying what to do
   when you press a button indicating you are ready to process the
   data (the :guilabel:`Find Sum` button in this case).

#. In the cases we consider in this tutorial, the action is given
   as a web resource, giving the location of a CGI script on some
   server (in our cases, the same directory on the server as the
   current web page).

#. When you press the button, the browser sends the data that you
   entered to that web location (in this case ``adder.cgi`` in the same
   folder as the original web page).

#. The server recognizes the web resource as an executable script,
   sees that it is a Python program, and executes it, using the data
   sent along from the browser form as input.

#. The script runs, manipulates its input data into some results,
   and puts those results into the text of a web page that is the
   output of the program.

#. The server captures this output from the program and sends it
   back to your browser as a new page to display.

#. You see the results in your browser.

This also works *locally*, entirely on your own computer, using a
simple server built into Python. (*Internet no longer needed!*)

Windows  
	In an operating system file window, go to the folder with the www
	examples. Double click on ``localCGIServer.py`` to start the local,
	internal, web server. You should see a console window pop up,
	saying "Localhost CGI server started" . 

Mac
    This is more involved.  
    See http://anh.cs.luc.edu/python/hands-on/3.1/pythonOnMac.html. 

Once the server is
started, leave the console window there as long as you want the
local server running. 

.. warning::
   Do *not* start the local server running from inside Idle.

.. note::
   If the server aborts and gives an error message about
   spaces in the path, look at the path through the parent directories
   over this www directory. If any of the directory names have spaces
   in them, the local file server will not work.

In case of this error, either go up the
directory chain and alter the directory names to eliminate spaces
or move the examples directory to a directory that does not have
this issue. In particular, you need to move your examples directory
if it is under the 'My Programs' directory.

Back in the www directory, *after you have the local server going*,

#. Open the web link http://localhost:8080/adder.html (preferably
   in a new window, separate from this tutorial).

#. You should see an adder form in your browser again. Note that
   the web address no longer includes 'cs.luc.edu'. Instead it starts
   with 'localhost:8080', to reference the local Python server you
   started. Fill out the form and test it as before.

#. Look at the console window. You should see a log of the activity
   with the server. *Close* the server window.

#. Reload the web link http://localhost:8080/adder.html. You should
   get an error, since you refer to localhost, but you just stopped
   the local server.

For the rest of this chapter, we will be wanting to use the local
server, so *restart* ``localCGIServer.py`` *from its operating system*
*folder*, and *keep it going*.

A Simple Buildup
----------------

Before we get too complicated, consider the source code of a couple
of even simpler examples.

.. rubric:: hellotxt.cgi

.. index::
   single: #!

The simplest case is a CGI script with no input that just
generates plain text, rather than HTML.
*Assuming you have your local server going*, you can go to the link
for hellotxt.cgi, http://localhost:8080/hellotxt.cgi. The code is
in the www example directory, ``hellotxt.cgi``, and below for you
to *read*:

.. literalinclude:: ../examples/www/hellotxt.cgi

The top line is what tells the operating system that this is a Python 3
program. It says where to find the right Python interpreter to process
the rest of the script. This exact location is significant 
on a Unix derived server (like the one Loyola's Computer Science Department
uses or any Mac with OS X). In Windows the only thing important is the distinction
between Python 2 and 3.
If you leave the line there
as a part of your standard text, you have one less thing to think
about when uploading to a Unix server or running on a Mac.

The first print function is telling the server receiving this
output that the format of the rest of the output will be plain
text. This information gets passed back to the browser later. This
line should be included exactly as stated IF you only want the
output to be plain text (the simplest case, but *not our usual*
case).

The rest of the output (in this case just from one print function)
becomes the body of the plain text document you see on your browser
screen, verbatim since it is plain text. The server captures this
output and redirects it to your browser.

.. rubric:: hellohtml.cgi

We can make some variation and display an already determined *html*
page rather than plain text. Try the link
http://localhost:8080/hellohtml.cgi. The code is in the www example
directory, ``hellohtml.cgi``, and below for you to *read*:

.. literalinclude:: ../examples/www/hellohtml.cgi

There are two noteworthy changes. The *first* print function now
declares the rest of the output will be *html*. This is the
standard line you will be using for your CGI programs. The
remaining print function has the markup for an html page. Note that
the enclosing triple quotes work for a multi line string. Other
than as a simple illustration, this CGI script has no utility: Just
putting the contents of the last print function in a file for a
static web page ``hello.html`` is much simpler.

.. rubric:: now.cgi

One more simple step: we can have a CGI script that generates
dynamic output by reading the clock from inside of Python: Try the
link http://localhost:8080/now.cgi. Then click the refresh button
and look again. This cannot come from a static page. The code is in
the www example directory, ``now.cgi``, and below for you to
*read*:

.. literalinclude:: ../examples/www/now.cgi

This illustrates a couple more ideas: First a library module,
``time``, is imported and used to generate the string for the
current date and time.

The web page is generated like in ``helloWeb2.py``, embedding the
dynamic data (in this case the time) into a literal web page format
string. (Note the embedded ``{timeStr}``.) Unlike ``helloWeb2.py``,
this is a CGI script so the web page contents are delivered to the
server just with a ``print`` function.

.. _adder.cgi:
    
.. rubric:: adder.cgi

It is a small further step to get to processing dynamic input. Try filling
out and submitting the adder form one more time,
http://localhost:8080/adder.html. This time notice the URL at the
top of the browser page *when the result is displayed*. You should
see something like the following (only the numbers should be the
ones *you* entered):

   http://localhost:8080/adder.cgi?x=24&y=56

This shows one
mechanism to deliver data from a web form to the CGI script that
processes it. The names x and y are used in the form (as we will
see later) and the data you entered is associated with those names.
In fact a form is not needed at all to create such an association:
If you directly go to the URLs

    http://localhost:8080/adder.cgi?x=24&y=56

or

    http://localhost:8080/adder.cgi?x=-12345678924&y=33333333333

you get arithmetic displayed without the form. This is just a new input
mechanism into the CGI script.

You have already seen a program to produce this adder page from
inside a regular Python program taking input from the keyboard. The
new CGI version, adder.cgi, only needs to make a few modifications
to accept input this way from the browser. New features are
commented in the source and discussed below. The new parts are the
``import`` statement through the ``main`` function, and the code
after the end of the ``fileToStr`` function. *Read* at least these
new parts in the source code shown below:

.. literalinclude:: ../examples/www/adder.cgi

.. index::
   cgi; module

First the overall structure of the code:


-  To handle the CGI input we import the ``cgi`` module.

-  The main body of the code is in a ``main`` method, following
   good programming practice.

-  After the definition of ``main`` come supporting functions, each
   one copied from the earlier local web page version,
   additionWeb.py.


-  At the end is the new, but standard, cgi wrapper code for
   ``main()``. This is code that you can always just copy. I chose to
   put the initial ``print`` function here, that tells the server html
   is being produced. That mean the ``main`` method only needs to
   construct and print the *actual* html code. Also keep the final
   ``try``\ -``except`` block that catches any execution errors in the
   program and generates possibly helpful trace information that you
   can see from your browser. (Writing such error catching code in
   general is not covered in this introductory tutorial,
   but you can copy it!)

The ``main`` function has three sections, as in the local web page
version: read input (this time from the form), process it, and
generate the html output.


-  Reading input: The first line of main is a standard one (to
   copy) that sets up an object called ``form`` that holds the CGI
   form data accompanying the web request sent by the browser. You
   access the form data with statements like the next two that have
   the pattern:

       **variable** ``= form.getfirst(`` *nameAttrib* ``,`` *default* ``)`` 

   If there is a form field with name *nameAttrib*, its value
   from the browser data is assigned to *variable*. If no value is
   given in the browser's data for *nameAttrib*,
   *variable* is set equal to *default* instead.

   In this way
   data associated with names given by the browser can transferred to
   your Python CGI program. In this program the values associated with
   the browser-supplied names, 'x' and 'y', are extracted. I use
   Python variable names that remind you that all values from the
   browser forms are strings.

-  The ``processInput`` function that is passed the input
   parameters from whatever source, is exactly the same as in
   ``additionWeb.py``, so we already know it works!

-  Output the page. In a CGI script this is easier than with the
   local web pages: just print it - no need to save and separately
   display a file! The server captures the "printed" output.

This program can now serve as a template for your own CGI scripts:
The only things you need to change are the lines in ``main()`` that
get the input from a web form, and the contents of
``processInput``.  Furthermore the ``processInput`` part can be written and
tested earlier with a local web page. While this is the only Python
code, you still need to create an output web page template, and
refer to it in the parameter of ``fileToStr``.
A further stripped down skeleton, with comments about needed changes is in
``skeletonFor.cgi``.

Now we have discussed both the top regular Python sequence, the bottom
cgi sequence, and the common part in the middle, as shown in the following
diagram.  In both cases input data gets processed into the content of a
web page that goes to a browser.  For any major application the main work
is in the processing in the middle.  Since that part is shared in both
approaches, it can be tested with a simple Python program,
before the starting and ending steps
for the input and output flow are changed for the cgi client/server model.

.. figure:: images/dynamicWebFlow.*
   :align: center
   :alt: image
   :width: 461.25 pt

The only part that still needs details explained is for web forms.
Before going on to that, it is time to talk about handling errors
in the CGI scripts we have been discussing.

.. index::
   single: cgi; errors

.. _Errors-in-CGI:
    
Errors in CGI Scripts
---------------------

Before you start running your own CGI scripts on the local server,
it is important to understand how different kinds of errors that
you might make will be handled.

If you write a regular Python program, even one that produces a web page,
you can write the code and run it in Idle, and idle will display all the
kinds of errors.

With a CGI script, you can still use Idle to write your code,
but you cannot run the cgi code in Idle, and errors show up in three
different places, depending on their type:

Syntax errors
    You are encouraged to check for syntax errors
    *inside* Idle, by either going to the Run menu and selecting Check
    Module, or by using the shortcut :kbd:`Alt-X`. If you fail to do this and
    try running a script with a syntax error, the error trace appears
    in the *console* window that appears when you start the local
    server. If you want an illustration, you might try changing
    adder.cgi, making an error like ``impor cgi``, and try using
    adder.html with the flawed script. (Then fix it and try again.)

Execution Errors
    The error trace for execution errors is
    displayed in your *web browser*, thanks to the final standard code
    with the ``try``\ -``catch`` block at the end of the CGI script.
    *If you omit that final standard code, you completely lose descriptive*
    *feedback: Be sure to include that standard code!* You can also
    illustrate here. Get an error by introducing the statement::

        bad = 'a'.append('b')

    in the main function.
    (Then take it out.)

Server Errors
    Your work can cause an issue inside the local server,
    not directly in the Python execution.  Some errors are
    communicated to the browser, but not necessarily all.
    Other errors appear in the log generated in the local server's window.
    It does not appear likely that you will miss something
    in Windows, but on a Mac or in Linux, where the CGI script needs
    to be set as executable, an error with a non-executable CGI script
    only shows up in this log in the local server window.

Logical Errors
    Since your output appears in the web browser,
    when you produced something legal but other than what you intended,
    you see in the browser . If it is a formatting error, fix your
    output page template. If you get wrong answers, check your
    ``processInput`` function.

Here is an outline for client/server program testing,
emphasizing errors to be conscious of and avoid:

* If you want an easy environment to test a fancy ``processInput`` function,
  embed it
  in a regular Python program, so you can test it normally in Idle.
  This will also allow you to make sure the web template, that you refer to
  in your ``processInput`` function, is in a legitimate form,
  with substitutions only for local variables.

* You can *code* a CGI script in idle, but *not run* it.
  Be sure to save it with the suffix ``.cgi``,
  *not* ``.py``.  Do *not run* it it Idle.  The only testing you can do in Idle
  is for syntax, for instance using the :kbd:`Alt-X` keyboard shortcut.

* At the end of your CGI script, make sure you include the standard
  code that catches execution errors.

* Make sure your local server is going, and that all the files you
  reference are in the same folder as the local server.

* Make sure you test your page by starting it in your web browser with a
  URL starting ``http://localhost:8080/``.  If you load a web page
  directly from your file system by mistake, it *will not cause an obvious error* -
  the dynamic actions will just not take place.  If you are not paying attention,
  this can happen and be very confusing!

We have not covered web forms yet, but rather than bite off too
much at once, this is a good time to write your own first CGI
script in the following exercise.

.. _quotient.cgi:

Quotient.cgi Exercise
~~~~~~~~~~~~~~~~~~~~~

\* Modify :ref:`quotientWeb` and save it as a CGI script
``quotient.cgi`` in the *same* directory where you have
``localCGIServer.py`` and your output page template for ``quotientWeb.py``.
Make ``quotient.cgi`` take its input from a browser, rather than the
keyboard. This means merging all the standard CGI code from
``adder.cgi`` and the ``processInput`` function code from your
``quotientWeb.py``. You
can keep the same browser data names, x and y, as in adder.cgi, so
the main method should not need changes from adder.cgi. Remember to
test for syntax errors inside Idle, and to have the local web
server running when you run the CGI script in your browser. Since
we have not yet covered web forms, test your CGI script by entering
test data into the URL in the browser, like by going to links
http://localhost:8080/quotient.cgi?x=24&y=56 and
http://localhost:8080/quotient.cgi?x=36&y=15. After trying these
links, you can edit the numbers in the URL in the browser to see
different results.


.. index::
   single: web page; form

.. _Editing-HTML-Forms:
    
Editing HTML Forms
------------------

This section is a continuation of
:ref:`Introduction-to-Static`. It is about HTML editing, not
Python. HTML forms will allow user-friendly data entry for Python
CGI scripts. This is the last elaboration to allow basic web
interaction: Enter data in a form, submit it, and get a processed
result back from the server.

The initial example, adder.html, used only two text fields. To see
more common form fields, open
http://localhost:8080/commonFormFields.html. (Make sure your local
server is still running!)

To allow easy concentration on the data sent by the browser, this
form connects to a simple CGI script ``dumpcgi.cgi``, that just
dumps and labels all the form data to a web page.
Press the submit button in
the form, and see the result. Back up from the output to the
previous page, the form, and change some of the data in all kinds
of fields. Submit again and see the results. Play with this until
you get the idea clearly that the form is passing on your data.

To play with it at a deeper level, open this same file, the www
example ``commonFormFields.html``, in *Kompozer*. The static text in
this page is set up as a tutorial on forms in Kompozer. Read the
content of the page describing how to edit the overall form and
each type of individual field. Textbooks such as the Analytical
Engine give another discussion of some of the attributes associated
with each field type. Read the static text about how to edit
individual fields, and change some field parameters, save the file
and reload it in your browser, and submit again. If you change the
name or value attributes, they are immediately indicated in the
dumped output. If you change things like the text field size, it
makes a change in the way the form looks and behaves. You can
return to the original version: An extra copy is saved in
``commonFormFieldsOrig.html``.

Now open ``adder.html`` in Kompozer. Switch to the Source view. This is
a short enough page that you should not get lost in the source
code. The raw text illustrates another feature of html: attributes.
The tag to start the form contains not only the tag code *form*,
but also several expressions that look like Python assignment
statements with string values. The names on the left-hand side of
the equal signs identify a type of *attribute*, and the string
value after the equal sign gives the corresponding *value* for the
attribute. The tag for many kinds of input fields is ``input``.
Notice that each field includes ``name`` and ``value`` attributes.
See that the 'x' and 'y' that are passed in the URL by the browser
come from the names given in the HTML code for the corresponding
fields!

Kompozer and other web editors translate your menu selections into
the raw html code with proper attribute types. This high level
editor behavior is convenient to avoid having to learn and debug
the exact right html syntax! On the other hand, using pop-up field
editing windows has the disadvantage that you can only see the
attributes of one field at a time. Particularly if you want to
modify a number of name or value attributes, it is annoying that
you need a number of mouse clicks to go from one field to the next.
If you *only* want to modify the *values* of existing attributes like
``name`` and ``value``, it may be easier to do in the source
window, where you can see everything at once. Making syntax errors
in not very likely if you *only* change data in quoted value
strings.

The action URL is a property of the entire form. To edit it in
Kompozer, right click inside the form, but *not* on any field
element, and select the bottom pop-up choice, Form Properties. Then
you see a window listing the Action URL and you can change the
value to the name of the CGI script that you want to receive the
form data. When you create your own web form, I suggest you make
the initial action URL be dumpcgi.cgi. This will allow you to debug
your form separate from your CGI script. When you have tested that
your web form has all the right names and initial values, you can
change the action URL to your CGI script name (like quotient.cgi),
and go on to test the combination of the form and the CGI script!


Now we have discussed the last piece, web forms,
in the diagram for the comparison of generating web pages dynamically
by a regular Python program or a server CGI script:
    
.. figure:: images/dynamicWebFlow.*
   :align: center
   :alt: image
   :width: 490 pt

Note the last three Python videos do not directly corresponding to a single
place in the Tutorial text.  Instead they go through the entire process
for web based programs from the beginning.
Video 4.4.4b creates a ``birthday.html`` web form looking forward to
``birthday.cgi`` of video 4.4.4d.
In the middle video 4.4.4c creates ``birthdayWeb.py``, testing the process
function and output template to be used in ``birthday.cgi``.    

QuotientWeb Form Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~

\* Complete the web presentation for quotient.cgi of
:ref:`quotient.cgi` by creating a web form ``quotient.html`` that
is intelligible to a user and which supplies the necessary data to
``quotient.cgi``.

Be sure to test the new form on your local server! Remember that
you must have the local server running first. You must have all the
associated files in the same directory as the server program you
are running, and you cannot just click on quotient.html in a file
browser. You must start it from the the URL
http://localhost:8080/quotient.html, that specifically refers to
the server localhost.

Dynamic Web Programming Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\* Make a simple complete dynamic web presentation with a CGI
script that uses at least *three* user inputs from a form. The
simplest would be to just add three numbers instead of two. Call
your form ``dynamic.html``. Call your CGI script ``dynamic.cgi``. Call an
output template ``dynamicTemplate.html``. Remember the details listed
in the previous exercise to make the results work on localhost.
After the server is started and you have all the files, go to
http://localhost:8080/dynamic.html.


:ref:`websummary` starts with the overall process for
creating dynamic web pages.

.. _More-Advanced-Examples:
    
More Advanced Examples
----------------------

One of the advantages of having a program running on a public
server is that data may be stored centrally and augmented and
shared by all. In high performance sites data is typically stored
in a sophisticated database, beyond the scope of this tutorial. For
a less robust but simpler way to store data persistently, we can
use simple text files on the server.

The www example page ``namelist.html`` uses ``namelist.cgi`` to maintain a
file ``namelist.txt`` of data submitted by users of the page. You can
test the program with your local Python server. It is less
impressive when you are the only one who can make changes! You may
also try the copy on the public Loyola server,
http://anh.cs.luc.edu/python/hands-on/3.1/examples/www/namelist.html.
The local source code is documented for those who would like to
have a look.

You also may want to look at the source code of the utility script
you have been using, ``dumpcgi.cgi``. It uses a method of getting
values from the CGI data that has not been discussed::

    val = form.getlist(name) 

This method returns a list of values associated with a name from
the web form. The list many have, 0, 1, or many elements. It is
needed if you have a number of check boxes with the same name.
(Maybe you want a list of all the toppings someone selects for a
pizza.)

Both ``dumpcgi.cgi`` and ``namelist.html`` add an extra layer of robustness
in reflecting back arbitrary text from a user. The user's text may
include symbols used specially in html like '<'. The function
``safePlainText`` replaces reserved symbols with appropriate
alternatives.

The examples in earlier sections were designed to illustrate the
flow of data from input form to output page, but neither the html
or the data transformations have been very complicated. A more
elaborate situation is ordering pizza online, and recording the
orders for the restaurant owner. You can try
http://localhost:8080/pizza1.cgi several times and look at the
supporting example www files ``pizza1.cgi``, ``pizzaOrderTemplate1.html``,
and the simple ``pizzaReportTemplate.html``. To see the report, the
owner needs to know the special name ``owner777``. After ordering
several pizzas, enter that name and press the Submit button again.

This CGI script gets used in two ways by a regular user: initially,
when there is no order, and later to confirm an order that has been
submitted. The two situations use different logic, and the script
must distinguish what is the current use. A *hidden variable* is used
to distinguish the two cases: when pizza1.cgi is called directly
(not from a form), there is no ``pastState`` field. On the other hand
the ``pizzaOrderTemplate1.html`` includes a hidden field named
``pastState``, which is set to the value ``'order'``. (You can confirm this
by examining the end of the page in Kompozer's source mode.) The CGI
script checks the value of the field ``pastState``, and varies its
behavior based on whether the value is ``'order'`` or not.

The form in pizzaOrderTemplate1.html has radio buttons and check
boxes hard coded into it for the options, and copies of the data
are in pizza1.cgi. Keeping multiple active copies of data is not a
good idea: They can get out of sync. If you look at the source code
for pizzaOrderTemplate1.html, you see that all the entries for the
radio button and check box lines are in a similar form. In the
better version with altered files ``pizza.cgi`` and
``pizzaOrderTemplate.html`` (that appears the same to the user), the
basic data for the pizza options is only in one place in ``pizza.cgi``,
and the proper number of lines of radio buttons and check boxes
with the right data are generated dynamically.  To do the dynamic generation,
a templates for an individual html line with a size radio button
is in the source code, and it is used repeatedly to generate multiple lines, each with
a different size and price embedded into the format string
from the program data.  These lines are joined
together and placed as one entity into the html form template. 
A similar procedure is done with the toppings and checkboxes.

A further possible elaboration would be to also allow the
restaurant manager to edit the size, cost and available topping data online,
and store the data in a file rather than having the data hard coded in
pizza.cgi, so if the manager runs out of a topping, she can remove
it from the order form. This change would be a fairly elaborate
project compared to the earlier exercises!

.. put back when it works!

    Final www examples are a pair of programs in real use in my
    courses. To illustrate, I provide the sample survey,
    ``pythonTutorialsurvey.html``.  Forms can be set up like this one
    to link to the www example CGI script ``surveyFeedback.cgi``, which
    will save any number of responses to the survey.  Unfortunately
    this script does not work under Python 3+ as yet.  (My Python 2.6 version
    should still work, but that is not in this version of the example code.)
    When it is fixed,
    you can do the survey at
    http://localhost:8080/pythonTutorialsurvey.html. Run it several
    times with different responses.                                                        
    Assuming you get this to work, and you have responses,
    you can start the Idle shortcut in the www example
    directory and run the regular Python program that is in that directory,
    ``readFeedback.py``.  At the prompt for a survey base name, enter *exactly*:

        pythonTutorial

    Then the program prints out all the survey feedback, grouped in two
    different ways. It documents the use of a couple of modules not
    introduced in this tutorial, but the rest just uses ideas from the
    tutorial, including considerable emphasis on dictionaries and
    string processing.
