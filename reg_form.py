from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter
import tkinter.messagebox


window = Tk()
window.title("Registration Screen")
window.geometry('300x300')
window.configure(background = "azure");



Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 1,column = 0)
Email_Id = Label(window ,text = "Email-Id").grid(row = 2,column = 0)
Mobile_Number = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
Address = Label(window ,text = "Address: ").grid(row = 4,column =0)
tkinter.messagebox.showinfo("Alert Message", "This is just a alert message!")


Firstname = Entry(window).grid(row = 0,column = 1)
Lastname = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile = Entry(window).grid(row = 3,column = 1)
Address = Entry(window).grid(row = 4,column = 1)
tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2)
response = tkinter.messagebox.askquestion("Tricky Question", "Does this Work?")
if response == 1:
    tkinter.Label(window, text = "Yes").pack()
else:
    tkinter.Label(window, text = "No").pack()

    
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
    
btn = ttk.Button(window ,text="Submit").grid(row=100,column=36)
window.mainloop()
