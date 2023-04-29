from tkinter import *
root=Tk()
e=Entry(root)
e.pack() #input file e pack alada deoa lgge
def myClick():
	top=Toplevel()
	mylabel=Label(top,text="My name is "+e.get(),fg="blue")
	# print("Hi")
	mylabel.pack()
mybutton=Button(root,text="Enter",command=myClick,fg="white",bg="black")
mybutton.pack()
root.mainloop()