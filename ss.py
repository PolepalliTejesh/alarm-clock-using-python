import datetime
from playsound import playsound


alarmhour=int(input("enter hour:"))
alarmmin=int(input("enter minutes:"))
alarmAm=input("am/pm:")

if alarmAm=="pm":
    alarmhour+=12

while True:

    if alarmhour==datetime.datetime.now().hour and alarmmin==datetime.datetime.now().minute:
        print("playing....")
        playsound("punky.mp3")
        break