from tkinter import *
from customtkinter import *
from constantes import *
from tkcalendar import Calendar

root = debug_win()


def ins_lista_agend():
    agend_scr = Frame(root, bg=cor_bg, width=20, height=20)
    agend_scr.pack(fill=BOTH, expand=1)

    lista_esq = Frame(agend_scr, bg=cor_fg2)
    lista_esq.grid(column=0, sticky=NSEW)

    agend_scr.columnconfigure(0, weight=4)
    agend_scr.columnconfigure(1, weight=9)
    agend_scr.rowconfigure(0, weight=1)

    cal = Calendar(agend_scr, background="black", disabledbackground="black", bordercolor="black",
                   headersbackground="black", normalbackground="black", foreground='white',
                   normalforeground='white', headersforeground='white', firstweekday='sunday', showweeknumbers=False)
    cal.config(background=cor_fg2)
    cal.grid(column=1, row=0, sticky=NSEW, padx=20, pady=50)


ins_lista_agend()

root.mainloop()
