from tkinter import *
import math
def click(value):
    ex = entryField.get()  # 789 ex[0:len(ex)-1]
    answer = ''
    try:
        if value == 'C':
            ex = ex[0:len(ex) - 1]  # 78
            entryField.delete(0, END)
            entryField.insert(0, ex)
            ansField.delete(0, END)
            return
        elif value == 'CE':
            entryField.delete(0, END)
            ansField.delete(0, END)
        elif value == '√':
            answer = math.sqrt(eval(ex))
        elif value == 'π':
            answer = math.pi
        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))
        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))
        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))
        elif value == '2π':
            answer = 2 * math.pi
        elif value == 'cosh':
            answer = math.cosh(eval(ex))
        elif value == 'tanh':
            answer = math.tanh(eval(ex))
        elif value == 'sinh':
            answer = math.sinh(eval(ex))
        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)
        elif value == 'x\u02b8':  # 7**2
            entryField.insert(END, '**')
            return
        elif value == 'x\u00B3':
            answer = eval(ex) ** 3
        elif value == 'x\u00B2':
            answer = eval(ex) ** 2
        elif value == 'ln':
            answer = math.log2(eval(ex))
        elif value == 'deg':
            answer = math.degrees(eval(ex))
        elif value == "rad":
            answer = math.radians(eval(ex))
        elif value == 'e':
            answer = math.e
        elif value == 'log₁₀':
            answer = math.log10(eval(ex))
        elif value == 'x!':
            answer = math.factorial(ex)
        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return
        elif value == '=':
            answer = eval(ex)
        else:
            entryField.insert(END, value)
            return
        entryField.delete(0, END)
        ansField.insert(0, answer)
    except SyntaxError:
        pass
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def lcm(a,b):
    l=math.lcm(a,b)
    return l
def hcf(a,b):
    h=math.gcd(a,b)
    return h
operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm , 'HCF':hcf,
            'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod }
root = Tk()
root.title('calculator created by PRATIK')
root.config(bg='black')                  
root.geometry('694x486+100+100')
entryField = Entry(root, font=('arial', 20, 'bold'), fg="dark red", bg="white", bd=10, relief=SUNKEN, width=22)
entryField.grid(row=0, column=0, columnspan=4)

ansField = Entry(root, font=('arial', 20, 'bold'), fg="forest green", bg="white", bd=10, relief=SUNKEN, width=15)
ansField.grid(row=0, column=5 , columnspan=3)
button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='white',
                    font=('arial', 18, 'bold'), activebackground='white', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=2)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0
root.mainloop()