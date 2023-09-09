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

def purekorean_click(event) :
    if o.text == '갈라쇼' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "뒤풀이공연")
    if o.text == '골드미스' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "황금독신여성")
    if o.text == '그라피티' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "길거리그림")
    if o.text == '그룹 홈' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "자활꿈터")
    if o.text == '그린 프리미엄' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "환경덧두리")
    if o.text == '글램핑' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "귀족야영")
    if o.text == '갈라쇼' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "뒤풀이공연")
    if o.text == '네티즌' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "누리꾼")
    if o.text == '넷북' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "손누리틀")
    if o.text == '노블레스 오블리주' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "지도층의무")
    if o.text == '다크서클' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "눈그늘")
    if o.text == '다크 투어리즘' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "역사교훈여행")
    if o.text == '테크아트 마케팅' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "예술감각상품")
    if o.text == '드레스 코드' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "표준옷차림")
    if o.text == '드레싱' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "맛깔장")
    if o.text == '디오라마' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "실사모형")
    if o.text == '디펜딩 챔피언' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "우승지킴이")
    if o.text == '갈라쇼' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "뒤풀이공연")
    if o.text == '러브 라인' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "사랑구도")
    if o.text == '러브샷' :
        text2.delete("1.0", "end")
        text2.insert(1.0, "사랑공연")

b1 = Button(root, text='번역')
b2 = Button(root, text='삭제')
b3 = Button(root, text='⇄')
b4 = Button(root, text='순우리말 번역')

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
b4.grid(row=4, column=0, columnspan=5, sticky='ew')
b4.bind('<Button-1>', purekorean_click)

root.mainloop()
