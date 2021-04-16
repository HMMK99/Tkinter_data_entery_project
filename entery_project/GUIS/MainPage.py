from tkinter import Tk, Label, Button, Canvas, PhotoImage, N, NW
import os
from subprocess import call
import sys
from html_func import init_html
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))

root = Tk()
root.geometry('800x600+250+60')
root.minsize(width=1, height=1)
root.configure(bg='Indigo')
root.title('دفاتر')
space = '\t\t\t\t'
for i in range(20):
    Label(root, text='', fg='Indigo', bg='Indigo').grid(column=0, row=i)
Label(root, text=space, fg='Indigo', bg='Indigo').grid(column=0,
                                                       row=21)
Label(root, text=space, fg='Indigo', bg='Indigo').grid(column=2,
                                                       row=0)


def open_del():
    path = os.path.join(__location__, 'delete.py')
    call([sys.executable, path])


def open_del_freq():
    path = os.path.join(__location__, 'delete_freq.py')
    call([sys.executable, path])


def open_new():
    path = os.path.join(__location__, 'new.py')
    call([sys.executable, path])


def open_new_m3a4():
    path = os.path.join(__location__, 'new_m3a4.py')
    call([sys.executable, path])


def open_new_a3ba2():
    path = os.path.join(__location__, 'new_a3ba2.py')
    call([sys.executable, path])


def open_edit_freq():
    path = os.path.join(__location__, 'freq_edit_init.py')
    call([sys.executable, path])


def open_freq():
    path = os.path.join(__location__, 'freq.py')
    call([sys.executable, path])


def open_hist():
    path = os.path.join(__location__, 'search_components.py')
    call([sys.executable, path])


def open_edit():
    path = os.path.join(__location__, 'edit_init.py')
    call([sys.executable, path])


init_html()

time.sleep(2)


Button(root, text='إضافة جديد', command=open_new, font=('Arial Bold', 18),
       width=25).grid(column=1, row=3)
Button(root, text='إضافة تردد', command=open_freq, font=('Arial Bold', 18),
       width=25).grid(column=1, row=5)
Button(root, text='بحث عن تاريخ', command=open_hist,
       font=('Arial Bold', 12), width=8).grid(column=0, row=1)
Button(root, text='تعديل الجديد', command=open_edit,
       font=('Arial Bold', 18), width=25).grid(column=1, row=7)
Button(root, text='تعديل التردد', command=open_edit_freq,
       font=('Arial Bold', 18), width=25).grid(column=1, row=9)
Button(root, text='حذف تسجيل جديد', command=open_del,
       font=('Arial Bold', 18), width=25).grid(column=1, row=11)
Button(root, text='حذف تسجيل تردد', command=open_del_freq,
       font=('Arial Bold', 18), width=25).grid(column=1, row=13)

canvas = Canvas(root, width=160, height=60)
canvas.grid(column=2, row=1)
img = PhotoImage()
canvas.create_image(0, 0, anchor=NW, image=img)
lbl = Label(root, text="مَركَز العِلاج الطَبيعي", font='Roboto 16',
            bg='Indigo', fg='white', anchor='e')
lbl.grid(column=2, row=2, sticky=N)

root.mainloop()
