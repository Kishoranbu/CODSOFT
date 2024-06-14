from tkinter import *
import pyperclip
import random
import os

root=Tk()
root.title("password generator")
root.geometry("400x400")
root.resizable(False,False)
passstr=StringVar()
passlen=IntVar()
passlen.set(0)

def generate():
    pass1=[
        'A','B','C','D','E','F','G','H','I','j','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '1','2','3','4','5','6','7','8','9','0','.','<','>',',','@','#','^','!','$','%','&','*']
    password=""
    for x in range(passlen.get()):
       password += random.choice(pass1)
    passstr.set(password)

def copytoclipboard():
    random_password=passstr.get()
    pyperclip.copy(random_password)
    
frame=Frame(root,width=400,height=400,bg="#00FF7F")
frame.place(x=0,y=10)

label=Label(text="password generator",bg='#00FF7F',font="candara 12")
label.place(x=0,y=103,width=400,height=37)

entry1=Entry(root,textvariable=passlen,bg='#FFF68F',font="candara 12",justify="center")
entry1.place(x=100,y=131,width=201,height=37)

button1=Button(text="generate password",font="candara 10 ",width=5,bg="#FFBBFF",fg="black",bd=0,command=generate)
button1.place(x=126,y=184,height=24,width=149)

label=Label(text="password",bg='#00FF7F',font="candara 12")
label.place(x=0,y=230,width=400,height=37)

entry2=Entry(root,textvariable=passstr,bg="#FFF68F",font="candara 12",justify='center')
entry2.place(x=100,y=258,width=201,height=37)



button2=Button(text="copy to clipboard",font="candara 10 ",width=5,bg="#FFBBFF",fg="black",bd=0,command=copytoclipboard)
button2.place(x=126,y=310,height=24,width=149)

root.mainloop()


