from tkinter import *
root=Tk()
c=Checkbutton(root,text="I am so bad").pack()
d=Checkbutton(root,text="I am so bad").pack()
#dropdown box
click=StringVar()
click.set("mon")
drop=OptionMenu(root,click,"sat","sun","mon").pack()
root.mainloop()