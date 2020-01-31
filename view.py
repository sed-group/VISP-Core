#!/usr/bin/env python
import controller
from configurations import *
from guizero import App, Box, Text, TextBox, PushButton, ListBox, MenuBar

class View():

    def __init__(self):
        pass

needs = ['one','two','three']


def say_hello():
    '''
    Changes the value of "text" to "hello world"
    '''
    text.value = "hello world"

def new_file_function():
    app.info("Create new something", "Not yet implemented.")

def open_file_function():
    file = app.select_file(title="Select file", folder=".", filetypes=[["All files", "*.*"]], save=False)
    print("File selected: {}".format(file))

def save_file_function():
    file = app.select_file(title="Select file", folder=".", filetypes=[["All files", "*.*"]], save=True)
    print("File saved as: {}".format(file))

def edit_function():
    print("Edit option")

def about_function():
    app.info("About", "This is a prototype of a GUI for the SED group.")

def destroy_app():
    if app.yesno("Closing the app", "Are you sure you want to exit the app?"):
        print("Closing the app")
        app.destroy()

def select_alternative(value):
    text.value = value

app = App(title="Example", height=400, width=600)
app.when_closed = destroy_app

menubar = MenuBar(app,
                  toplevel=["File", "Edit", "Help"],
                  options=[
                      [
                          ["Open", open_file_function], 
                          ["Save", save_file_function], 
                          ["Close", destroy_app] 
                      ],
                      [ 
                          ["Edit option 1", edit_function], 
                          ["Edit option 2", edit_function] 
                      ],
                      [ 
                          ["About", about_function]
                      ]
                  ])

toolbar_box = Box(app, width="fill", align="top")
toolbar_box.bg = "#ffffff"
new_button = PushButton(toolbar_box, command=new_file_function, align="left", text="New", image="./img/file.gif")
open_button = PushButton(toolbar_box, command=open_file_function, align="left", text="Open", image="./img/folder-open.gif")
save_button = PushButton(toolbar_box, command=save_file_function, align="left", text="Save", image="./img/content-save.gif")
calculate_button = PushButton(toolbar_box, command=say_hello, align="left", text="Calculate", image="./img/calculator.gif")
plot_button = PushButton(toolbar_box, command=say_hello, align="left", text="Plot", image="./img/chart-areaspline-variant.gif")

content_box = Box(app, align="top", width="fill", height="fill")
listbox = ListBox(
    content_box, 
    items=needs, 
    selected=None, 
    command=select_alternative,
    scrollbar=True,
    align="left",
    height="fill")
text = Text(content_box, text="This is a test")

form_box = Box(content_box, layout="grid", width="fill", align="top")
Text(form_box, grid=[0,0], text="form", align="right")
Text(form_box, grid=[0,1], text="label", align="left")
TextBox(form_box, grid=[1,1], text="data", width="fill")

status_box = Box(app, align="bottom", width="fill", height="20")
status_box.bg = "#ffffff"
status_text = Text(status_box, text="Status: All is fine", align="left")
status_text.text_size = 8

app.display()