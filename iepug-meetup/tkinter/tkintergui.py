
# from tkinter import *

import tkinter as tk
root = tk.Tk()

# Set title of the GUI window
root.title ('Greetings App')

# Set size of GUI in pixels (width x height)
root.geometry('350x250') 

# Tkinter supports 15 widgets. Widgets provide controls to integrate with the GUI

# Label - Allows you to display text or an image on the screen
default_value = tk.StringVar()
default_value.set('????')
first_name_label = tk.Label(root, text='What\'s your name?').pack()
first_name = tk.Entry(root, textvariable=default_value).pack()
button = tk.Button(text='Click Me!', command = greeting).pack()

tk.mainloop()

# Look up attributes of Tkinter label widgets.


def greeting():
  greetings = tk.Label(root, bg ='tan', borderwidth=3.5, relief=groove', text="Hello {}, welcome to the wonderful world of programming!"



