from tkinter import Label
# from spacing import break_17


def create_nav(root):

    color = '#1F1F26'
    body_clr = '#E5E5E5'

    def break_logo(row, col, size):  # function for logo spacing
        lbl = Label(root, text='', width=size,
                    font='Helvetica 8 bold', bg=color)
        lbl.grid(row=row, column=col)

    break_logo(0, 0, 1)  # upper margin
    break_logo(1, 0, 121)  # left margin
    break_logo(1, 3, 15)  # right margin
    break_logo(3, 0, 1)  # lower margin
    lbl = Label(root, text="هيئة قناة السويس", font='Roboto 20 bold',
                bg=color, fg=body_clr, anchor='e', width=10)
    lbl.grid(row=1, column=2)
    lbl = Label(root, text="مَركَز العِلاج الطَبيعي", font='Roboto 16',
                bg=color, fg=body_clr, anchor='e', width=17)
    lbl.grid(row=1, column=1)
