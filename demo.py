from tkinter import *

root=Tk()
#creating label text
mylabel=Label(root,text="hi!")
mylabel1=Label(root,text="My name is samanta")
mylabel.grid(row=0,column=0)
mylabel1.grid(row=1,column=1)

root.mainloop()