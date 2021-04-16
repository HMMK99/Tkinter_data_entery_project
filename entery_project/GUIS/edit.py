from tkinter import Button, Label, Frame, Tk, RAISED, NSEW, Entry
import os
from functions import (only_number, verify_not_empty, change_id_edit,
                       add_in_freq, read_temp_file, delete_id)
from html_func import reinit_html
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
        self.master.title("تعديل")
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

        def make_tk_edit(line, enteries):
            n = 0
            for key, value in line.items():
                cond = ['اليوم', 'الوقت', 'دفتر', 'order', 'file_name', 'x']
                if key in cond:
                    continue
                lbl = Label(entery_frame, text=key, font=("Purisa", 18))
                lbl.grid(row=(2*n)+1, column=3)
                enteries[n].grid(row=(2*n)+1, column=1, sticky=NSEW)
                enteries[n].insert(0, value)
                n += 1

        line = read_temp_file('edit')
        file_name = line['file_name']
        print(line)

        def edit_data(line=line, filename=file_name):
            labels = ['الإسم',
                      'بطاقة علاج رقم',
                      'الرقم داخل الهيئة',
                      'القسم',
                      'محول من',
                      'اسم المسجل']

            values = [name_e.get(), hc_e.get(), id_e.get(), sec_e.get(),
                      doc_e.get(), entery_e.get()]
            id_old = line["بطاقة علاج رقم"]
            x = 0
            for label in labels:
                line[label] = values[x]
                x += 1
            if not verify_not_empty(line):
                change_id_edit(filename, line, int(line['x']))

                delete_id('دفتر التردد', id_old, new=False)
                time.sleep(1)
                add_in_freq(line, file_name.split(' ')[-1])
                reinit_html(filename)
                reinit_html("دفتر التردد")
                root.destroy()
            else:
                errlb = 'من فضلك تأكد من ادخال جميع البيانات'
                lbl = Label(entery_frame,
                            text=errlb,
                            font=("Purisa", 12),
                            bg='red', fg='white')
                lbl.grid(row=12, column=1)
                return 0

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

        # name entry column=1, sticky=NSEW)
        name_e = Entry(entery_frame, text='ادخل الاسم', width=30,
                       font=("Purisa", 18), justify='right')

        validation = root.register(only_number)
        # health card number
        hc_e = Entry(entery_frame, text='رقم بطاقة العلاج', width=30,
                     validate='key', validatecommand=(validation, '%S'),
                     font=("Purisa", 18), justify='right')

        # id in work entery
        id_e = Entry(entery_frame, text='الرقم داخل الهيئة', width=30,
                     font=("Purisa", 18), justify='right')

        # sec in work entery
        sec_e = Entry(entery_frame, text='القسم', width=30,
                      font=("Purisa", 18), justify='right')

        # From who?
        doc_e = Entry(entery_frame, text='محول من', width=30,
                      font=("Purisa", 18), justify='right')

        # who entered data?
        entery_e = Entry(entery_frame, text='اسم المسجل', width=30,
                         font=("Purisa", 18), justify='right')

        for i in range(6):
            line_break(entery_frame, (i+1)*2)

        col_break(entery_frame, row=7, col=2)
        col_break(entery_frame, row=7, col=4)

        # Frame 2
        # adding spacing in  1st row and column
        space = '\t\t\t\t'
        Label(button_frame, text=space, fg='Grey').grid(row=0,
                                                        column=0, sticky=NSEW)

        def command():
            print(doc_e.get() == '')
        # Quit Button
        quitButton = Button(button_frame, command=root.destroy,
                            text="خروج", width=20, height=2)
        quitButton.grid(row=0, column=1, sticky=NSEW)  #

        # input Button
        encryptModeButton = Button(button_frame, command=edit_data,
                                   text="تسجيل", width=20, height=2)
        encryptModeButton.grid(row=0, column=3, sticky=NSEW)  #

        line_break(button_frame, 1)
        col_break(button_frame, row=0, col=2)

        enteries = [name_e, hc_e, id_e, sec_e, doc_e, entery_e]
        make_tk_edit(line, enteries)


root = Tk()
root.geometry("+100+100")
app = Window(root)
root.mainloop()
