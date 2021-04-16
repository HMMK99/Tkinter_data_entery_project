from tkinter import (Button, Label, Frame, Tk, RAISED, NSEW,
                     Entry, ttk, RIGHT, E)
from functions import search_id_edit, delete_id, only_number
from subprocess import call
from html_func import reinit_html
import os
import time
import sys


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
        self.master.title("حذف")
        # configure weights; note: that action need for each container!
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)

        def line_break(root, row):
            Label(root, text="").grid(row=row, column=1)

        def col_break(root, row, col):
            Label(root, text=' ').grid(row=row, column=col)

        def open_edit():
            path = os.path.join(__location__, 'edit.py')
            call([sys.executable, path])

        def delete_row():
            # getting the path
            file_name = data_name.get()
            x = '../الدفاتر/' + file_name
            path = os.path.join(x)
            # searching for the id
            if search_id_edit(path, hc_e.get()) is False:
                lbl = Label(entery_frame,
                            text='الرقم غير موجود في تسجيل اليوم',
                            font=("Purisa", 12), bg='red', fg='white')
                lbl.grid(row=5, column=1, sticky=NSEW)
            else:
                if file_name != "دفتر التردد":
                    delete_id(file_name, hc_e.get(), new=True)
                    delete_id("دفتر التردد", hc_e.get(), new=False)
                    reinit_html(file_name)
                    reinit_html("دفتر التردد")
                else:
                    delete_id(file_name, hc_e.get(), new=False)
                    reinit_html("دفتر التردد")
                time.sleep(0.2)
                root.destroy()

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

        # create the combo box

        def create_search_combobox(root, row, col):
            comb = ttk.Combobox(root, font='Roboto 14', exportselection=0,
                                justify=RIGHT, width=12)
            comb['values'] = ("دفتر الجديد شخصي", "دفتر الجديد معاشات",
                              "دفتر الجديد أعباء")
            comb.current(1)
            comb.grid(column=col, row=row, sticky=E)
            return comb

        data_name = create_search_combobox(entery_frame, 2, 1)

        lbl = Label(entery_frame, text='اسم الدفتر',
                    font=("Purisa", 18))
        lbl.grid(row=2, column=3, sticky=NSEW)

        # health card number
        validation = root.register(only_number)
        hc_e = Entry(entery_frame, text='رقم بطاقة العلاج', width=30,
                     validate='key', validatecommand=(validation, '%S'),
                     font=("Purisa", 18), justify='right')
        hc_e.grid(row=4, column=1, sticky=NSEW)
        lbl = Label(entery_frame, text='رقم بطاقة العلاج',
                    font=("Purisa", 18))
        lbl.grid(row=4, column=3, sticky=NSEW)

        for i in range(3):
            line_break(entery_frame, (i*2)+1)

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
        encryptModeButton = Button(button_frame, command=delete_row,
                                   text="حذف", width=20, height=2)
        encryptModeButton.grid(row=0, column=3, sticky=NSEW)  #

        line_break(button_frame, 1)
        col_break(button_frame, row=0, col=2)


root = Tk()
root.geometry("725x250+250+100")
app = Window(root)
root.mainloop()
