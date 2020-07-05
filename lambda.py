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
        entry.set("error")
        exp = ""


normalFrame = Frame(gui)
normalFrame.pack()
display = Entry(normalFrame, font=('arial', 15, 'bold'), textvariable=entry, bd=20,
                insertwidth=4, insertbackground='tomato', bg="powder blue", fg="black", justify=RIGHT)
display.pack(side=TOP, pady=10, padx=10, fill=X)
# entry.set("enter num")

# top_line

btnFrame = Frame(gui)
btnFrame.pack()

bClear = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                text="C", bg="tomato", command=Clear).grid(row=0, column=0)

btnLefBrkt = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                 text="(", bg="Honeydew3", command=lambda : press("(")).grid(row=0, column=1)

btnRghtBrkt = Button(btnFrame, padx=15, bd=8, fg="black", font=('arial', 10, 'bold'),
                text=")", bg="Honeydew3", command=lambda: press(")")).grid(row=0, column=2)

btnDiv = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                text="/", bg="Honeydew3", command=lambda: press("/")).grid(row=0, column=3)

# second_line

btn7 = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="7", command=lambda: press(7)).grid(row=1, column=0)

btn8 = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="8", command=lambda: press(8)).grid(row=1, column=1)

btn9 = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="9", command=lambda: press(9)).grid(row=1, column=2)

btnMulti = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                  text="*", bg="Honeydew3", command=lambda: press("*")).grid(row=1, column=3)

# third_line

btn4 = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="4", command=lambda: press(4)).grid(row=2, column=0)

btn5 = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="5", command=lambda: press(5)).grid(row=2, column=1)

btn6 = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="6", command=lambda: press(6)).grid(row=2, column=2)

btnSub = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                text="-", bg="Honeydew3", command=lambda: press("-")).grid(row=2, column=3)

# 4th line

btn1 = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="1", command=lambda: press(1)).grid(row=4, column=0)

btn2 = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="2", command=lambda: press(2)).grid(row=4, column=1)

btn3 = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="3", command=lambda: press(3)).grid(row=4, column=2)

btnAdd = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                text="+", bg="Honeydew3", command=lambda: press("+")).grid(row=4, column=3)

# Bottom line
btnDot = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                text=".", bg="Honeydew3", command=lambda: press(".")).grid(row=5, column=0)

btnZero = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                 text="0", command=lambda: press(0)).grid(row=5, column=1)

# btnPlusMinus=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
#                text="+/-",bg="Honeydew3").grid(row=5,column=2)
btnlog = Button(btnFrame, padx=10, bd=8, fg="black", font=('arial', 10, 'bold'),
                text="log", bg="Honeydew3", command=lambda: log()).grid(row=5, column=2)

btnEquals = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),

                   text="=", bg="tomato", command=Equal).grid(row=5, column=3)

# Scientificmode

sFrame = Frame(gui)
#sFrame.config(padx=8)
normalMode = True


def scientific():
    global normalMode
    if normalMode:
        print(" show scntfc")
        sFrame.pack(side=TOP)
        btnFrame.pack(side=TOP)

        normalMode = False
    else:
        print(" showNormal")
        sFrame.pack_forget()

        normalMode = True


# firstrow

btnpi = Button(sFrame, padx=15, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
               text=" π ", command=lambda: press("* 3.1415")).grid(row=0, column=0)

btnpower = Button(sFrame, padx=10, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                  text=" x^ ", command=lambda: press(2)).grid(row=0, column=1)

btnFact = Button(sFrame, padx=14, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                 text=" x! ", command=lambda: press(3)).grid(row=0, column=2)

btnrad = Button(sFrame, padx=11, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text="rad", command=lambda: press(3)).grid(row=0, column=3)

# secondrow

btnsin = Button(sFrame, padx=10, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text="sinθ", command=lambda: press(3)).grid(row=1, column=0)

btnCos = Button(sFrame, padx=12, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text="cosθ", command=lambda: press(3)).grid(row=1, column=1)

btnTan = Button(sFrame, padx=12, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text="tanθ", command=lambda: press(3)).grid(row=1, column=2)
btnDeg = Button(sFrame, padx=11, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text="deg", command=lambda: press(3)).grid(row=1, column=3)

#thirdrow

btnLog = Button(sFrame, padx=10, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text=" log ", command=lambda: press(3)).grid(row=2, column=0)

btnRoot = Button(sFrame, padx=12, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text=" √x ", command=lambda: press(3)).grid(row=2, column=1)

btnExpo = Button(sFrame, padx=12, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text=" ℮x ", command=lambda: press(3)).grid(row=2, column=2)
btnPer = Button(sFrame, padx=11, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text=" %  ", command=lambda: press("/100")).grid(row=2, column=3)












# btnsin = Button(sFrame, bd=7, width=5, fg="black", font=('arial', 11, 'bold'),
#
#                 text="sinθ", bg="Honeydew3",  command=scientific).grid(row=0, column=0)
# btncos = Button(sFrame, padx=2.5, bd=7, fg="black", font=('arial', 11, 'bold'),
#
#                 text="cos∅", bg="Honeydew3", command=scientific).grid(row=0, column=1, ipadx=3)
# btntan = Button(sFrame, padx=2.5, bd=7,  fg="black", font=('arial', 11, 'bold'),
#
#                 text="tan∅", bg="Honeydew3", command=scientific).grid(row=0, column=2)
#
# btnPi = Button(sFrame, padx=2.5, bd=7, fg="black", font=('arial', 8, 'bold'),
#                text="π", bg="Honeydew3", command=lambda: press("3.1415")).grid(row=0,
#                                                                                column=3),
#
# btnpowr = Button(sFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
#                  text="^", bg="Honeydew3", command=scientific).grid(row=1, column=1)
#
# btnfact = Button(sFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
#                 text="!", bg="Honeydew3", command=scientific).grid(row=1, column=2)

# btnRad = Button(sFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
#                text="rad", bg="Honeydew3", command=lambda: press("3.1415")).grid(row=2,
#                                                                                   column=1),

# btnDeg = Button(sFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),

#               text="Deg", bg="Honeydew3", command=scientific).grid(row=1, column=0)

# btnpowr = Button(sFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),

# text="pow", bg="tomato", command=scientific).grid(row=1, column=1)


menubar = Menu(gui)
mod = Menu(menubar, tearoff=0)
mod.add_checkbutton(label="Scientific Calculator", command=scientific)

menubar.add_cascade(label="mode", menu=mod)
gui.configure(menu=menubar)

gui.mainloop()
