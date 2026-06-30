from tkinter import *

root = Tk()
root.title("Tk")
root.geometry("300x200")

heo = Label(root, text="HELLO Everyone!!!", font=("Arial",20))
heo.pack(padx=20, pady=20)

def say():
    heo.config(text="Button Clicked!")

but = Button(root, text="Click Here", command=say)
but.pack(padx=20, pady=20)

root.mainloop()