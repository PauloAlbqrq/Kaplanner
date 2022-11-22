from tkinter import *
from customtkinter import *
from constantes import *
from tkcalendar import Calendar
from PIL import Image, ImageTk

root = debug_win()
root.title(os.path.basename(__file__))


def ins_lista_agend():
    agend_scr = Frame(root, bg=cor_bg, width=20, height=20)
    agend_scr.pack(fill=BOTH, expand=1)

    lado_esq = Frame(agend_scr)
    lado_esq.grid(column=0, sticky=NSEW)
    lista_canvas = Canvas(lado_esq, bg='red')
    lista_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    lista_esq = Frame(lista_canvas, bg=cor_fg2)
    lista_canvas.create_window(
        (0, 0), window=lista_esq, anchor='nw', width=380)
    #lista_esq.pack(fill=BOTH, expand=1)

    agend_scr.columnconfigure(0, weight=0)
    agend_scr.columnconfigure(1, weight=1)
    agend_scr.rowconfigure(0, weight=1)

    cal = Calendar(agend_scr, background=cor_fg2, disabledbackground="black", bordercolor="black",
                   headersbackground="black", normalbackground=cor_fg1, foreground='white',
                   normalforeground='black', headersforeground='white', firstweekday='sunday',
                   showweeknumbers=False, font=('Fira Code', 15), selectbackground=cor_fg2,
                   weekendbackground=cor_fg1, weekendforeground='black', othermonthbackground=cor_disable,
                   othermonthforeground=cor_fg2, othermonthwebackground=cor_disable, othermonthweforeground=cor_fg2,)
    cal.grid(column=1, row=0, sticky=NSEW, padx=20, pady=50)

    add_agd = Frame(lista_esq, bg=cor_fg2, height=60)
    add_agd.pack(fill='x')

    plus_btn = CTkButton(add_agd, text='+', border_width=3, width=35, height=35, border_color='white',
                         fg_color=cor_fg2, text_font=('Fira Code Bold', 15), hover_color=cor_disable)
    plus_btn.place(rely=0.5, relx=0.1, anchor=CENTER)
    texto_add = Label(add_agd, text='Adicionar compromisso',
                      font=('Fira Code', 11), fg='white', bg=cor_fg2)
    texto_add.place(rely=0.5, relx=0.2, anchor=W)

    def pack_comp():
        bloco_comp = Frame(lista_esq, bg=cor_fg2, height=60)
        bloco_comp.pack(fill='x', anchor=N, pady=15)
        date = Label(bloco_comp, text='32/13:',
                     font=('Fira Code', 13), bg=cor_fg2, fg='white')
        date.place(relx=0.05, rely=0.3, anchor=W)
        nome = Label(bloco_comp, text='Lorem Ipsum', font=(
            'Fira Code Bold', 13), bg=cor_fg2, fg='white')
        nome.place(relx=0.05, rely=0.8, anchor=W)

        lixeira_o = Image.open(
            'assets/lixeira.png').resize((15, 15), Image.ANTIALIAS)
        lixeira_ic = ImageTk.PhotoImage(lixeira_o)

        lixeira_bt = CTkButton(bloco_comp, height=10, width=10, image=lixeira_ic,
                               text=None, fg_color=cor_fg2, hover_color=cor_fg1)
        lixeira_bt.place(relx=0.98, rely=0.8, anchor=E)

        editar_o = Image.open(
            'assets/editar.png').resize((15, 15), Image.ANTIALIAS)
        editar_ic = ImageTk.PhotoImage(editar_o)

        editar_bt = CTkButton(bloco_comp, height=10, width=10, image=editar_ic,
                              text=None, fg_color=cor_fg2, hover_color=cor_fg1)
        editar_bt.place(relx=0.90, rely=0.8, anchor=E)

    for x in range(50):
        pack_comp()
    scroll_lista = CTkScrollbar(
        lado_esq, scrollbar_color=cor_disable, fg_color=cor_fg1, orientation=VERTICAL, command=lista_canvas.yview)
    scroll_lista.pack(side=RIGHT, fill=Y)

    lista_canvas.configure(yscrollcommand=scroll_lista.set)
    lista_canvas.bind('<Configure>', lambda e: lista_canvas.configure(
        scrollregion=lista_canvas.bbox('all')))


ins_lista_agend()

root.mainloop()
