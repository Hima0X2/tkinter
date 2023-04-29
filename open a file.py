from tkinter import *
from tkinter import filedialog

root=Tk()
root.filename=filedialog.askopenfilename(initialdir="D:\\documents\\tkinter",title="Select a file",filetypes=(("png files","*.png"),("all files","*.*")))
label=Label(root,)
root.mainloop()