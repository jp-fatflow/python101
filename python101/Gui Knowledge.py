from tkinter import *
from tkinter import ttk # ธีมของ tk
from tkinter import messagebox

GUI = Tk() # หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') # ชื่อโปรแกรม
GUI.geometry('500x400') # ขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้แบบปุ่ม',fg='green')
#########################################

def Button1():
    text = 'วันนี้เป็นวันจันทร์'
    messagebox.showinfo('คำตอบแรก',text)

FB1 = LabelFrame(GUI,text='คำถามแรก') #คล้ายกระดาน
FB1.place(x=50,y=50)
B2 = ttk.Button(FB1,text='วันนี้วันอะไร?',command=Button1) # ชื่อปุ่ม
B2.pack(ipadx=10,ipady=20,padx=30,pady=30)

def Button2():
    text = 'สวัสดีวันจันทร์ T_T'
    messagebox.showinfo('คำตอบที่สอง',text)

FB1 = LabelFrame(GUI,text='คำถามที่สอง') #คล้ายกระดาน
FB1.place(x=300,y=50)
B2 = ttk.Button(FB1,text='คุณรู้สึกอย่างไร?',command=Button2) # ชื่อปุ่ม
B2.pack(ipadx=10,ipady=20,padx=30,pady=30)

def Button3():
    text = 'ฉันง่วงแล้ว'
    messagebox.showinfo('คำตอบสุดท้าย',text)

FB1 = LabelFrame(GUI,text='คำถามสุดท้าย') #คล้ายกระดาน
FB1.place(x=150,y=200)
B2 = ttk.Button(FB1,text='คุณอยากจะบอกอะไร?',command=Button3) # ชื่อปุ่ม
B2.pack(ipadx=20,ipady=20,padx=30,pady=30)


GUI.mainloop()



