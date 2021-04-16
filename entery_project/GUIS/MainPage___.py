from tkinter import (Tk, Label, Button, Frame, X, RIGHT, Toplevel)
import os
from subprocess import call
import sys
from html_func import init_html
import time
from navbar import create_nav

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))

body_clr = '#E5E5E5'

root = Tk()
root.geometry("1350x690+5+5")
root.minsize(width=1, height=1)
root.configure(bg=body_clr)
root.title('دفاتر مركز العلاج الطبيعي بقناة السويس')


def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


top = Toplevel(root)
root.overrideredirect(True)  # turns off title bar, geometry


def onRootIconify(event): top.withdraw()


root.bind("<Unmap>", onRootIconify)


def onRootDeiconify(event): top.deiconify()


root.bind("<Map>", onRootDeiconify)


window = Frame(master=top)

title_clr = '#1F1F26'
# make a frame for the title bar
title_bar = Frame(root, bg=title_clr, relief='raised', bd=2)

# put a close button on the title bar
close_button = Button(title_bar, bg='#D8434C', text='X', command=root.destroy)
title_lbl = Label(title_bar, text='دفاتر مركز العلاج الطبيعي بقناة السويس',
                  bg=title_clr, fg=body_clr)

# pack the widgets
title_bar.pack(expand=1, fill=X)
close_button.pack(side=RIGHT)
title_lbl.pack(side=RIGHT)

# bind title bar motion to the move window function
title_bar.bind('<B1-Motion>', move_window)


def open_del():
    path = os.path.join(__location__, 'delete.py')
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


upper_part_frame = Frame(root, bg=title_clr)
upper_part_frame.pack(side="top", fill="both", expand=True)

# creating the nav bar
nav_bar_frame = Frame(upper_part_frame, bg=title_clr)
nav_bar_frame.grid(row=0, column=0)
create_nav(nav_bar_frame)

# creating page content frame
entery_part_frame = Frame(root, bg=body_clr)
entery_part_frame.pack(side="bottom", expand=True)

space = '\t\t\t'
for i in range(20):
    Label(entery_part_frame, text='', fg=body_clr,
          bg=body_clr).grid(column=2, row=i)
    Label(entery_part_frame, text=space, fg=body_clr,
          bg=body_clr).grid(column=2, row=0)


init_html()

time.sleep(2)
btn_clr = '#383845'
txt_clr = body_clr
w = 22
h = 2

Button(entery_part_frame, text='إضافة جديد شخصي', bg=btn_clr, height=h,
       command=open_new, font=('Arial Bold', 18), fg=txt_clr,
       width=w).grid(column=3, row=3)
Button(entery_part_frame, text='إضافة جديد معاش', bg=btn_clr, height=h,
       command=open_new_m3a4, font=('Arial Bold', 18), fg=txt_clr,
       width=w).grid(column=3, row=5)
Button(entery_part_frame, text='إضافة جديد أعباء', bg=btn_clr, height=h,
       command=open_new_a3ba2, font=('Arial Bold', 18), fg=txt_clr,
       width=w).grid(column=3, row=7)
Button(entery_part_frame, text='إضافة تردد', bg=btn_clr, height=h,
       command=open_freq, font=('Arial Bold', 18), fg=txt_clr,
       width=w).grid(column=3, row=9)
Button(entery_part_frame, text='بحث عن تاريخ',  bg=btn_clr, height=h,
       command=open_hist, font=('Arial Bold', 18), fg=txt_clr,
       width=w).grid(column=1, row=3)
Button(entery_part_frame, text='تعديل الجديد', bg=btn_clr, height=h,
       command=open_edit, font=('Arial Bold', 18), fg=txt_clr,
       width=w).grid(column=1, row=5)
Button(entery_part_frame, text='تعديل التردد', bg=btn_clr, height=h,
       command=open_edit_freq, font=('Arial Bold', 18), fg=txt_clr,
       width=w).grid(column=1, row=7)
Button(entery_part_frame, text='حذف تسجيل', bg=btn_clr, height=h,
       command=open_del, font=('Arial Bold', 18), fg=txt_clr,
       width=w).grid(column=1, row=9)

root.mainloop()
