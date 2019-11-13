from tkinter import *
from tkinter import messagebox
from datetime import date


root4 = Tk()
root4.title("BirthDay Remainder @theHardCoder")
root4.geometry('350x200')
global filename
filename = open("birthday.txt", "a+")


def AddRemainder():
    root1 = Tk()
    root1.title("Add Remainder")
    root1.geometry('350x200')
    date = Label(root1, text="Date(in format dd/mm) ")
    name = Label(root1, text="Name(in format fn sn) ")

    e1 = Entry(root1)
    e2 = Entry(root1)

    date.grid(row=0, pady=5)
    name.grid(row=1, pady=5)
    e1.grid(row=0, column=1, pady=5)
    e2.grid(row=1, column=1, pady=5)

    def Save():
        global filename
        filename.write("\n%s " % (e1.get()))
        filename.write("%s\n" % (e2.get()))

        filename.close()
        mes = messagebox.showinfo("Done", "Added Successfully")

    Save = Button(root1, text="Save", command=Save).grid(row=2, pady=5)
    Exit = Button(root1, text="Exit", command=exit).grid(row=2, column=1, pady=5)

    root1.mainloop()


def ShowRemainder():
    root2 = Tk()
    root2.title("Show Remainder")
    root2.geometry('350x200')
    global filename1
    filename1 = open("birthday.txt","r")

    def pri():
        text = Text(root2)
        global filename1
        for line in filename1:
            
            text.insert(INSERT, line)
            text.grid(row=2)
        
            
    pr = Button(root2, text="Show", command=pri)
    ex= Button(root2,text="Exit",command=exit).grid(row=1)
    
    pr.grid(row=0, pady=5)
    root2.mainloop()


def Show_options():
    root = Tk()
    root.title("Birthday Remainder")
    root.geometry('350x200')

    AddB = Button(root, text="Add Remainder", command=AddRemainder, activebackground="red")
    ShowB = Button(root, text="Show Remainder", command=ShowRemainder, activebackground="blue")
    #DeleteB = Button(root, text="Delete Remainder", command=Delete, activebackground="green")
    ExB = Button(root, text="Exit", command=exit, activebackground="pink")

    AddB.grid(row=0, pady=5)
    ShowB.grid(row=1, pady=5)
    
    ExB.grid(row=3, pady=5)

    root.mainloop()

def DestB():
    w =Tk()
    w.withdraw()
    w.after(3000, w.destroy) 
    global line
    if messagebox.showinfo("BirthDay Reamainder",line):
        w.destroy()

def DestN():
    
    w = Tk()
    w.withdraw()
    w.after(3000, w.destroy)
    
    if messagebox.showinfo("BirthDay Reamainder","No BirthDay Today"):
        w.destroy()


def RemindMe():
    flag = 0
    filename4 = open("birthday.txt")
    
    today = date.today()
    d1 = today.strftime('%d/%m')
    global line
    for line in filename4:
        if d1 in line:
            DestB()
            
            
            flag = flag + 1
    if flag == 0:
        DestN()
                        
    filename4.close()


Rb = Button(root4, text="Remind Me", command=RemindMe).grid(row=0, pady=5)
Sb = Button(root4, text="Show Options", command=Show_options).grid(row=1, pady=5)
Eb = Button(root4, text="Exit", command=exit).grid(row=2, pady=5)
root4.mainloop()





