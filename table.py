from tkinter import *
lst= [('id','name','place','roll'),
        (1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
rows=len(lst)
cols=len(lst[0])
for i in range(rows):
    for j in range(cols):
        e = Entry()
        e.grid(row=i, column=j)
        e.insert(0,lst[i][j])
        e.config(state= "disabled")

mainloop()