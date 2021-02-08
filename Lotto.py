#creating a window
from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry("500x450")

label1 = Label(window, text="You have to be 18 and above play the lotto.")
label1.pack()

#this function is for the button on the left, if they say "No, i am not 18 and above." a message box will pop up and it will close
def No():
    #if you agree with window , it will close the application
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application?',icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        messagebox.showinfo('Return','You will now return to the application screen')

but1 = Button(window, text="No, i am not 18 and above.", command=No)
but1.place(x=10, y=70)


#this function is for the button on the right and it will close the window once they said yes and open a new window
def verify():

#the window will be destroyed once clicking yes
    window.destroy()
    import Lotto2


but2 = Button(window, text="Yes, i am 18 and above.", command=verify)
but2.place(x=300, y=70)


window.mainloop()
