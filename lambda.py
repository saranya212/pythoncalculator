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


normalFrame = Frame(gui)
normalFrame.pack()
display = Entry(normalFrame, font=('arial', 15, 'bold'), textvariable=entry, bd=20,
                insertwidth=4, insertbackground='tomato', bg="powder blue", fg="black", justify=CENTER)
display.pack(side=TOP, pady=10, padx=10, fill=X)

# top_line

btnFrame = Frame(gui)
btnFrame.pack()

bClear = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                text="C", bg="tomato", command=Clear).grid(row=0, column=0)

btnLefBrkt = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
                    text="(", bg="Honeydew3", command=lambda: press("(")).grid(row=0, column=1)

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
btnPerc = Button(btnFrame, padx=10, bd=8, fg="black", font=('arial', 10, 'bold'),
                 text=" % ", bg="Honeydew3", command=lambda: press("/100")).grid(row=5, column=2)

btnEquals = Button(btnFrame, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),

                   text="=", bg="tomato", command=Equal).grid(row=5, column=3)

# Scientificmode

sFrame = Frame(gui)

normalMode = True


def printName(event):
    print("btn..")

    btn = event.widget
    text = btn['text']
    print(text)
    exp = entry.get()
    ans = ""

    if text == "  rad ":
        ans = math.radians(float(exp))


    elif text == "  deg ":
        ans = math.degrees(float(exp))

    elif text == " x  2 ":
        ans = float(exp) * float(exp)

    elif text == " x ! ":
        ans = math.factorial(float(exp))

    elif text == " sin ":

        ans = str(math.sin(math.radians(float(exp))))

    elif text == " cos ":

        ans = str(math.cos(math.radians(float(exp))))

    elif text == " tan ":
        ans = str(math.tan(math.radians(float(exp))))

    elif text == " log ":
        ans = math.log(float(exp))

    elif text == " √ x ":
        ans = math.sqrt(float(exp))


    elif text == " ℮x ":
        try:
            ans = math.exp(float(exp))
        except:
            ans = display.set(math.pi)

    elif text == " π ":
        ans = int(exp) * math.pi

    elif text == " mod ":
        ans = math.modf(float(exp))

    display.delete(0, END)
    display.insert(0, ans)


def scientific():
    global normalMode
    if normalMode:
        print("show scntfc")
        sFrame.pack(side=TOP)
        btnFrame.pack(side=TOP)

        normalMode = False
    else:
        print(" showNormal")
        sFrame.pack_forget()

        normalMode = True


# firstrow

btnpi = Button(sFrame, padx=15, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
               text=" π ")
btnpi.grid(row=0, column=0)

btnPower = Button(sFrame, padx=10, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                  text=" x  2 ")
btnPower.grid(row=0, column=1)

btnFact = Button(sFrame, padx=14, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                 text=" x ! ")
btnFact.grid(row=0, column=2)

btnRad = Button(sFrame, padx=11, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text="  rad ")
btnRad.grid(row=0, column=3)

# secondrow

btnSin = Button(sFrame, padx=10, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text=" sin ")
btnSin.grid(row=1, column=0)

btnCos = Button(sFrame, padx=12, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text=" cos ")
btnCos.grid(row=1, column=1)

btnTan = Button(sFrame, padx=12, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text=" tan ")
btnTan.grid(row=1, column=2)

btnDeg = Button(sFrame, padx=11, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text="  deg ")
btnDeg.grid(row=1, column=3)

# thirdrow

btnLog = Button(sFrame, padx=10, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text=" log ")
btnLog.grid(row=2, column=0)

btnRoot = Button(sFrame, padx=12, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                 text=" √ x ")
btnRoot.grid(row=2, column=1)

btnExpo = Button(sFrame, padx=12, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                 text=" ℮x ")
btnExpo.grid(row=2, column=2)

btnMod = Button(sFrame, padx=11, bd=8, fg="black", bg="honeydew3", font=('arial', 10, 'bold'),
                text=" mod ")
btnMod.grid(row=2, column=3)

# butonbinding

btnpi.bind("<Button-1>", printName)
btnPower.bind("<Button-1>", printName)
btnFact.bind("<Button-1>", printName)
btnRad.bind("<Button-1>", printName)
btnSin.bind("<Button-1>", printName)
btnCos.bind("<Button-1>", printName)
btnTan.bind("<Button-1>", printName)
btnDeg.bind("<Button-1>", printName)
btnLog.bind("<Button-1>", printName)
btnRoot.bind("<Button-1>", printName)
btnExpo.bind("<Button-1>", printName)
btnMod.bind("<Button-1>", printName)

menubar = Menu(gui)
mod = Menu(menubar, tearoff=0)
mod.add_checkbutton(label="Scientific Calculator", command=scientific)

menubar.add_cascade(label="mode", menu=mod)
gui.configure(menu=menubar)

gui.mainloop()
