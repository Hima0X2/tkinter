from tkinter import *
from PIL import Image,ImgeTK
root=Tk()
root.geometry('200x300')#window size
photo=PhotoImage(file="1.png")
label=Label(image=photo)
label.pack()
root.mainloop()