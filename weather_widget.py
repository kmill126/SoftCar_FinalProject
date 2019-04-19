# import Tkinter
# top = Tkinter.Tk()
# top.mainloop()
# export DISPLAY=0.0

# import tkinter as tk
# master = tk.Tk()
# whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
# msg = tk.Message(master, text = whatever_you_do)
# msg.config(bg='lightgreen', font=('times', 24, 'italic'))
# msg.pack()
# tk.mainloop()

# import Tkinter
# import tkMessageBox 
# tkMessageBox.showinfo("Title", "a Tk MessageBox")

# from tkinter import messagebox 
# messagebox.showinfo("Title", "a Tk MessageBox")

import tkinter as tk
from tkinter import *
import tkMessageBox
import time

def grab_often():
	often_value = often.get()
	try:
		return int(often_value)
	except ValueError:
		tkMessageBox.showinfo("Error", "Entry value must be a number")


# Creates the overall window
master = PanedWindow()
master.pack(fill=BOTH, expand=2)

# Makes the left pane
left_pane = PanedWindow(master, orient=VERTICAL, relief=RAISED, height=220, width=200)
master.add(left_pane)
left = LabelFrame(left_pane, text=" The Umbrella Project")
left_pane.add(left)

# Adds in the text of the intro to the left pane
var = StringVar()
intro_message = ("This window will allow you to run The Umbrella Project:\n"
	+ "A program that will check the weather every so often and send "
	+ "you text alerts to tell you when it starts and stops raining")
intro = Label(left, textvariable=var, wraplength=190, height=11)
var.set(intro_message)
intro.pack()

# Adds the exit button to the left pane
exit_button = Button(left, text = "Quit", command = exit, height=50)
exit_button.pack()

# Makes the right pane
right_pane = PanedWindow(master, orient=VERTICAL, relief=RAISED, height=220, width=200)
master.add(right_pane)

# Makes the top part of the right pane
top_right_pane = PanedWindow(right_pane, orient=VERTICAL, relief=RAISED, height=110, width=200)
right_pane.add(top_right_pane)
top_right = LabelFrame(top_right_pane, text="Recurring Weather Checker")
top_right_pane.add(top_right)

# Adds in the various parts of the top right pane
recurance_label = ("How often (in minutes) would you like to check the weather?")
recurance = Label(top_right, text=recurance_label, wraplength=200)
recurance.pack()
often = Entry(top_right, bd=5)
often.pack()
run_button = tk.Button(top_right, text = "Run", command = grab_often)
run_button.pack()

# Makes the bottom part of the right pane
bottom_right_pane = PanedWindow(right_pane, orient=VERTICAL, relief=RAISED, height=110, width=200)
right_pane.add(bottom_right_pane)
bottom_right = LabelFrame(bottom_right_pane, text="Current Weather Check")
bottom_right_pane.add(bottom_right)

# Adds in the various parts of the bottom right pane
instant_label = ("Manually run the weather checker to see if it is currently raining\n")
instant = Label(bottom_right, text=instant_label, wraplength=200)
instant.pack()
check_button = tk.Button(bottom_right, text = "Check now", command = grab_often)
check_button.pack()

mainloop()


# Might need to check that you can press button and run loop and while loop is running
# you can press a different button to do something else (here exit) might need to 
# do parallel stuff maybe

# Need to make sure weather runs in the background so you can access other widget pieces
# if name = main
# arg1 =
# arg2 = 
# etc
# p1 = Process(target= function_name, args=( , , ))
# p1.start()  this will run the thing in the background and continue the code onwards

