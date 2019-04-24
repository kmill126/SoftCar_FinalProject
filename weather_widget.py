'''
The Umbrella Project, final project for Software Carpentry
Authors: Josh Cole and Katherine Miller
Date & Time Due: 4/29/19 11:59 pm

More to be written

**Functions**
    Needs to be written

**Classes**
    WW
        *Functions*
            recurring_run
                Checks weather/sends messages in defined time frame
            close_out
                Stops the recurring run
'''

from tkinter import *
from tkinter import messagebox
import time
import smtplib
import sys
from multiprocessing import Process, Pipe
from bs4 import BeautifulSoup
import requests
import datetime

class WW:
    '''
    This is an object that holds pipes for two functions to
    communicate, and the functions that run and stop a continuous
    weather check.
    '''
    def __init__(self):
        '''
        This initializes the process pipes that allow the 
        functions to communicate
        '''
        self.c1, self.c2 = Pipe()

    def recurring_run(self, often_value, phone_number):
        '''
        Checks the weather in a continuous loop that runs
        on a defined time interval and is stopped by the
        close_out function. Is triggered as a process by
        the continuous_check function in the weather_widget

        **Parameters**
            self: *object*
                This WW object instance
            often_value: *int*
                The number of minutes for how often the function
                will check the weather
            phone_number: *str*
                The 10 digit phone number with attached carrier @ tag
                to send the alert to. Ex. 1234567890@mms.att.net
        '''

        # Starts checking the weather at a given time interval
        i = 0
        mode = "Umbrella"
        while True:
            if i % (often_value * 60) == 0:
                weather = grab_baltimore_weather()
                
                # If some form of rain is happening, and previously wasn't then alert
                if "Rain" in weather or "Shower" in weather \
                        or "Storm" in weather or "Snow" in weather \
                        or "Sleet" in weather or "storm" in weather:
                    if mode == "Clear":
                        alert = ("Precipitation currently occuring\n"
                            + "Umbrella highly advised")
                        mode = "Umbrella"

                        #Sends a text message containing the above alert
                        server = smtplib.SMTP( "smtp.gmail.com", 587 )
                        server.starttls()
                        server.login( 'SoftwareCarpentry1@gmail.com', 'SoftCar1')
                        server.sendmail( 'SoftwareCarpentry1', phone_number, alert)

                # If not some form of rain, and previously was then alert
                else:
                    if mode == "Umbrella":
                        alert = ("Weather has cleared\n"
                            + "Umbrella no longer necessary")
                        mode = "Clear"

                        #Sends a text message containing the above alert
                        server = smtplib.SMTP( "smtp.gmail.com", 587 )
                        server.starttls()
                        server.login( 'SoftwareCarpentry1@gmail.com', 'SoftCar1')
                        server.sendmail( 'SoftwareCarpentry1', phone_number, alert)

            # Checks if the weather checking loop should be stopped
            if self.c2.poll() and self.c2.recv() == "KILL":
                messagebox.showinfo("Recurring Weather Checker", 
                    "Your phone is successfully unpaired")
                break

            time.sleep(2)
            i += 2

    def close_out(self):
        '''
        Stops the continuous loop that is running from the
        recurring_run function and creates a confirmation pop up.
        Is triggered by the exit_button in the weather_widget.

        **Parameters**
            self: *object*
                This WW object instance

        **Returns**
            None
        '''
        self.c1.send("KILL")
        # exit()

def grab_baltimore_weather():
    '''
    Searches the website "https://weather.com/weather/today/l/21218:4:US"
    for the current weather conditions and returns that

    **Parameters**
        None

    **Returns**
        weather: *str*
            The current weather acording to the website contained in > <
            Example: >Light Rain<
    '''

    webpage = "https://weather.com/weather/today/l/21218:4:US"
    data = requests.get(webpage)
    soup = str(BeautifulSoup(data.text, features='lxml'))
    looking_for = 'class="today_nowcard-phrase"'
    chopped_text = soup.split(looking_for)
    start_is_weather = chopped_text[1].split("/")
    weather = start_is_weather[0]

    return weather

def weather_widget():
    '''
    Starts a user interface window that can be used to check the
    current weather, or have a text sent to you when it starts
    or stops raining

    **Parameters**
        None, but some things are user input in the user interface

    **Returns**
        None, but will create pop up messages and send text messages
    '''

    ww = WW()

    def continuous_check():
        '''
        Makes sure that user inputs to the user interface are in the
        correct form, and if so starts the recurring_run as a process
        in the background. If they are incorrect, then creates pop up
        error messages telling user how inputs should be entered
        
        **Parameters**
            None, but some things are user input in the interface

        **Returns**
            None, but will create pop up messages
        '''

        check1 = False
        check2 = False
        
        #Check for correct input of how often to run
        try:
            often_value = int(often.get())
            check1 = True

            #Checks for correct input of phone number and carrier
            try:
                phone_number = str(num.get()) + str(carrier.get())
                server = smtplib.SMTP( "smtp.gmail.com", 587 )
                server.starttls()
                server.login( 'SoftwareCarpentry1@gmail.com', 'SoftCar1')
                test_msg = "Your phone is successfully paired!"
                server.sendmail( 'SoftwareCarpentry1', phone_number, test_msg)

                answer = messagebox.askyesno("Phone Pairing", 
                    "Did you recieve a pairing message?\n\n"
                    + "Please note, this may take a few seconds.")
                if answer == True:
                    check2 = True
                else:
                    messagebox.showinfo("Error", 
                        "Please check that your phone number is 10 digits "
                        + "(no dashes) and the correct carrier "
                        + "has been selected and try again.")
            except:
                messagebox.showinfo("Error", 
                    "Please check that your phone number is 10 digits "
                    + "(no dashes) and the correct carrier "
                    + "has been selected and try again.")
            
        except ValueError:
            messagebox.showinfo("Error", "Entry value must be a number")

        # If both inputs are correct and user indicates phone has been 
        # successfully connected to, then starts the process of the
        # recurring_run function
        if check1 and check2:
            p1 = Process(target=ww.recurring_run, args=(often_value, phone_number))
            p1.start()
    
    def manual_check():
        '''
        Checks the current weather and creates a pop up message stating it

        **Parameters**
            None

        **Returns**
            None, but will create a pop up message
        '''
        weather = grab_baltimore_weather()
        messagebox.showinfo("Current Weather", "The weather outside is:\n\n"
            + weather)

    
    ##############################################################################  
    #                 Creation of the User Interface Window                      #
    ##############################################################################

    # Creates the overall window
    master = PanedWindow()
    master.pack(fill=BOTH, expand=2)

    # Makes the left pane
    left_pane = PanedWindow(master, orient=VERTICAL, relief=RAISED, height=230, width=200)
    master.add(left_pane)
    left = LabelFrame(left_pane, text=" The Umbrella Project")
    left_pane.add(left)

    # Adds in the various parts of the left pane
    var = StringVar()
    intro_message = ("This window will allow you to run The Umbrella Project:\n"
        + "A program that will check Baltimore's weather every so often and send "
        + "you text alerts to tell you when it starts and stops raining")
    intro = Label(left, textvariable=var, wraplength=190, pady=2)
    var.set(intro_message)
    intro.pack()

    p_num_label = ("What phone number should alerts be sent to?")
    p_num = Label(left, text=p_num_label, wraplength=190)
    p_num.pack()
    num = Entry(left, bd=5)
    num.pack()

    spacer = Label(left, text="Select carrier: ", width=200, anchor=W)
    spacer.pack()

    carrier = StringVar()
    carrier1 = Radiobutton(left, text = "AT&T", variable=carrier, value="@mms.att.net")
    carrier1.pack(side=LEFT)
    carrier2 = Radiobutton(left, text = "T-Mobile", variable=carrier, value="@tmomail.net")
    carrier2.pack(side=LEFT)
    carrier3 = Radiobutton(left, text = "Verizon", variable=carrier, value="@vtext.com")
    carrier3.pack(side=RIGHT)

    # Makes the right pane
    right_pane = PanedWindow(master, orient=VERTICAL, relief=RAISED, height=230, width=200)
    master.add(right_pane)

    # Makes the top part of the right pane
    top_right_pane = PanedWindow(right_pane, orient=VERTICAL, relief=RAISED, height=160, width=200)
    right_pane.add(top_right_pane)
    top_right = LabelFrame(top_right_pane, text="Recurring Weather Checker")
    top_right_pane.add(top_right)

    # Adds in the various parts of the top right pane
    recurance_label = ("How often (in minutes) would you like to check the weather?")
    recurance = Label(top_right, text=recurance_label, wraplength=190)
    recurance.pack()
    often = Entry(top_right, bd=5)
    often.pack()
    warning_message = ("*If you do not press stop before closing, "
        + "The Umbrella Project will continue running in the background")
    warning = Label(top_right, text=warning_message, width=200, wraplength=205)
    warning.pack(side=BOTTOM)
    run_button = Button(top_right, text = "Run", command = continuous_check, width=12)
    run_button.pack(side=LEFT)
    exit_button = Button(top_right, text = "Stop", command = ww.close_out, width = 12)
    exit_button.pack(side=RIGHT)

    # Makes the bottom part of the right pane
    bottom_right_pane = PanedWindow(right_pane, orient=VERTICAL, relief=RAISED, height=70, width=200)
    right_pane.add(bottom_right_pane)
    bottom_right = LabelFrame(bottom_right_pane, text="Current Weather Check")
    bottom_right_pane.add(bottom_right)

    # Adds in the various parts of the bottom right pane
    instant_label = ("Manually run the weather checker")
    instant = Label(bottom_right, text=instant_label, wraplength=190)
    instant.pack()
    check_button = Button(bottom_right, text = "Check now", command = manual_check)
    check_button.pack()
    
    mainloop()


if __name__ == "__main__":
    weather_widget()