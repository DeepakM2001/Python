# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:48:47 2021

@author: Deepak Murugesan
"""

from tkinter import *
expression = " "
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expresion)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = " "
except:
        equation.set("error")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
if__name__ == "__main__";
    gui = Tk()
    gui.configure(background='light blue')
    gui.title("Calculator")
    gui.geometry("280x150")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    button1 = Button(gui, text="1")
