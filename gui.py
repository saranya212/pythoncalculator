from tkinter import *

window = Tk()
window.geometry('350x300')


def callback(a):
    print(a)

Label = Label(window, text="welcome", )
Label.pack()
print("gui __name__ = %s" % __name__)
e1 = Entry(window, bd=5,cursor="dot",highlightcolor="green")
e1.pack()
Button = Button(window, text="click", width=30, height=10, compound="center", activeforeground="orange", bd=3,
                highlightcolor="red", relief="raised", command=lambda: callback("b"))
Button.pack(pady=40, side=TOP)
scroll_bar = Scrollbar(window)

scroll_bar.pack(side=RIGHT,
                fill=X)
window.mainloop()
