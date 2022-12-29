from tkinter import *
from tkinter import messagebox
import sys
window = Tk()
s = ""

window.title('Calculator 2023')
def press(key):
    global s, screen_value
    s+=str(key)
    screen_value.set(s)

def calc():
    global s
    try:
        s = str(eval(s))
        screen_value.set(s)
    except ZeroDivisionError as err:
        messagebox.showerror(title='Calculator',message=str(err))
    except SyntaxError as err2:
        messagebox.showerror(title='Calculator', message=str(err2))

def delete():
    global s , screen_value
    s = ""
    screen_value.set("")
screen_value = StringVar()
window.config(bg='grey')
screen = Label(master=window, bg="white", width=15, font=("Ariel", 35), textvariable=screen_value)
screen.pack()
frame = Frame(window,bg="grey")
frame.pack()

num1 = Button(frame, text=1, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(1))
num1.grid(row=0, column=0)

num2 = Button(frame, text=2, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(2))
num2.grid(row=0, column=1)

num3 = Button(frame, text=3, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(3))
num3.grid(row=0, column=2)

num4 = Button(frame, text=4, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(4))
num4.grid(row=1, column=0)

num5 = Button(frame, text=5, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(5))
num5.grid(row=1, column=1)

num6 = Button(frame, text=6, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(6))
num6.grid(row=1, column=2)

num7 = Button(frame, text=7, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(7))
num7.grid(row=2, column=0)

num8 = Button(frame, text=8, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(8))
num8.grid(row=2, column=1)

num9 = Button(frame, text=9, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(9))
num9.grid(row=2, column=2)

num0 = Button(frame, text=0, width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press(0))
num0.grid(row=2, column=3)

equal = Button(frame, text="=", width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=calc)
equal.grid(row=2, column=4)

time = Button(frame, text="*", width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press("*"))
time.grid(row=1, column=3)

plus = Button(frame, text="+", width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press("+"))
plus.grid(row=1, column=4)

minus = Button(frame, text="-", width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press("-"))
minus.grid(row=0, column=3)

divide = Button(frame, text="/", width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey",command=lambda:press("/"))
divide.grid(row=0, column=4)

point = Button(frame, text=".", width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey", command=lambda:press("."))
point.grid(row=3, column=1)

clear = Button(frame, text="Clear", width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey", command=delete)
clear.grid(row=3, column=3)

quitting = Button(frame, text="Exit", width=10, height=4, font=("Ariel", 10, "bold"), bg="light grey", command=sys.exit)
quitting.grid(row=3, column=2)
window.mainloop()
