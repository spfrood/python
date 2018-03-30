.. _websummary:
    
Summary
=======

#. The Overall Process for Creating Dynamic Web Pages

   Making dynamic web pages has a number of steps. I have suggested
   several ways of decoupling the parts, so you can alter the order,
   but if you are starting from nothing, you might follow the
   following sequence:
   
   #. Determine the inputs you want to work with and make a web form
      that makes it easy and obvious for the user to provide the data.
      You may initially want to have the form's action URL be
      ``dumpcgi.cgi``, so you can debug the form separately. Test with the
      local server. When everything seems OK, *make sure to change the
      action URL to be the name of the CGI script you are writing*.
      [:ref:`Editing-HTML-Forms`]

   #. It is easier to debug a regular Python program totally inside
      Idle than to mix the Idle editor and server execution. Particularly
      if the generation of output data is going to be complicated or
      there are lots of places you are planning to insert data into an
      output template, I suggest you write the ``processInput`` function
      with its output template first and test it *without* a server, as we
      did with ``additionWeb.py``, providing either canned input in the
      main program, or taking input data from the keyboard,
      and saving the output page to a local file that you examine in your
      webbrowser. [:ref:`Dynamically-Created-Static`]

   #. When you are confident about your ``processInput`` function, put
      it in a program with the proper cgi skeleton, and add the necessary
      lines at the beginning of the ``main`` function to take all the CGI
      script input from the browser data. [:ref:`adder.cgi <adder.cgi>`]

   #. Be sure to check for syntax errors in Idle, for instance using
      :kbd:`Alt-X`.  Fix as necessary.
                                                       
   #. Finally test the whole thing with the local server.  Make sure the
      local server is running, and all the resources that you refer to are in
      the same folder as the local web server:  Initial web page, web page
      templates, CGI script.  Do not open the starting web page or CGI script
      in Idle or by finding it in your file system.  You must run it in
      your browser with a URL that starts with ``http://localhost:8080/``.
      In error, if you load a web page
      directly from your file system, it will not cause an obvious error -
      the dynamic actions will just not take place.
      

   #. If is does not work right:

      * If you get a page that uses your template, but it looks wrong,
        either fix your template or look for a logical error in your
        program.  (If you had tested your ``processInput`` function
        in a regular Python program before, this should not happen.)
      
      * If the web page output shows an error description, see if you can
        pick any help out and go back and fix your code.

      * If you get nothing
        back in your web browser, make sure you had tested the final version
        of the code in Idle for syntax errors (:kbd:`Alt-X`),
        and that you have the final error catching code in the CGI script,
        and that you used a URL that starts with ``http://localhost:8080/``.

      * If all of the parts mentioned above are there, the problem may be
        with the server, not Python.
        Look in the local server window's log output,
        and see if it points to a filename that it cannot find or ....

   #. If you have an account on a public server, it should not take
      much more work than just uploading your files to make your creation
      available to the whole world. You may have a public server with a
      different configuration than the Loyola server. If so see this
      note: [#]_

#. Markup: Plain text may be *marked up* to include formatting. The
   formatting may be easily interpreted only by a computer, or it may
   be more human readable. One form of human-readable markup is
   hypertext markup language (HTML). [:ref:`Format-of-Web`]

   
   #. HTML markup involves tags enclosed in angle braces. Ending tags
      start with '/'. For instance  
      ``<title>Computer Science</title>``.
      
      #. Tags may be modified with attributes specified similar to Python
         string assignments, for example the text input field tag, ::

             <input value="red" name="color" type="radio">

   #. Modern editors allow HTML to be edited much like in a word
      processor. Two views of the data are useful: the formatted view and
      the source view, showing the raw HTML markup.

#. Python and HTML: Since HTML is just a text string, it can easily
   be manipulated in Python, and read and written to text files.
   [:ref:`Dynamically-Created-Static`]

#. The ``webbrowser`` module has a function ``open``, that will
   open a file or web URL in the default browser:
   [:ref:`Dynamically-Created-Static`]
   
       ``webbrowser.open(`` *filename* ``)``

#. Common Gateway Interface (CGI). The sequence of events for
   generating a dynamic web page via CGI: [:ref:`CGI-Example`]
   
   #. The data a user types is handled directly by the browser. It
      recognizes forms.

   #. The user presses a Submit button. An action is stored in the
      form saying what to do when the button is pressed.

   #. In the cases we consider in this tutorial, the action is given
      as a web resource, giving the location of a CGI script on some
      server. The browser sends the data that you entered to that web
      location.

   #. The server recognizes the page as an executable script, sees
      that it is a Python program, and executes it, using the data sent
      along from the browser form as input.

   #. The script runs, manipulates the input data into some results,
      and puts those results into the text of a web page that is the
      output of the program.

   #. The server captures this output from the program and send it
      back to the user's browser as a new page to display.

   #. The results appear in the user's browser.

#. The ``cgi`` Module
   
   #. Create the object to process CGI input with [:ref:`adder.cgi <adder.cgi>`] ::

          form = cgi.FieldStorage()

   #. Extract the first value specified by the browser with name
      *nameAttrib*, or use *default* if no such value
      exists [:ref:`adder.cgi <adder.cgi>`]
   
          **variable** ``= form.getfirst(`` *nameAttrib* ``,`` *default* ``)``

   #. Extract the ``list`` of all values specified by the browser
      associated with
      name *nameAttrib* [ref{:ref:`More-Advanced-Examples`]

           *listVariable* ``= form.getlist(`` *nameAttrib* ``)`` 

      This case occurs if you have a number of checkboxes, all with the
      same name, but different values.  The list may be empty.


#. Local Python Servers.
   
   #. Python has modules for creating local testing servers that can
      handle static web pages and Python CGI
      scripts.[:ref:`CGI-Example`]

   #. Different kinds of errors with CGI scripts are handled different
      ways by a local Python server. [:ref:`Errors-in-CGI`]


#. A comparison of the various types of files used in web
   programming, listing the different ways to edit and use the files,
   is given in :ref:`Editing-and-Testing`.

.. [#]
   The tutorial assumed a server configured as follows: html pages and
   CGI scripts can all be in the same directory, and the CGI scripts
   end with .cgi. This is the convention on Loyola's Computer Science
   public server. Another common configuration is that scripts
   all go in a cgi-bin directory, where they just have the normal .py
   suffix. If you have a server with the latter configuration, your
   action URLs will be of the form cgi-bin/*someScript*.py. Depending
   on the server configuration the current directory may or may not be
   cgi-bin while the script executes. That may mean you need a path
   before the file names for your output templates, or your need to be
   careful what directory referenced files end up in. If you are
   making arrangements for your own site on a public server, be sure
   to check with your system administrator to find out what the
   conventions are.
