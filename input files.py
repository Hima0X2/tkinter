from tkinter import *

root=Tk()
#root.iconbitmap("C:/Users/SANJIDA/Desktop/pocket_calculator.png")
#creating input file
mylabel=Label(root,text="Enter your name",fg="blue")
mylabel.pack()
e=Entry(root,width=10)
e.pack()
#creating button
def myClick():
	mylabel=Label(root,text="My name is "+e.get(),fg="blue")
	# print("Hi")
	mylabel.pack()
mybutton=Button(root,text="Enter",command=myClick,fg="white",bg="black")
mybutton.pack()
root.mainloop()