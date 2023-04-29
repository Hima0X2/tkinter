from tkinter import *
root=Tk()
label=Label(root,text="hi")
label1=Label(root,text="bye")
label.grid(row=100,column=50)
label1.grid(row=20,column=0)
#label.pack() #default layout
root.mainloop()