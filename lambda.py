from tkinter import *
import math

gui = Tk()

gui.title("calculator")

entry = StringVar()
exp = ""


def press(num):
    global exp
    exp = exp + str(num)
    entry.set(exp)


def Clear():
    global exp
    exp = ""
    entry.set("")


def Equal():
    try:
        global exp
        sumof = str(eval(exp))
        entry.set(sumof)
        exp = ""

    except:
        entry.set("error ")
        exp = ""


def root():
    try:
        global exp
        value = math.sqrt(float(exp))
        entry.set(value)
        exp = ""

    except:
        entry.set(' sqrt(0) ')
        exp = ""


def log():
    try:
        global exp

        rslt = math.log(float(exp))
        entry.set(rslt)
        exp = ""

    except:
        entry.set("error",)
        exp = ""


display = Entry(gui, font=('arial', 20, 'bold'), textvariable=entry, bd=30,
                insertwidth=4, insertbackground='tomato', bg="powder blue", fg="tomato" ,justify='right').grid(columnspan=3)
entry.set("enter num")

# top_line
bClear = Button(gui, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="C", bg="Honeydew3", command=Clear).grid(row=0, column=3)

btnPi = Button(gui, padx=13, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="π", bg="Honeydew3", command=lambda: press("3.1415")).grid(row=1,
                                                                               column=0),

btnRoot = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="√", bg="Honeydew3", command=root).grid(row=1, column=1)

btnper = Button(gui, padx=15, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="%", bg="Honeydew3", command=lambda: press("/100")).grid(row=1, column=2)

btnDiv = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="/", bg="Honeydew3", command=lambda: press("/")).grid(row=1, column=3)

# second_line

btn7 = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", command=lambda: press(7)).grid(row=2, column=0)

btn8 = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", command=lambda: press(8)).grid(row=2, column=1)

btn9 = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", command=lambda: press(9)).grid(row=2, column=2)

btnMulti = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="*", bg="Honeydew3", command=lambda: press("*")).grid(row=2, column=3)

# third_line

btn4 = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", command=lambda: press(4)).grid(row=3, column=0)

btn5 = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", command=lambda: press(5)).grid(row=3, column=1)

btn6 = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", command=lambda: press(6)).grid(row=3, column=2)

btnSub = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="-", bg="Honeydew3", command=lambda: press("-")).grid(row=3, column=3)

# 4th line

btn1 = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", command=lambda: press(1)).grid(row=4, column=0)

btn2 = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", command=lambda: press(2)).grid(row=4, column=1)

btn3 = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", command=lambda: press(3)).grid(row=4, column=2)

btnAdd = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="+", bg="Honeydew3", command=lambda: press("+")).grid(row=4, column=3)

# Bottom line
btnDot = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text=".", bg="Honeydew3", command=lambda: press(".")).grid(row=5, column=0)

btnZero = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="0", command=lambda: press(0)).grid(row=5, column=1)

# btnPlusMinus=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
#                text="+/-",bg="Honeydew3").grid(row=5,column=2)
btnlog = Button(gui, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="log", bg="Honeydew3", command=lambda: log()).grid(row=5, column=2)

btnEquals = Button(gui, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                   text="=", bg="tomato", command=Equal).grid(row=5, column=3)

gui.mainloop()
