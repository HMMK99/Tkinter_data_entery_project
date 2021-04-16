from tkinter import Button, Label, Frame, Tk, RAISED, NSEW, E
import os
from functions import add_in_freq
from functions import read_temp_file
from html_func import update_table
# from datetime import datetime
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
        self.master.title("تأكيد التردد")
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

        def make_tk_ffreq(line):
            n = 0
            for key, value in line.items():
                print(key)
                print(n)
                if key in ["اسم المسجل", "محول من"]:
                    continue
                lbl = Label(entery_frame, text=key, font=("Purisa", 18))
                lbl.grid(row=(2*n)+1, column=3)
                lbl = Label(entery_frame, text=value, width=30,
                            font=("Purisa", 18))
                lbl.grid(row=(2*n)+1, column=1, sticky=E)
                n += 1

        def add_freq():
            line = read_temp_file('freq')
            file_name = line['دفتر']
            # if found print in freq
            if line:
                print('add in freq')
                add_in_freq(line, file_name)
                update_table(line, 'دفتر التردد', new=False)
                time.sleep(0.2)
                root.destroy()
            # if not print message
            else:
                lbl = Label(entery_frame,
                            text='خطأ',
                            font=("Purisa", 12), bg='red', fg='white')
                lbl.grid(row=4, column=1, sticky=NSEW)

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
        encryptModeButton = Button(button_frame,  command=add_freq,
                                   text="تسجيل", width=20, height=2)
        encryptModeButton.grid(row=0, column=3, sticky=NSEW)  #

        line_break(button_frame, 1)
        col_break(button_frame, row=0, col=2)
        line = read_temp_file('freq')
        make_tk_ffreq(line)


root = Tk()
# root.geometry("800x200+100+100")
app = Window(root)
root.mainloop()
