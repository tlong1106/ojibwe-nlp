# from tkinter import *

# create the application window
# app = Tk()

# >> add single label to application window
# label = Label(app,text="this is a label")

# >> add multiple labels to application window
# Label(app,text="this is label one").grid(row=0)
# Label(app,text="this is label two").grid(row=1)
# entry_one = Entry(app)
# entry_two = Entry(app)
# entry_one.grid(row=0,column=1)
# entry_two.grid(row=1,column=1)

# >> add a button to application window
# button = Button(app,text="close application",width=25,command=app.destroy)
# button.pack()

# >> add check box to application window
# var1 = IntVar()
# Checkbutton(app,text="option 1",variable=var1).grid(row=0,sticky=W)
# var2 = IntVar()
# Checkbutton(app,text="option 2",variable=var2).grid(row=1,sticky=W)

# >> add radio button to application window
# var = IntVar()
# Radiobutton(app,text="option 1",variable=var,value=1).pack(anchor=W)
# Radiobutton(app,text="option 2",variable=var,value=2).pack(anchor=W)

# >> add list box to application window
# listBox = Listbox(app)
# listBox.insert(1,"option 1")
# listBox.insert(2,"option 2")
# listBox.insert(3,"option 3")
# listBox.pack()

# >> add scroll bar to application window
# scrollBar = Scrollbar(app)
# scrollBar.pack(side=RIGHT,fill=Y)
# myList = Listbox(app,yscrollcommand=scrollBar.set)
# for line in range(1,11):
#     myList.insert(END,"this is line number "+str(line))
# myList.pack(side=LEFT,fill=BOTH)
# scrollBar.config(command=myList.yview)

# >> add menu to application window
# menu = Menu(app)
# app.config(menu=menu)
# fileMenu = Menu(menu)
# menu.add_cascade(label="file",menu=fileMenu)
# fileMenu.add_command(label="new")
# fileMenu.add_command(label="open")
# fileMenu.add_separator()
# fileMenu.add_command(label="exit",command=app.quit)
# helpMenu = Menu(menu)
# menu.add_cascade(label="help",menu=helpMenu)
# helpMenu.add_command(label="about")

# >> add top level to application: this creates a pop-up window
# app.title("top level")
# top = Toplevel()
# top.title("top title")
# top.mainloop()

# >> add message to application
# ourMessage = "this is a long message. this is a long message. this is a long message. this is a long message. this is a long message. this is a long message."
# messageVar = Message(app,text=ourMessage)
# messageVar.config(bg="lightgreen")
# messageVar.pack()

# >> add menu button to application
# > > > this could be used to select multiple attributes: verb classe (vii, vai, vti, vta), tense, negation, etc.
# menuButton = Menubutton(app,text="top menu button")
# menuButton.grid()
# menuButton.menu = Menu(menuButton,tearoff=0)
# menuButton["menu"] = menuButton.menu
# cVar = IntVar()
# aVar = IntVar()
# menuButton.menu.add_checkbutton(label="contact",variable=cVar)
# menuButton.menu.add_checkbutton(label="about",variable=aVar)
# menuButton.pack()

# >> add progress bar to application
# import tkinter as tk
# from tkinter import ttk
# import time
# app = tk.Tk()
# app.title("this is a title")

# def start_progress():
#     for i in range(1,101):
#         time.sleep(0.005)
#         progress["value"] = i
#         app.update_idletasks()
#     progress.stop()

# # progressbar widget
# app.title("progress example")
# progress = ttk.Progressbar(app,orient="horizontal",length=300,mode="determinate")
# progress.pack(pady=20)

# # button to start progressbar
# startButton = tk.Button(app,text="start progress",command=start_progress)
# startButton.pack(pady=10)

# >> add spinbox to application
# spinBox = Spinbox(app,from_=0,to=10)
# spinBox.pack()

# >> add text to application
# > > > this could be used to display the explanation lines
# text = Text(app,height=2,width=30)
# text.pack()
# text.insert(END,"this is a\nmulti-line string")

# app.mainloop()



# ~ ~ ~ application starts here ~ ~ ~
from tkinter import *
import random

def random_verb():
    verbs = ["wiisini","bakade","giishkaabaagwe","minikwe"]
    verb_choice = random.choice(verbs)
    return verb_choice

def random_pronoun():
    pronouns = ["niin","giin","wiin"]
    pronoun_choice = random.choice(pronouns)
    return pronoun_choice

def random_tense():
    tenses = ["past","present","future deciderative"]
    tense_choice = random.choice(tenses)
    return tense_choice

def random_negation():
    negation = [True,False]
    negation_choice = random.choice(negation)
    if negation_choice == True:
        return "yes"
    else:
        return "no"
    
def user_input():
    user_response = input("conjugate verb for pronoun, tense, and negation: ")

app = Tk()
app.geometry("500x350")

# generate a random prompt for verb, pronoun, tense, and negation
verb_prompt = Label(app,text=f"verb: {random_verb()}",font=("Arial", 20))
pronoun_prompt = Label(app,text=f"pronoun: {random_pronoun()}",font=("Arial", 20))
tense_prompt = Label(app,text=f"tense: {random_tense()}",font=("Arial", 20))
negated_prompt = Label(app,text=f"negated? {random_negation()}",font=("Arial", 20))
verb_prompt.pack(anchor="w")
pronoun_prompt.pack(anchor="w")
tense_prompt.pack(anchor="w")
negated_prompt.pack(anchor="w")

# user input for conjugated verb according to prompt
entry = Entry(app, width=20,font=("Arial", 20))
entry.focus_set()
entry.pack(anchor="w",pady=20)
button = Button(app,text="submit",width=25)
button.pack(anchor="w",pady=20)
# button will prompt a comparison between user response and algorithm response

app.mainloop()