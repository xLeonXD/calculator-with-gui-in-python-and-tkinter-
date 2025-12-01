from tkinter import *

def txt():
    try:
        with open("calc.txt", "r") as file:
            txt = file.read()
        if txt == "":
            txt = "0"
        return txt
    except:
        print("file not found")

def lb_update(func):
    def wrapper(x):
        func(x)
        try:
            with open("calc.txt", "r") as file:
                tx = file.read()
            if tx == "":
                tx = "0"
        except:
            print("error on lb_update")
        a.config(text=tx)
    return wrapper

def lb_update2(func):
    def wrapper():
        func()
        try:
            with open("calc.txt", "r") as file:
                tx = file.read()
            if tx == "":
                tx = "0"
        except:
            print("error on lb_update2")
        a.config(text=tx)
    return wrapper

@lb_update
def appending(x):
        x = str(x)
        with open("calc.txt", "r") as file:
            tx = file.read()

        if tx == "Syntax Error":
            with open("calc.txt", "w") as file:
                file.write(x)
        elif tx == "0":
            with open("calc.txt", "w") as file:
                file.write(x)
        else:
            with open("calc.txt", "a+") as file:
                file.write(x)

@lb_update
def resulting(x):
    x = str(x)
    with open("calc.txt", "w")as file:
        file.write(x)

@lb_update2
def clear():
    with open("calc.txt", "w") as file:
        file.write("")

@lb_update2
def equal():
    tx = txt()
    try:
        result = eval(tx)
        print(result)
        resulting(result)
        return result
    except ZeroDivisionError:
        print("Can't divide by zero!!")
        result = "Syntax Error"
        print(result)
        resulting(result)
        return result
    except SyntaxError:
        result = "Syntax Error"
        print(result)
        resulting(result)
        return result
    except:
       print("Error with calc.txt")

tx = txt()

root = Tk()
root.geometry("300x300")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)
root.grid_rowconfigure(4,weight=1)

a = Label(root,text=tx,anchor="center")
a.grid(row=0,column=1,columnspan=4,sticky="nsew")

root.title("Calculator")
button1 = Button(root,text="1",command=lambda: appending(1))
button1.grid(row=1,column=0,sticky="nsew")
button2 = Button(root,text="2",command=lambda: appending(2))
button2.grid(row=1,column=1,sticky="nsew")
button3 = Button(root,text="3",command=lambda: appending(3))
button3.grid(row=1,column=2,sticky="nsew")
button4 = Button(root,text="4",command=lambda: appending(4))
button4.grid(row=2,column=0,sticky="nsew")
button5 = Button(root,text="5",command=lambda: appending(5))
button5.grid(row=2,column=1,sticky="nsew")
button6 = Button(root,text="6",command=lambda: appending(6))
button6.grid(row=2,column=2,sticky="nsew")
button7 = Button(root,text="7",command=lambda: appending(7))
button7.grid(row=3,column=0,sticky="nsew")
button8 = Button(root,text="8",command=lambda: appending(8))
button8.grid(row=3,column=1,sticky="nsew")
button9 = Button(root,text="9",command=lambda: appending(9))
button9.grid(row=3,column=2,sticky="nsew")
button0 = Button(root,text="0",command=lambda: appending(0))
button0.grid(row=4,column=0,columnspan=2,sticky="nsew")
buttondec = Button(root,text=".",command=lambda: appending("."))
buttondec.grid(row=4,column=2,sticky="nsew")
buttonadd = Button(root,text="+",command=lambda: appending("+"))
buttonadd.grid(row=1,column=3,sticky="nsew")
buttonsubtract = Button(root,text="-",command=lambda: appending("-"))
buttonsubtract.grid(row=2,column=3,sticky="nsew")
buttondivide = Button(root,text="/",command=lambda: appending("/"))
buttondivide.grid(row=2,column=4,sticky="nsew")
buttonmultiply = Button(root,text="*",command=lambda: appending("*"))
buttonmultiply.grid(row=1,column=4,sticky="nsew")
buttonclear = Button(root,text="C",command=clear)
buttonclear.grid(row=0,column=0,sticky="nsew")
buttonequal = Button(root,text="=",command=equal)
buttonequal.grid(row=3,rowspan=2,column=3,columnspan=2,sticky="nsew")

root.mainloop()
