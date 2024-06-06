import tkinter as Tk
from tkinter import *

root=Tk()
root.title("Task-work")
root.geometry("400x520+400+400")
root.resizable(False,False)

task_list=[]

def addTask():
    task=task_entry.get()
    

    if task:
        with open("tasklist.txt",'a')as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w')as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)

def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r")as taskfile:
            task=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file=open('tasklist.txt','w')
        file.close()
        

frame=Frame(root,width=400,height=50,bg="Black")
frame.place(x=0,y=10)

task=StringVar()
task_entry=Entry(frame,width=30,font="candara",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold",width=5,bg="Sienna",fg="black",bd=0,command=addTask)
button.place(x=310,y=0)

frame1=Frame(root,bd=0,width=700,height=280,bg="PowderBlue")
frame1.pack(pady=(100,30))

listbox=Listbox(frame1,font=('candara',12),width=40,height=16,bg="PowderBlue")
listbox.pack(side=LEFT,fill=BOTH,padx=2)



button = Button(root, text = 'DELETE',bg="PaleGreen",width=10,height=15,command =deleteTask)
button.pack(side=BOTTOM,padx=20, pady=20)




root.mainloop


