from tkinter import *
root = Tk()
root.title("GUI Calculator")

content = ""
txt_input = StringVar(value = "0")
def btn(number):
    global content
    content = content + str(number)
    txt_input.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = ""

def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0, "0")

display = Entry(font = ("prompt",30,"bold"), fg = "white" , bg = "green",textvariable = txt_input,justify = "right")
display.grid(columnspan = 4)

btn7 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "7" , padx = 30 ,command = lambda:btn(7), pady = 15).grid(row = 1, column =0)
btn8 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "8" , padx = 30 ,command = lambda:btn(8), pady = 15).grid(row = 1, column =1)
btn9 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "9" , padx = 30 ,command = lambda:btn(9), pady = 15).grid(row = 1, column =2)
C = Button(font = ("prompt",30,"bold"),bg = "orange" ,fg = "black" , text = "C" , padx = 30 ,command = lambda:clear(), pady = 15).grid(row = 1, column = 3)

btn4 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "4" , padx = 30 ,command = lambda:btn(4), pady = 15).grid(row = 2, column =0)
btn5 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "5" , padx = 30 ,command = lambda:btn(5), pady = 15).grid(row = 2, column =1)
btn6 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "6" , padx = 30 ,command = lambda:btn(6), pady = 15).grid(row = 2, column =2)
D = Button(font = ("prompt",30,"bold"),bg = "orange" ,fg = "black" , text = "+" , padx = 30 ,command = lambda:btn("+"), pady = 15).grid(row = 2, column = 3)

btn1 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "1" , padx = 30 ,command = lambda:btn(1), pady = 15).grid(row = 3, column =0)
btn2 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "2" , padx = 30 ,command = lambda:btn(2), pady = 15).grid(row = 3, column =1)
btn3 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "3" , padx = 30 ,command = lambda:btn(3), pady = 15).grid(row = 3, column =2)
E = Button(font = ("prompt",30,"bold"),bg = "orange" ,fg = "black" , text = "-" , padx = 30 ,command = lambda:btn("-"), pady = 15).grid(row = 3, column = 3)

btn0 = Button(font = ("prompt",30,"bold"), fg = "black" , text = "0" , padx = 30 ,command = lambda:btn(0), pady = 15).grid(row = 4, column =0)
btndot = Button(font = ("prompt",30,"bold"), fg = "black" , text = "." , padx = 30 ,command = lambda:btn("."), pady = 15).grid(row = 4, column =1)
btnslash = Button(font = ("prompt",30,"bold"),bg = "orange" , fg = "black" , text = "/" , padx = 35 ,command = lambda:btn("/"), pady = 15).grid(row = 4, column =2)
X = Button(font = ("prompt",30,"bold"),bg = "orange" ,fg = "black" , text = "x" , padx = 35 ,command = lambda:btn("*"), pady = 15).grid(row = 4, column = 3)

btnequal = Button(font = ("prompt",30,"bold"),bg = "light blue" , fg = "black" , text = "=" , padx = 95,command = lambda:equal(), pady = 15).grid(row = 5, column =0 ,columnspan = 2)
btneopen = Button(font = ("prompt",30,"bold"),bg = "orange" , fg = "black" , text = "(" , padx = 35 ,command = lambda:btn("("), pady = 15).grid(row = 5, column = 2)
btnclose = Button(font = ("prompt",30,"bold"),bg = "orange" ,fg = "black" , text = ")" , padx = 35 ,command = lambda:btn(")"), pady = 15).grid(row = 5, column = 3)
root.mainloop()