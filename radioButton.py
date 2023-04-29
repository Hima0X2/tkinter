from tkinter import *

root=Tk()
i = IntVar()
Radiobutton(root, text="option 1", value=1, variable=i).pack()
Radiobutton(root, text="option 2", value=2, variable=i).pack()
root.mainloop()