from tkinter import*
from math import*

win = Tk()
win.geometry("400x400")
win.title("Simple Calculator")

num1 = Label(win,text="Enter X:",fg="red",font=("Calibri Light",12))
num1.place(x=20,y=20)

num1Ent = Entry(win)
num1Ent.place(x=80,y=20)

num2 = Label(win,text="Enter Y:",fg="Green",font=("Arial",12))
num2.place(x=20,y=90)

num2Ent = Entry(win)
num2Ent.place(x=80,y=90)

ans = Label(win,text="Answer:",fg="Blue",font=("Arial",14))
ans.place(x=20,y=150)

ansShow = Entry(win)
ansShow.place(x=100,y=150)
#-------------------------------------------------------------------------------------------------#
#function part
#-------------------------------------------------------------------------------------------------#
def addition():
    n1=int(num1Ent.get())
    n2=int(num2Ent.get())
    final = n1+n2
    ansShow.delete(0,"end")
    ansShow.insert(0,final)

def subtract():
    n1=int(num1Ent.get())
    n2=int(num2Ent.get())
    nf = n1 - n2
    ansShow.delete(0,"end")    
    ansShow.insert(0,nf)

def multi():
    n1=int(num1Ent.get())
    n2=int(num2Ent.get())
    nf = n1 * n2
    ansShow.delete(0,"end")    
    ansShow.insert(0,nf)    

def div():
    n1=int(num1Ent.get())
    n2=int(num2Ent.get())
    nf = n1 / n2
    ansShow.delete(0,"end")    
    ansShow.insert(0,nf)    

def reset():
    num1Ent.delete(0,"end")
    num2Ent.delete(0,"end")
    ansShow.delete(0,"end")

def root():
    x=int(num1Ent.get())
    nf = sqrt(x)
    ansShow.delete(0,"end")
    ansShow.insert(0,nf)

#------------------------------------------------------------------------------------------------#
addBtn = Button(win,text="Add",font=("Arial",16),command=addition)
addBtn.place(x=20,y=190)

subBtn = Button(win,text="Subtract",font=("Arial",16),command=subtract)
subBtn.place(x=90,y=190)

multiBtn = Button(win,text="Multiply",font=("Arial",16),command=multi)
multiBtn.place(x=200,y=190)

divBtn =Button(win,text="divid",font=("Arial",16),command=div)
divBtn.place(x=20,y=250)

resBtn = Button(win,text="Reset Enteries",font=("Arial",16),command=reset)
resBtn.place(x=90,y=250)

rootBtn = Button(win,text="sqrt(x)",font=("Arial",16),command=root)
rootBtn.place(x=20, y=300)

win.mainloop()
