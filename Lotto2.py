# Creating a window
from tkinter import *
import random
from datetime import *
from tkinter import messagebox

# Creating a window
window = Tk()
window.geometry("1020x1020")
labelA = Label(window, text="Please enter your numbers.")
labelA.pack()

# creating random numbers between 1 - 49, in a loop
gen = []
lottery = random.sample(range(1, 50), 6)
# this will show the date and time on the 2nd window, when the user is about to enter their numbers
date = datetime.now()
dlb = Label(window)
dlb.place(x=200, y=1)
dlb.config(text="Date" + date.strftime("%d/%m/%y %H:%M"))

res = Label(window)

res.place(x=280, y=100)


def response():
    num1.configure(text=str(random.sample(range(0, 50), 1)))
    print(num1)
    num2.configure(text=str(random.sample(range(0, 50), 1)))
    print(num2)
    num3.configure(text=str(random.sample(range(0, 50), 1)))
    print(num3)
    num4.configure(text=str(random.sample(range(0, 50), 1)))
    print(num4)
    num5.configure(text=str(random.sample(range(0, 50), 1)))
    print(num5)
    num6.configure(text=str(random.sample(range(0, 50), 1)))
    print(num6)

    return


def changes():
    num1.configure(text=str(0))
    num2.configure(text=str(0))
    num3.configure(text=str(0))
    num4.configure(text=str(0))
    num5.configure(text=str(0))
    num6.configure(text=str(0))


# creating labels  for each entry block
try:
    num1 = Entry(window, relief='groove', width=5, bd=4, fg='white', bg='blue')
    num1.place(y=100, x=100)
    num2 = Entry(window, relief='groove', width=5, bd=4, fg='white', bg='purple')
    num2.place(y=200, x=100)
    num3 = Entry(window, relief='groove', width=5, bd=4, fg='white', bg='red')
    num3.place(y=300, x=100)
    num4 = Entry(window, relief='groove', width=5, bd=4, fg='white', bg='orange')
    num4.place(y=400, x=100)
    num5 = Entry(window, relief='groove', width=5, bd=4, fg='white', bg='green')
    num5.place(y=500, x=100)
    num6 = Entry(window, relief='groove', width=5, bd=4, fg='white', bg='black')
    num6.place(y=600, x=100)
except ValueError:
    messagebox.showerror("error", "please enter your numbers")


# the winning numbers changes every time you start a new thing
def win():
    try:
        gen.append(int(num1.get()))
        gen.append(int(num2.get()))
        gen.append(int(num3.get()))
        gen.append(int(num4.get()))
        gen.append(int(num5.get()))
        gen.append(int(num6.get()))
    except ValueError:
        messagebox.showerror("ERROR","Please enter your numbers")
    right = set(gen).intersection(lottery)
    lb = Label(window)

    if gen == lottery:
        res.config(text="Results:" + str(lottery))
        lb.config(text="You're a winner!: R10 000 000.00" "Woo-hoo!")
        messagebox.showinfo("Message", "You're a winner!: R10 000 000.00" "Woo-hoo!")

    elif len(right) == 0:
        res.config(text="Results:" + str(lottery))
        lb.config(text="You're a winner!: R10 000 000.00" "Woo-hoo!")
        messagebox.showinfo("Message", "You won: Nothing")
    elif len(right) == 1:
        res.config(text="Results:" + str(lottery))
        lb.config(text="You won: Nothing")
        messagebox.showinfo("Message", "You won: Nothing")

    elif len(right) == 2:
        lb.config(text="You won: R8,584.00")
        res.config(text="Results:" + str(lottery))
        messagebox.showinfo("Message", "You won: R8,584.00")


    elif len(right) == 3:
        res.config(text="Results:" + str(lottery))
        lb.config(text="You won: R2,384.00")
        messagebox.showinfo("Message", "You won: R2,384.00")

    elif len(right) == 4:
        res.config(text="Results:" + str(lottery))
        lb.config(text="You won: R100.00")
        messagebox.showinfo("Message", "You won: R100.00")

    elif len(right) == 5:
        res.config(text="Results:" + str(lottery))
        lb.config(text="You won: R20.00")
        messagebox.showinfo("Message", "You won: R20.00")

    date = datetime.now()
    dlb = Label(window)
    dlb.place(x=200, y=1)
    dlb.config(text="Date" + date.strftime("%d/%m/%y %H:%M"))

    f = open("result.txt", "w+")
    f.write(res.cget("text"))
    f.close()

    f = open("result.txt", "a+")
    f.write(res.cget("text"))
    f.close()


numberGen = Button(window, width=20, text="Generate Numbers", command=win)
numberGen.place(x=280, y=40)

window.mainloop()
