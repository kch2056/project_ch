import googletrans

translator = googletrans.Translator()
# i = input()
# o = translator.translate(i, dest = 'ko', src = 'en')
# print(o.text)

from tkinter import *

root = Tk()

# listbox = Listbox(root)
label1 = Label(root, text='영어')
label2 = Label(root, text='한국어')
#entry = Entry(root)
text1 = Text(root)
text2 = Text(root)

form = '1'
language = ''
translate = 'n'

def translate_click(event):
    global i
    global o
    global language
    global translate
    i = text1.get("1.0", "end")
    if form == '1' : 
        o = translator.translate(i, dest = 'ko', src = 'en')
        language = 'en->ko'
    else : 
        o = translator.translate(i, dest = 'en', src = 'ko')
        language = 'ko->en'
    text2.delete("1.0", "end")
    text2.insert(1.0, o.text)
    translate = 'y'

def delete_click(event):
    global translate
    text1.delete("1.0", "end")
    text2.delete("1.0", "end")
    translate = 'n'

def language_click(event) :
    global form
    global language
    global translate
    if form == '1' : 
        label1.config(text='한국어')
        label2.config(text='영어')
        if translate == 'y' : 
            if language == 'en->ko' : 
                text1.delete("1.0", "end")
                text1.insert(1.0, o.text)
                text2.delete("1.0", "end")
                text2.insert(1.0, i)
            else : 
                text1.delete("1.0", "end")
                text1.insert(1.0, i)
                text2.delete("1.0", "end")
                text2.insert(1.0, o.text)
        form = '2'
    else : 
        label1.config(text='영어')
        label2.config(text='한국어')
        if translate == 'y' : 
            if language == 'en->ko' : 
                text1.delete("1.0", "end")
                text1.insert(1.0, i)
                text2.delete("1.0", "end")
                text2.insert(1.0, o.text)
            else : 
                text1.delete("1.0", "end")
                text1.insert(1.0, o.text)
                text2.delete("1.0", "end")
                text2.insert(1.0, i)
        form = '1'

b1 = Button(root, text='번역')
b2 = Button(root, text='삭제')
b3 = Button(root, text='⇄')

# listbox.grid(row=0, column=0, columnspan=3, sticky='ew')
label1.grid(row=1, column=0,columnspan=2)
b3.grid(row=1, column=2,columnspan=1, sticky='ew')
b3.bind('<Button-1>', language_click)
label2.grid(row=1, column=3,columnspan=2)
#entry.grid(row=1, column=1, columnspan=2, sticky='ew')
text1.grid(row=2, column=0, columnspan=2)
text2.grid(row=2, column=3, columnspan=2)
b1.grid(row=3, column=0,columnspan=2, sticky='ew')
b1.bind('<Button-1>', translate_click)
b2.grid(row=3, column=3,columnspan=2, sticky='ew')
b2.bind('<Button-1>', delete_click)

root.mainloop()
