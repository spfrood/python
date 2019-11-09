#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1996</h3>
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # create a list to store the data that is pulled from the html file
  names = []
  
  # open the HTML file to parse for the desired data
  fil = open(filename, 'rU')
  htmlfile = fil.read()
  
  # get the year using re.search to match the context around the year
  name_year = re.search(r'Popularity\sin\s(\d\d\d\d)', htmlfile)
  # above - r is raw data, looking for the regular expression 'Popularity in '
  # then puts the date into a group by putting in parenthesis (\d\d\d\d)   
  # \s is searching for a whitespace. \d is looking for a decimal number 0-9
  if not name_year:
    #if no year is found return an error message
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)
  year = name_year.group(1)
  names.append(year)
  
  name_tuples = []
  name_tuples = re.findall(r'<td>([\d]+)</td><td>([\w]+)</td><td>([\w]+)</td>', htmlfile)
  
  temp_names = []
  for item in name_tuples:
    temp_names.append((item[1] + ' ' + item[0]))
    temp_names.append((item[2] + ' ' + item[0]))
  
  # alphabetize the list according to names
  temp_names = (sorted(temp_names[1:]))
  for item in temp_names:
    names.append(item)
  
#  for item in names:
#    if isinstance(item, tuple):
#      print item[0] + ' ' + str(item[1])
#    else:
#      print item
#  above is no longer necessary since the temp_names is no longer tuples but rather just a list of strings

  fil.close()
  return names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    final_names = extract_names(filename)
    names_as_text = '\n'.join(final_names)
    if summary:
      filout = open(filename + ".summary", 'w')
      filout.write(names_as_text + '\n')
      filout.close()
    else:
      print names_as_text
    
  
if __name__ == '__main__':
  main()
