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

from tkinter import *
import tkMessageBox
import time

import sys
# import multiprocessing
from multiprocessing import Process, Pipe
# import threading


class WW:
    '''

    '''
    def __init__(self):
        self.c1, self.c2 = Pipe()


    # def manual_check():
    #     often_value = often.get()
    #     phone_number = num.get()
    #     print often_value
    #     print phone_number
    #     try:
    #         return int(often_value)
    #     except ValueError:
    #         tkMessageBox.showinfo("Error", "Entry value must be a number")

    # def continuous_check():
    #     often_value = often.get()
    #     phone_number = num.get()

    #     p1 = Process(target=recurring_run, args=(often_value, phone_number,))
    #     p1.start()

    def recurring_run(self, often_value, phone_number):
        print often_value
        print phone_number
        for i in range(10):
            print("abc")
            sys.stdout.flush()
            time.sleep(2)
            if self.c2.poll() and self.c2.recv() == "KILL":
                # exit()
                break
        try:
            return int(often_value)
        except ValueError:
            tkMessageBox.showinfo("Error", "Entry value must be a number")

    def close_out(self):
        self.c1.send("KILL")
        print("Close out worked")
        exit()
    
    '''

    '''
def weather_widget():


    ww = WW()

    def continuous_check():
        often_value = often.get()
        phone_number = num.get()

        p1 = Process(target=ww.recurring_run, args=(often_value, phone_number,))
        p1.start()
    
    # def close_out(self):
    #     self.c1.send("KILL")
    #     print("Close out worked")

    def manual_check():
        often_value = often.get()
        phone_number = num.get()
        print often_value
        print phone_number
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

    # Adds in the various parts of the left pane
    var = StringVar()
    intro_message = ("This window will allow you to run The Umbrella Project:\n"
        + "A program that will check the weather every so often and send "
        + "you text alerts to tell you when it starts and stops raining")
    intro = Label(left, textvariable=var, wraplength=190, pady=2)
    var.set(intro_message)
    intro.pack()

    p_num_label = ("What phone number should alerts be sent to?")
    p_num = Label(left, text=p_num_label, wraplength=190)
    p_num.pack()
    num = Entry(left, bd=5)
    num.pack()

    spacer = Label(left, text=" ", wraplength=190)
    spacer.pack()

    exit_button = Button(left, text = "Quit", command = ww.close_out, height=50)
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
    recurance = Label(top_right, text=recurance_label, wraplength=190)
    recurance.pack()
    often = Entry(top_right, bd=5)
    often.pack()
    run_button = Button(top_right, text = "Run", command = continuous_check)
    run_button.pack()

    # Makes the bottom part of the right pane
    bottom_right_pane = PanedWindow(right_pane, orient=VERTICAL, relief=RAISED, height=110, width=200)
    right_pane.add(bottom_right_pane)
    bottom_right = LabelFrame(bottom_right_pane, text="Current Weather Check")
    bottom_right_pane.add(bottom_right)

    # Adds in the various parts of the bottom right pane
    instant_label = ("Manually run the weather checker to see if it is currently raining\n")
    instant = Label(bottom_right, text=instant_label, wraplength=190)
    instant.pack()
    check_button = Button(bottom_right, text = "Check now", command = manual_check)
    check_button.pack()
    
    mainloop()


if __name__ == "__main__":
    weather_widget()
    # c1, c2 = Pipe()
    # p1=Process(target=recurring_run, args=(15, 16, c2))
    # p1.start()
    # time.sleep(5)
    # close_out()




