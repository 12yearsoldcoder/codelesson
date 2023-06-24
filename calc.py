from tkinter import *
from tkinter.ttk import *
from main import *
import matplotlib.pyplot as plt
import numpy as np


def draw_graph():
    A = int(ent_A.get())
    B = int(ent_B.get())
    C = int(ent_C.get())
    x = np.array(range(-20,21))
    y = A*x**2+B*x+C
    plt.grid(color = '0.8')

    plt.xlabel('x axis')
    plt.ylabel('y axis')

    label = f"{A}x²"
    if B:
        op = '+' if B > 0 else '-'
        label += f' {op} {abs(B)}x'
    if C:
        op = '+' if C > 0 else '-'
        label += f" {op} {abs(C)}"
    plt.plot(x,y,label = label)
    plt.legend()
    plt.show()


def get_result():
    A = ent_A.get()
    B = ent_B.get()
    C = ent_C.get()

    result = solution(A,B,C)
    print(result)
    ent_result.delete(0,'end')
    ent_result.insert(0,result)



#메인창 만들기
root = Tk()

root.title('Calculater')
root.geometry('580x300')

# Entry
ent_A = Entry(font = '맑은고딕 20')
ent_A.place(x = 50, y = 50, width=70, height = 50)
ent_A.insert(0,'A')

text_A = Message(text = 'x² +')
text_A.place(x = 90, y = 5,  width = 100, height = 150)
text_A.configure(font = ('맑은고딕',25))

ent_B = Entry(font = "맑은고딕 20")
ent_B.place(x = 190, y = 50,width=120, height = 50,)
ent_B.insert(0,'B')

text_B = Message(text = 'x +')
text_B.place(x = 240, y = 5,width=100, height = 150)
text_B.configure(font = ('맑은고딕',25),padx = 20)

ent_C = Entry(font = "맑은고딕 20")
ent_C.place(x = 340, y = 50,width=100, height = 50)
ent_C.insert(0,'C')

text_C = Message(text = '= 0')
text_C.place(x = 430, y = 5,width=100, height = 150)
text_C.configure(font = ('맑은고딕',25))

text_y = Message(text='해 :')
text_y.place(x = 00, y = 100, width=70, height = 100)
text_y.configure(font = ('맑은고딕',17))

ent_result = Entry(font = '맑은고딕 30')
ent_result.place(x = 60, y = 125 , width=500, height = 50)
ent_result.insert(0,'정답이 나올 공간')

#Button

btn_cal = Button(text = '계산하기')
btn_cal.place(x = 100 ,y = 200 ,width= 150, height = 70)
btn_cal.configure(command= get_result)

btn_draw = Button(text = '그래프로 보기')
btn_draw.place(x = 300 ,y = 200 ,width= 150, height = 70)
btn_draw.configure(command=draw_graph)


#메인 루프이벤트 처리
root.mainloop()