from tkinter import *
from datetime import date

root = Tk()
root.title('Getting started with Widgets')
root.geometry('400x300')

#add widgets & label
lbl = Label(text = "Hey there!", fg="white", bg="#072F5F", height=1, width=300)

#add label for getting name as user input
#add entry window to create a text box for ser to enter details
name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

#function to display message
def display():

    #read user input
    name = name_entry.get()

    #declaring global variable to make it accessible anywhere in the program
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello "+name+"\n"

    #display details in the text box
    #specify where to add details inside the text box 
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

#add text widget to display info/messages
text_box = Text(height=3)

#add button to give value of command as name of the function
#press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')


#organise al widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
