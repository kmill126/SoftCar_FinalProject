from bs4 import BeautifulSoup
import requests
import datetime
import time

finish = True
i = 0

while finish:
    datetime.datetime.now()
    datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
    a = str(datetime.datetime.now())

    webpage = "https://weather.com/weather/today/l/21218:4:US"
    r = requests.get(webpage)
    soup = str(BeautifulSoup(r.text))
    looking_for = 'class="today_nowcard-phrase"'
    new_stuff = soup.split(looking_for)
    new_new_stuff = new_stuff[1].split("/")

    with open("Weather_Tracking.txt", 'a') as recording:
        recording.write("\n%s" % a)
        recording.write(" %s" % new_new_stuff[0])

    time.sleep(900)

    i = i + 1
    if i == 96:
        finish = False
        break

print("DONE")