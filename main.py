from tkinter import *
from random import randint

wn = Tk()
wn.title("Rock,paper,scissor")
wn.configure(background="black")

a = 0
x = ""
res = ""

def rock():
    a = randint(1, 3)
    if a == 1:
        x = "Rock"
        res = "Draw"

    elif a == 2:
        x = "Paper"
        res = "Loss"

    else:
        x = "Scissor"
        res = "Win"

    la1.insert(1, x)
    la2.insert(1, res)


def paper():
    a = randint(1, 3)
    if a == 1:
        x = "Rock"
        res = "Win"

    elif a == 2:
        x = "Paper"
        res = "Draw"

    else:
        x = "Scissor"
        res = "Loss"

    la1.insert(1, x)
    la2.insert(1, res)

def scissor():
    a = randint(1, 3)
    if a == 1:
        x = "Rock"
        res = "Loss"

    elif a == 2:
        x = "Paper"
        res = "Win"

    else:
        x = "Scissor"
        res = "Draw"

    la1.insert(1, x)
    la2.insert(1, res)

def restart():
    a = 0
    x = ""
    res = ""
    la1.delete(0, 10)
    la2.delete(0, 10)

l1 = Label(wn, text="Computer:",bg="black", fg="white")
l1.grid(row=0, column=0)

la1 = Entry(wn)
la1.grid(row=0, column=1, columnspan=2)

l2 = Label(wn, text="Your choice:", bg="black",fg="white")
l2.grid(row=3, column=0)

but_r = Button(wn, text="  Rock ", command=rock, bg="red")
but_r.grid(row=3, column=1)

but_p = Button(wn, text=" paper ", command=paper, bg="light green")
but_p.grid(row=3, column=2)

but_s = Button(wn, text="Scissor", command=scissor, bg="blue")
but_s.grid(row=3, column=3)

l3 = Label(wn, text="Result:", bg="black",fg="white")
l3.grid(row=4, column=0)

la2 = Entry(wn)
la2.grid(row=4, column=1, columnspan=2)

but_restart = Button(wn, text="Restart", command=restart, bg="brown", fg="Yellow")
but_restart.grid(row=5, column=1)

but_exit = Button(wn, text="Exit", command=exit, bg="brown", fg="Yellow")
but_exit.grid(row=6, column=1)

wn.mainloop()