# SoftCar_FinalProject
The Umbrella Project by Josh Cole and Katherine Miller for the JHU WSE Software Carpentry Course Final Project

The Umbrella Project uses python to create a desktop application for checking the weather, from the website weather.com, in a given zipcode and creating alerts for it in one of two ways. The main application is to take the user's phone number and carrier and sending a text alert (to take your umbrella) whenever it starts raining and again when it stops (to let you know you don't need the umbrella anymore). The check is done every x minutes (where x is a user input value in order to control the frequency). A secondary application is to click a check now button that will give a pop up window on desktop for the current weather condition in the given zipcode.

To use this application all you will need is the **weather_widget.py** file, and you will need to run the function **weather_widget()**.
This will create a pop up window using tkinter from which you can run The Umbrella Project

weather_widget enterables:
- 5 digit US zipcode
- 10 digit US phone number (without dashes)
- carrier: 
- AT&T, T-Mobile, and Verizon are the options but other carriers could be incorporated into the code)
- number of minutes you would like the text alert functionality to check for rain

Required imports:
-
- from tkinter import *
- from tkinter import messagebox
- import time
- import smtplib
- import sys
- from multiprocessing import Process, Pipe
- from bs4 import BeautifulSoup
- import requests
