from tkinter import *
import time
root=Tk()
root.title('Calculater')
root.config(bg='#27A')
root.geometry("500x600")
root.resizable(True,True)

def Result(x):
    if x=='=':
        try:
            string.set(eval(string.get()))
        except Exception as e:
            string.set(e)
    elif x=='C':
        string.set('')
    elif x=='CE':
        string.set(string.get()[:-1])
    else:
        string.set(string.get()+x)

f1=Frame(root)
f1.pack(padx=10,pady=5,fill=BOTH,expand=YES)
string=StringVar()
e1=Entry(f1,textvariable=string,font="arial 20 bold",bg='powder blue', bd=30, justify=RIGHT,relief=RIDGE)
e1.pack(fill=BOTH,expand=YES)

for data in ['789/','456*','123+','.0=-',['C','CE']]:
    f=Frame(root,bg='#27A')
    for d in data:
        b=Button(f,text=d,font="arial 10 bold",bg='powder blue',
                 command=lambda x=d:Result(x),relief=RAISED)
        b.pack(side=LEFT,padx=10,pady=10,fill=BOTH,expand=YES)
    f.pack(padx=5,pady=5,fill=BOTH,expand=YES)
    
def ShowTime():
    label['text']=time.ctime()
    label.after(1000,ShowTime)
f1=Frame(root)
f1.pack(padx=10,pady=10,fill=BOTH,expand=YES)
label=Label(f1,font="arial 10 bold",bg='powder blue',relief=RAISED)
label.pack(fill=BOTH,expand=YES)
ShowTime()

f1=Frame(root)
b=Button(f1,text='Close',font="arial 10 bold",bg='powder blue',command=lambda:root.destroy(),relief=RAISED)
b.pack(side=LEFT,fill=BOTH,expand=YES)
f1.pack(padx=10,pady=10,fill=BOTH,expand=YES)

root.mainloop()
