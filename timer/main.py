from playsound import playsound
import threading
import time
from tkinter import *
from tkinter import messagebox
import random


ecran = Tk()

ecran.title('Countdown Timer')
ecran.geometry("500x300")
ecran.configure(background='black')

ecran.columnconfigure(0, weight=1)
ecran.columnconfigure(6, weight=1)

ecran.rowconfigure(0, weight=1)  # inceput
ecran.rowconfigure(1, weight=3)  # titlu
ecran.rowconfigure(2, weight=1)  # spatiu
ecran.rowconfigure(3, weight=1)  # inputs
ecran.rowconfigure(4, weight=1)  # labels
ecran.rowconfigure(5, weight=3)  # spatiu
ecran.rowconfigure(6, weight=1)  # buton
ecran.rowconfigure(8, weight=4)  # final

titlu = Label(ecran, text="Countdown Timer", bg="black", fg="white")
titlu.config(font=("Goudy Stout", 11, "bold"))
titlu.grid(row=1, column=3)

hoursLabel = Label(ecran, text="Hours", bg="black", fg="white")
hoursLabel.grid(row=4, column=1)
hoursLabel.config(font=("Arial", 11, "bold"))

minutesLabel = Label(ecran, text="Minutes", bg="black", fg="white")
minutesLabel.grid(row=4, column=3)
minutesLabel.config(font=("Arial", 11, "bold"))

secondsLabel = Label(ecran, text="Seconds", bg="black", fg="white")
secondsLabel.grid(row=4, column=5)
secondsLabel.config(font=("Arial", 11, "bold"))

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

hoursEntry = Entry(ecran, width=4, font=("Arial", 20, "bold"), textvariable=hours)
minutesEntry = Entry(ecran, width=4, font=("Arial", 20, "bold"), textvariable=minutes)
secondsEntry = Entry(ecran, width=4, font=("Arial", 20, "bold"), textvariable=seconds)

hoursEntry.grid(row=3, column=1)
minutesEntry.grid(row=3, column=3)
secondsEntry.grid(row=3, column=5)

hours.set("0")
minutes.set("0")
seconds.set("0")

checkRESET = 0
checkPAUSE = 0


def startCountdown():
    global checkRESET
    checkRESET = 0

    global checkPAUSE
    checkPAUSE = 0

    total_time_in_seconds = -1

    try:
        if int(hours.get()) >= 0 and int(minutes.get()) >= 0 and int(seconds.get()) >= 0:
            total_time_in_seconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
            hoursEntry.config(state='disabled')
            minutesEntry.config(state='disabled')
            secondsEntry.config(state='disabled')
        else:
            messagebox.showwarning('Error', 'Invalid input')
            hours.set("0")
            minutes.set("0")
            seconds.set("0")


    except:
        messagebox.showwarning('Error', 'Invalid input')
        hours.set("0")
        minutes.set("0")
        seconds.set("0")

    while total_time_in_seconds > -1 and checkRESET == 0 and checkPAUSE == 0:

        m = total_time_in_seconds // 60

        s = total_time_in_seconds % 60

        h = 0
        if m > 60:
            h = m // 60
            m = m % 60


        hours.set(str(h))
        minutes.set(str(m))
        seconds.set(str(s))

        ecran.update()
        time.sleep(1)

        if total_time_in_seconds == 0:
            threading.Thread(target=playsound, args=('bell.mp3',)).start()
            messagebox.showinfo("Finish", "Time is up")

            hours.set("0")
            minutes.set("0")
            seconds.set("0")
            hoursEntry.config(state='normal')
            minutesEntry.config(state='normal')
            secondsEntry.config(state='normal')

        total_time_in_seconds -= 1


def resetCountdown():
    global checkRESET
    checkRESET = 1
    hours.set("0")
    minutes.set("0")
    seconds.set("0")
    hoursEntry.config(state='normal')
    minutesEntry.config(state='normal')
    secondsEntry.config(state='normal')


def pauseCountdown():
    global checkPAUSE
    checkPAUSE = 1

def lucky():

    ore=random.randint(0,60)
    minute=random.randint(0,60)
    secunde=random.randint(0,60)
    hours.set(str(ore))
    minutes.set(str(minute))
    seconds.set(str(secunde))



start = Button(ecran, text='START \nCOUNTDOWN', command=startCountdown, bd=8, bg="white",cursor="hand2")

start.grid(row=6, column=3)
start.config(font=("Arial", 8, "bold"))


reset = Button(ecran, text='RESET \nCOUNTDOWN', command=resetCountdown, bd=8, bg="white",cursor="hand2")
reset.grid(row=6, column=1)
reset.config(font=("Arial", 8, "bold"))


pause = Button(ecran, text='PAUSE \nCOUNTDOWN', command=pauseCountdown, bd=8, bg="white",cursor="hand2")
pause.grid(row=6, column=5)
pause.config(font=("Arial", 8, "bold"))

lucky = Button(ecran, text='LUCKY \nCOUNTDOWN', command=lucky, bd=8, bg="white",cursor="hand2")
lucky.grid(row=7, column=5)
lucky.config(font=("Arial", 8, "bold"))

ecran.mainloop()
