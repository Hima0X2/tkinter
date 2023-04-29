from tkinter import *
from tkinter import messagebox
root=Tk()
def click():
	messagebox.showinfo( "Hello Python", "Hello World")

root.title("Button")
button=Button(root,text="hi",command=click,fg="green",bg="yellow")#state="disabled"=desable button
button.pack()
root.mainloop()