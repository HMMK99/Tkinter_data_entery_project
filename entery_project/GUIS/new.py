from tkinter import Button, Label, Frame, Tk, RAISED, NSEW, Entry
import os
from functions import (add_as_dict, check_file_exists, verify_not_empty,
                       add_in_freq, only_number)
from html_func import update_table
from datetime import datetime
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))


class Window(Frame):  # All the stuff for the GUI

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # self.master.minsize(width=400, height=200)
        self.configure(relief=RAISED, borderwidth=10)  #
        self.init_window()
        self.grid(sticky=NSEW)  #

    def init_window(self):
        self.master.title("إضافة جديد شخصي")
        # configure weights; note: that action need for each container!
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        for i in range(5):
            self.columnconfigure(i, weight=1)

        def line_break(root, row):
            Label(root, text="").grid(row=row, column=1)

        def col_break(root, row, col):
            Label(root, text=' ').grid(row=row, column=col)

        def add_new():
            # getting the path
            x = '../الدفاتر/دفتر الجديد شخصي'
            path = os.path.join(x)
            # getting the time and formating it
            x = datetime.now()
            day = '{}-{}-{}'.format(x.year, x.month, x.day)
            timing = '{}:{}'.format(x.hour, x.minute)
            # define labels and values and adding them to dictionary
            labels = ['الإسم',
                      'بطاقة علاج رقم',
                      'الرقم داخل الهيئة',
                      'القسم',
                      'اليوم',
                      'الوقت',
                      'محول من',
                      'اسم المسجل']
            values = [name_e.get(), hc_e.get(), id_e.get(), sec_e.get(),
                      day, timing, doc_e.get(), entery_e.get()]
            line = dict(zip(labels, values))

            # verify that all fields aren't empty
            if verify_not_empty(line):
                errlb = 'من فضلك تأكد من ادخال جميع البيانات'
                lbl = Label(entery_frame,
                            text=errlb,
                            font=("Purisa", 12),
                            bg='red', fg='white')
                lbl.grid(row=12, column=1)
                return 0

            # if the file exists print rows, if not print messag
            if check_file_exists(path):
                add_as_dict(path, line)
                add_in_freq(line, 'شخصي')
                update_table(line, "دفتر الجديد شخصي", new=True)
                line['دفتر'] = 'شخصي'
                update_table(line, "دفتر التردد")
                time.sleep(0.2)
                root.destroy()
            else:
                err_lbl = 'تأكد من وجود دفتر الجديد شخصي في ملف "الدفاتر"'
                lbl = Label(entery_frame,
                            text=err_lbl,
                            font=("Purisa", 12))
                lbl.grid(row=8, column=1)

        # making 2 frames
        entery_frame = Frame(self)
        button_frame = Frame(self)
        entery_frame.pack(side="top", fill="both", expand=True)
        button_frame.pack(side="bottom", fill="both", expand=True)

        # Frame 1
        # adding spacing in  1st row and column
        space = '\t\t\t'
        Label(entery_frame, text=space, fg='Grey').grid(row=0,
                                                        column=0, sticky=NSEW)

        # name entry
        name_e = Entry(entery_frame, text='ادخل الاسم', width=30,
                       font=("Purisa", 18), justify='right')
        name_e.grid(row=1, column=1, sticky=NSEW)
        lbl = Label(entery_frame, text='الإسم', font=("Purisa", 18))
        lbl.grid(row=1, column=3)

        # health card number
        validation = root.register(only_number)
        hc_e = Entry(entery_frame, text='رقم بطاقة العلاج', width=30,
                     validate='key', validatecommand=(validation, '%S'),
                     font=("Purisa", 18), justify='right')
        hc_e.grid(row=3, column=1, sticky=NSEW)
        lbl = Label(entery_frame, text='رقم بطاقة العلاج', font=("Purisa", 18))
        lbl.grid(row=3, column=3)

        # id in work entery
        id_e = Entry(entery_frame, text='الرقم داخل الهيئة', width=30,
                     validate='key', validatecommand=(validation, '%S'),
                     font=("Purisa", 18), justify='right')
        id_e.grid(row=5, column=1, sticky=NSEW)
        lbl = Label(entery_frame, text='الرقم داخل الهيئة',
                    font=("Purisa", 18))
        lbl.grid(row=5, column=3)

        # sec in work entery
        sec_e = Entry(entery_frame, text='القسم', width=30,
                      font=("Purisa", 18), justify='right')
        sec_e.grid(row=7, column=1, sticky=NSEW)
        lbl = Label(entery_frame, text='القسم', font=("Purisa", 18))
        lbl.grid(row=7, column=3)

        # From who?
        doc_e = Entry(entery_frame, text='محول من', width=30,
                      font=("Purisa", 18), justify='right')
        doc_e.grid(row=9, column=1, sticky=NSEW)
        lbl = Label(entery_frame, text='مُحوَل مِن', font=("Purisa", 18))
        lbl.grid(row=9, column=3)

        # who entered data?
        entery_e = Entry(entery_frame, text='اسم المسجل', width=30,
                         font=("Purisa", 18), justify='right')
        entery_e.grid(row=11, column=1, sticky=NSEW)
        lbl = Label(entery_frame, text='اسم المسجل', font=("Purisa", 18))
        lbl.grid(row=11, column=3)

        for i in range(6):
            line_break(entery_frame, (i+1)*2)

        col_break(entery_frame, row=7, col=2)
        col_break(entery_frame, row=7, col=4)

        # Frame 2
        # adding spacing in  1st row and column
        space = '\t\t\t\t'
        Label(button_frame, text=space, fg='Grey').grid(row=0,
                                                        column=0, sticky=NSEW)

        # Quit Button
        quitButton = Button(button_frame, command=root.destroy,
                            text="خروج", width=20, height=2)
        quitButton.grid(row=0, column=1, sticky=NSEW)  #

        # input Button
        encryptModeButton = Button(button_frame, command=add_new,
                                   text="تسجيل", width=20, height=2)
        encryptModeButton.grid(row=0, column=3, sticky=NSEW)  #

        line_break(button_frame, 1)
        col_break(button_frame, row=0, col=2)


root = Tk()
root.geometry("725x500+200+100")
app = Window(root)
root.mainloop()
