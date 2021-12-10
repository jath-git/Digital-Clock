# global imports
from tkinter import *
from tkinter.ttk import *
from Time import Time
from datetime import datetime

# get current time
now = datetime.now()

# initialize time object
time = Time(int(now.strftime('%H')), int(now.strftime('%M')),
            int(now.strftime('%S')), now.strftime('%p'))

# initialize tkinker and display
root = Tk()
root.title('Clock')
label = Label(font=('', 80))
label.pack(anchor='center')

# make integer have 2 digits
# assumes that 0 <= number < 100 and number is integer


def padInteger(number):
    return str(number) if number > 9 else f'0{str(number)}'

# display time in label


def updateTime():
    label.config(
        text=f'{padInteger(time.hour)}:{padInteger(time.minute)}:{padInteger(time.second)} {time.midday}')
    time.nextSecond()
    label.after(1000, updateTime)


# repeadedly update time every second
updateTime()
mainloop()
