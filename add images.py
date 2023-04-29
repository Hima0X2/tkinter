from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Add image")
My_img=ImageTK.PhotoImage(Image.open("pocket_calculator.png"))
my_label=Label(image=My_img)
my_label.pack()
root.mainloop()