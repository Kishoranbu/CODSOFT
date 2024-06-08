import tkinter

from tkinter import *

root=Tk()
root.title("Simple calculator")
root.geometry("400x600+400+100")
root.resizable(False,False)
root.configure(bg="LightCoral")

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)
    
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

    
label_result=Label(root,width=25,height=2,text="",font=("arial",30),bg="LemonChiffon")
label_result.pack()


Button(root,text="c",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="SpringGreen",command=lambda:clear()).place(x=0,y=100)
Button(root,text="/",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("/")).place(x=100,y=100)
Button(root,text="%",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("%")).place(x=200,y=100)
Button(root,text="*",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("*")).place(x=300,y=100)

Button(root,text="9",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("9")).place(x=0,y=200)
Button(root,text="8",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("8")).place(x=100,y=200)
Button(root,text="7",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("7")).place(x=200,y=200)
Button(root,text="-",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("-")).place(x=300,y=200)

Button(root,text="6",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("6")).place(x=0,y=300)
Button(root,text="5",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("5")).place(x=100,y=300)
Button(root,text="4",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("4")).place(x=200,y=300)
Button(root,text="+",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("+")).place(x=300,y=300)

Button(root,text="3",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("3")).place(x=0,y=400)
Button(root,text="2",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("2")).place(x=100,y=400)
Button(root,text="1",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("1")).place(x=200,y=400)
Button(root,text="0",width=11,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show("0")).place(x=0,y=500)

Button(root,text=".",width=5,height=1,font=("candara",24,"bold"),bd=1,fg="black",bg="Lavender",command=lambda:show(".")).place(x=200,y=500)
Button(root,text="=",width=5,height=4,font=("candara",24,"bold"),bd=1,fg="black",bg="cyan",command=lambda:calculate()).place(x=300,y=400)

root.mainloop()
