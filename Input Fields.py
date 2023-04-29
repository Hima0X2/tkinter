from tkinter import *
from pil import Image,ImageTK
root=Tk()
root.title("Kochu")
img=ImageTK.photoimage(Image.open("1.png"))
label=Label(root,image=img)
label.pack()
root.iconbitmap("D:/documents/openCV/images.jpg")
e=Entry(root,width=20)
e.pack()
def ok():
	label=Label(root,text=e.get())
	label.pack()

button=Button(root,text="CLick",command=ok)
button.pack()
root.mainloop()