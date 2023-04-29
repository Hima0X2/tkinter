from tkinter import *
root=Tk()
def hi(var):
	label=Label(root,text=horizontal.get()).pack()
	root.geometry(str(horizontal.get)+"*400")
vertical=Scale(root,from_=0,to=200).pack()
horizontal=Scale(root,from_=0,to=20,orient=HORIZONTAL,command=hi).pack()
root.mainloop()