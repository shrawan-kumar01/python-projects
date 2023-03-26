# import all the liberary
#Importing all the necessary libraries to form the alarm clock:

from tkinter import *
import datetime
import time
from tkinter import font
import winsound


# creating a while loop which take arg as time 

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("the set date is :~ ",date)
        print(now)
        if now == set_alarm_timer:
            print("tuime to weak up \n ")
winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            # break

def actual_time():
    set_alarm_timer = f"{hour.get()} : {min.get()} :{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()

clock.title("data flayer alarm clock")
clock.geometry("400 x 200")
time_formate = label(clock , text = "enter tiome in 24 hr formate",fg = "red",bg = "black",font = "Arial").place(x=60,y=120)

addTime = label(clock,text= "hour , min , sec",font = 60).place(x = 110)

setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)
clock.mainloop()
#Execution of the window.

















            
