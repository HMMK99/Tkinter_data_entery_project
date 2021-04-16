from tkinter import (Button, Label, Tk, Entry, Frame, N, RIDGE,
                     ttk, RIGHT)
import os
from functions import (search_date_for_search, search_id_for_search,
                       only_number)
from html_func import html_search
from time import sleep

# get_location
__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))

root = Tk()
# root.configure(bg='#DBE5F1')
root.geometry("190x200+800+250")
root.title('تاريخ')


def create_date_data_options(root, row, col):
    # creating frame for each component

    combo_frame = Frame(root)
    combo_frame.grid(row=0, column=0)

    selection_frame = Frame(root)
    selection_frame.grid(row=1, column=0)

    number_frame = Frame(selection_frame)
    number_frame.grid(row=2, column=0)

    date_frame = Frame(selection_frame)
    date_frame.grid(row=4, column=0)

    validation = root.register(only_number)

    # label details
    lbl_id = Label(number_frame, text='الرقم', font='Roboto 14')
    e_id = Entry(number_frame, validate='key',
                 validatecommand=(validation, '%S'),
                 text='الرقم داخل الهيئة', width=20)

    lbl_id.grid(row=0, column=2)
    e_id.grid(row=0, column=0)

    # date details
    lbl_d = Label(date_frame, text='اليوم', font='Roboto 14')
    e_d = Entry(date_frame, validate='key', validatecommand=(validation, '%S'),
                text='ادخل اليوم', width=8)
    lbl_m = Label(date_frame, text='الشهر', font='Roboto 14')
    e_m = Entry(date_frame, validate='key', validatecommand=(validation, '%S'),
                text='ادخل الشهر', width=8)
    lbl_y = Label(date_frame, text='السنة', font='Roboto 14')
    e_y = Entry(date_frame, validate='key', validatecommand=(validation, '%S'),
                text='ادخل السنة', width=8)

    lbl_d.grid(row=0, column=3)
    e_d.grid(row=0, column=2)
    lbl_m.grid(row=2, column=3)
    e_m.grid(row=2, column=2)
    lbl_y.grid(row=4, column=3)
    e_y.grid(row=4, column=2)

    Label(date_frame, text='  ',
          fg='#DBE5F1').grid(row=4, column=1)
    # create the combo box

    def create_search_combobox(root, row, col):
        comb = ttk.Combobox(root, font='Roboto 14', exportselection=0,
                            justify=RIGHT, width=12)
        comb['values'] = ("دفتر التردد", "دفتر الجديد شخصي",
                          "دفتر الجديد معاشات", "دفتر الجديد أعباء")
        comb.current(1)
        comb.grid(column=col, row=row)
        return comb

    datafile_name = create_search_combobox(combo_frame, 0, col)
    Label(date_frame, text='    ', font='Roboto 14',).grid(row=5, column=0)

    # e_d.get(), e_m.get(), e_y.get(),

    def get_values():
        if e_d.get() and e_m.get() and e_y.get():
            date = e_y.get()+'-'+e_m.get()+'-'+e_d.get()
            data = search_date_for_search(datafile_name.get(),
                                          date)
            name = datafile_name.get() + ' ' + date
            new = not (datafile_name.get() == "دفتر التردد")
            html_search(data, name, new=new)
            sleep(0.5)
            root.destroy()
        if e_id.get():
            data = search_id_for_search(datafile_name.get(), e_id.get())
            name = datafile_name.get() + ' ' + e_id.get()
            new = not (datafile_name.get() == "دفتر التردد")
            html_search(data, name, new=new)
            sleep(0.5)
            root.destroy()
    Button(date_frame, text='بحث', command=get_values,
           font='Roboto 14', bg='#CCCCCC').grid(row=5, column=1)


Label(root, text='  ').grid(row=0, column=0)
opt_frame = Frame(root, borderwidth=0, relief=RIDGE)
opt_frame.grid(row=0, column=4, sticky=N)
create_date_data_options(opt_frame, 0, 0)

# create_file_dropdown(root, 0, 0)
root.mainloop()
