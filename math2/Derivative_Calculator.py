import math
from sympy import symbols, Limit    # pip install sympy

from tkinter import *
# from sympy.parsing.sympy_parser import parse_expr

root = Tk()

# listbox = Listbox(root)
label1 = Label(root, text='... 의 미분 계산')
label2 = Label(root, text='다음과 같이 계산됩니다:')
entry = Entry(root)
text1 = Text(root)
text2 = Text(root)

b1 = Button(root, text='번역')
b2 = Button(root, text='삭제')
b3 = Button(root, text='Go!')

def Go_click(event):
    global fx
    global language
    global result
    x, a, h = symbols('x, a, h')
    fx = eval(entry.get())
    # fx = 3 * (x**2) - 4 * x + 1     # 함수 f(x) 정의
    fxa = fx.subs({x: a})           # f(x)에 x = a 대입
    fxh = fx.subs({x: a + h})       # f(x)에 x = a + h 대입
    result = Limit((fxh - fxa)/h, h, 0).doit()     # 극한값(미분계수) 계산
    text1.insert(1.0, result)

# x, a, h = symbols('x, a, h')

# fx = 3 * (x**2) - 4 * x + 1     # 함수 f(x) 정의
#  fxh = fx.subs({x: a + h})       # f(x)에 x = a + h 대입

# result = Limit( (fxh - fxa)/h, h, 0 ).doit()     # 극한값(미분계수) 계산

# print(fxa)
# print(fxh)
# print("미분 Result:", result)

# listbox.grid(row=0, column=0, columnspan=3, sticky='ew')
label1.grid(row=1, column=0,columnspan=10)
b3.grid(row=2, column=11,columnspan=1, sticky='ew')
b3.bind('<Button-1>', Go_click)
label2.grid(row=3, column=0,columnspan=10)
entry.grid(row=2, column=0, columnspan=10, sticky='ew')
text1.grid(row=4, column=0, columnspan=10)
# text2.grid(row=2, column=3, columnspan=2)
# b1.grid(row=3, column=0,columnspan=2, sticky='ew')
# b1.bind('<Button-1>', translate_click)
# b2.grid(row=3, column=3,columnspan=2, sticky='ew')
# b2.bind('<Button-1>', delete_click)

root.mainloop()
