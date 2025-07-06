import tkinter as tk
t=tk.Tk()
t.title("Basic calculator")
label1=tk.Label(t,text="Enter num1: ")
label2=tk.Label(t,text="Enter num2: ")
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
e1=tk.Entry(t)
e2=tk.Entry(t)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
def add():
   num1=int(e1.get())
   num2=int(e2.get())
   result=num1+num2
   label3.config(text=str(result))
def sub():
    num1=int(e1.get())
    num2=int(e2.get())
    if num1>num2:
        result=num1-num2
        label3.config(text=str(result))
    else:
        result=num2-num1
        label3.config(text=str(result))
def mul():
    num1=int(e1.get())
    num2=int(e2.get())
    result=num1*num2
    label3.config(text=str(result))
def divide():
    num1=int(e1.get())
    num2=int(e2.get())
    if num1>num2:
        result=num1/num2
        label3.config(text=str(result))
    else:
        result=num2/num1
        label3.config(text=str(result))
btn1=tk.Button(t,text="+",activebackground="blue",activeforeground="red",width=35,command=add)
btn2=tk.Button(t,text="-",activebackground="blue",activeforeground="red",width=35,command=sub)
btn3=tk.Button(t,text="*",activebackground="blue",activeforeground="red",width=35,command=mul)
btn4=tk.Button(t,text="/",activebackground="blue",activeforeground="red",width=35,command=divide)
btn1.grid(row=2,column=1)
btn2.grid(row=3,column=1)
btn3.grid(row=4,column=1)
btn4.grid(row=5,column=1)
label3=tk.Label(t,text="RESULT")
label3.grid(row=6,column=1)
t.mainloop()
