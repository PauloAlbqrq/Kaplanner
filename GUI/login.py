from tkinter import *
from customtkinter import *
from constantes import *

root=debug_win()

def ins_login_screen():
    log_scr=Frame(root, bg=cor_bg, width=20, height=20)
    log_scr.pack(fill=BOTH,expand=1)

    email_ent=CTkEntry(log_scr, fg_color=cor_fg1, border_width=0, width=400, placeholder_text='exemplo@kaplanner.com', text_font=('Fira Code', 10), text_color='black', placeholder_text_color='gray')
    email_ent.place(relx=0.5, rely=0.5, anchor=CENTER)

ins_login_screen()

root.mainloop()