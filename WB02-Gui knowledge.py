from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random #import module

no2d = random.randint(00, 99) #สุ่มเลข 00-99
no3d = random.randint(00, 999) #สุ่มเลข 000-999
store = ['คุณจะมีเกณฑ์ได้โชคลาภหรือโชคดีต่างๆ','ทรัพย์และโชคของคุณยังมีความติดขัด','ยังมีอุปสรรคในเรื่องทรัพย์และโชค']

GUI = Tk()
GUI.title('โปรแกรม "ถ้าไม่รวยเดือนนี้ ก็ยังมีเดือนหน้า"')#ชื่อโปรแกรม
GUI.geometry('500x400')#ขนาดโปรแกรม

def Button1():
    text = (no2d)#ใช้ตัวสุ่มเลข 00-99
    messagebox.showinfo('เลขท้าย 2 ตัว',text)
    
FB1 = LabelFrame(GUI,text='อธิษฐานก่อนกด',fg='red')
FB1.place(x=50,y=50)
B2 = ttk.Button(FB1,text='เลขท้าย 2 ตัว?',command=Button1)
B2.pack(ipadx=10,ipady=20,padx=30,pady=30)

def Button2():
    text = (no3d)#ใช้ตัวสุ่มเลข 000-999
    messagebox.showinfo('คำตอบที่สอง',text)

FB2 = LabelFrame(GUI,text='กลั้นหายใจก่อนจิ้ม',fg='green')
FB2.place(x=300,y=50)
B2 = ttk.Button(FB2,text='เลขท้าย 3 ตัว?',command=Button2)
B2.pack(ipadx=10,ipady=20,padx=30,pady=30)

def Button3():
    text = random.choice(store)
    messagebox.showinfo('ถ้าไม่รวยเดือนนี้ ก็ยังมีเดือนหน้า',text)

FB3 = LabelFrame(GUI,text='งวดนี้คุณจะ.......',fg='blue')
FB3.place(x=150,y=200)
B2 = ttk.Button(FB3,text='ดวงของคุณอยู่ในระดับ?',command=Button3)
B2.pack(ipadx=20,ipady=20,padx=30,pady=30)

GUI.mainloop()



