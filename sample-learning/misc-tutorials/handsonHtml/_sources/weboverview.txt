Overview
========

This chapter leads up to the creation of dynamic web pages. These
pages and supporting programs and data may be tested locally via a
simple Python web server available on your local machine. If you
have access, the pages and programs may be uploaded to a public
server accessible to anyone on the Internet.

A few disclaimers:

-  This tutorial does not cover uploading to an account on a public
   server.

-  No core Python syntax is introduced in this Chapter. Only a few
   methods in a couple of Python library modules are introduced.

-  The chapter is by no means a major source of information about
   specific HTML codes. That is mostly avoided with the use of a modern
   word-processor-like HTML editor. As a specific example, the open
   source HTML editor Kompozer is discussed.

The chapter does allow you to understand the overall interaction
between a browser (like Firefox on your local machine) and a web
server and to create dynamic web content with Python. We treat
interaction with the web basically as a mechanism to get input into
a Python program and data back out and displayed. Web pages
displayed in your browser are used for both the input and the
output. The advantage of a public server is that it can also be
used to store data accessible to people all over the world.

There are a number of steps in the development in this chapter, so
I start with an overview:

#. A few bits about the basic format of *hypertext markup language*
   are useful to start.

#. The simplest pages to start writing in Kompozer are just
   *static web pages*, formatted like a word-processing document.

#. Next we look at pages generated *dynamically*. An easy way to
   accomplish this is to create specialized static pages to act as
   templates into which the dynamic data is easily embedded. Web page
   creation can be tested totally locally, by creating HTML files and
   pointing your web browser to them. Initially we supply input data
   by our traditional means (keyboard input or function parameters),
   and concentrate on having our Python program *convert* the input to
   the desired output, and *display* this output in a web page.

#. We generate data from within a web page, using web forms
   (generated via Kompozer). Initially we will test web forms by
   automatically dumping their raw data.

#. To fully integrate a browser and server, we 

   #. use web forms to provide data

   #. use a Python program specified on the server called a *CGI script* to
      transform the input data into the desired output

   #. embed the output in a new dynamic web page that gets sent back to your
      browser. This Python server program transforms the input data, and
      generates output web pages much like we did in step 3, above.

#. Finally, if you set up a GoogleApp account, or have access to another
   server, you can upload and show off your work on your own
   personal web site, accessible to everyone on the Internet.
   (Modifications needed are not covered in this Tutorial.)
