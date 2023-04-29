from tkinter import * 
root=Tk() 
root.title("Calculator") 
e=Entry(root,width=30,borderwidth=10) 
e.grid(row=0,column=0,columnspan=3,padx=40,pady=20,ipadx=80, ipady=15) #design er jnno 
global c
def button_add():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    c=1
    e.delete(0, END)

def button_minus():
	c=2
	first_num = e.get()
	f_num = int(first_num)
	e.delete(0, END)
def button_mul():
	first_num = e.get()
	f_num = int(first_num)
	c=3
	e.delete(0, END)
def button_div():
	first_num = e.get()
	f_num = int(first_num)
	c=4
	e.delete(0, END)
def button_equal():
    second_num= e.get()
    e.delete(0, END)
    if(c==1):
    	e.insert(0, f_num + int(second_num))
    elif(c==2):
    	e.insert(0, f_num - int(second_num))
    elif(c==3):
    	e.insert(0, f_num * int(second_num))
    else:
    	e.insert(0, f_num / int(second_num))
def button_click(num):
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(num))
    
def button_clear():
    e.delete(0, END)

#define button 
button_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1)) 
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2)) 
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3)) 
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4)) 
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5)) 
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6)) 
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7)) 
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8)) 
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9)) 
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0)) 
button_add=Button(root,text="+",padx=39,pady=20,command=button_add) 
button_minus=Button(root,text="-",padx=39,pady=20,command=button_minus) 
button_mul=Button(root,text="*",padx=39,pady=20,command=button_mul)
button_div=Button(root,text="/",padx=39,pady=20,command=button_div)  
button_equal=Button(root,text="=",padx=79,pady=20,command=button_equal) 
button_clear=Button(root,text="C",padx=49,pady=20,command=button_clear) 

#for design 
button_1.grid(row=3,column=0) 
button_2.grid(row=3,column=1) 
button_3.grid(row=3,column=2) 
button_4.grid(row=2,column=0) 
button_5.grid(row=2,column=1) 
button_6.grid(row=2,column=2) 
button_7.grid(row=1,column=0) 
button_8.grid(row=1,column=1) 
button_9.grid(row=1,column=2) 
button_0.grid(row=4,column=0) 
button_clear.grid(row=4,column=1) 
button_add.grid(row=5,column=0) 
button_minus.grid(row=5,column=2)
button_mul.grid(row=4,column=2)
button_equal.grid(row=5,column=1)  
 
root.mainloop()