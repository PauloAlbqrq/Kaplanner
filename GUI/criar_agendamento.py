from tkinter import *
from customtkinter import *
from constantes import *
from tkcalendar import Calendar
from PIL import Image, ImageTk
from conexao import *
from tkinter import messagebox

root = Tk()
root.geometry('900x600')
root.resizable(False, False)
root.title(os.path.basename(__file__))
root.configure(bg=cor_bg)


def tela_evento():
    fundo_cad = Frame(root, bg=cor_fg2)
    fundo_cad.pack(fill=BOTH, expand=1, pady=10, padx=10)

    bt_evento = CTkButton(fundo_cad, text='Evento', fg_color=cor_disable, text_font=(
        'Fira Code', 15), hover_color=cor_disable)
    bt_evento.place(relx=0.05, rely=0.05, anchor=W)

    bt_meta = CTkButton(fundo_cad, text='Meta', fg_color=cor_bg, text_font=(
        'Fira Code', 15), hover_color=cor_disable)
    bt_meta.place(relx=0.25, rely=0.05, anchor=W)

    bt_tarefa = CTkButton(fundo_cad, text='Tarefa', fg_color=cor_bg, text_font=(
        'Fira Code', 15), hover_color=cor_disable)
    bt_tarefa.place(relx=0.45, rely=0.05, anchor=W)

    txt_nome = Label(fundo_cad, text='Nome:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_nome.place(relx=0.2, rely=0.2, anchor=E)
    entry_nome = CTkEntry(fundo_cad, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0, width=300,
                          text_color='black', text_font=('Fira Code', 12))
    entry_nome.place(relx=0.21, rely=0.2, anchor=W)

    txt_desc = Label(fundo_cad, text='descrição:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_desc.place(relx=0.2, rely=0.25, anchor=NE)
    entry_desc = CTkTextbox(fundo_cad, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0,
                            width=300, height=150, text_color='black', text_font=('Fira Code', 10))
    entry_real_desc = Text(fundo_cad, bg=cor_fg1,
                           borderwidth=0, font=('Fira Code', 10))
    entry_real_desc.place(relx=0.215, rely=0.255,
                          anchor=NW, width=290, height=140)
    entry_desc.place(relx=0.21, rely=0.25, anchor=NW)

    txt_date = Label(fundo_cad, text='Data:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_date.place(relx=0.2, rely=0.55, anchor=E)

    def atualizar_ent_dt(e):
        entry_date['text'] = calendario_agd.selection_get()

    calendario_agd = Calendar(fundo_cad, background=cor_fg2, disabledbackground="black", bordercolor="black",
                              headersbackground="black", normalbackground=cor_fg1, foreground='white',
                              normalforeground='black', headersforeground='white', firstweekday='sunday',
                              showweeknumbers=False, font=('Fira Code', 10), selectbackground=cor_fg2,
                              weekendbackground=cor_fg1, weekendforeground='black', othermonthbackground=cor_disable,
                              othermonthforeground=cor_fg2, othermonthwebackground=cor_disable, othermonthweforeground=cor_fg2,
                              date_pattern='y-mm-dd')
    calendario_agd.place(anchor=W, width=230,
                         height=200, rely=0.35, relx=0.6)
    calendario_agd.bind('<<CalendarSelected>>', atualizar_ent_dt)

    entry_date = Label(fundo_cad, fg='white', bg=cor_fg2,
                       text=calendario_agd.selection_get(), font=('Fira Code', 12))
    entry_date.place(relx=0.21, rely=0.55, anchor=W)

    txt_hora = Label(fundo_cad, text='Hora:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_hora.place(relx=0.2, rely=0.65, anchor=E)
    entry_hora = CTkEntry(fundo_cad, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0,
                          width=80, text_color='black', text_font=('Fira Code', 12), placeholder_text='00:00')
    entry_hora.place(relx=0.21, rely=0.65, anchor=W)

    def fn_salvar():
        pass

    def fn_cancelar():
        root.destroy()

    salvar_bt = CTkButton(fundo_cad, text='Salvar', fg_color=cor_fg1,
                          text_color='black', text_font=('Fira Code', 15), command=fn_salvar, hover_color=cor_disable)
    salvar_bt.place(rely=0.9, relx=0.95, anchor=E)

    cancelar_bt = CTkButton(fundo_cad, text='Cancelar', fg_color=cor_fg1,
                            text_color='black', text_font=('Fira Code', 15), command=fn_cancelar, hover_color=cor_disable)
    cancelar_bt.place(rely=0.9, relx=0.75, anchor=E)


def tela_meta():
    fundo_cad = Frame(root, bg=cor_fg2)
    fundo_cad.pack(fill=BOTH, expand=1, pady=10, padx=10)

    bt_evento = CTkButton(fundo_cad, text='Evento', fg_color=cor_bg, text_font=(
        'Fira Code', 15), hover_color=cor_disable)
    bt_evento.place(relx=0.05, rely=0.05, anchor=W)

    bt_meta = CTkButton(fundo_cad, text='Meta', fg_color=cor_bg, text_font=(
        'Fira Code', 15), hover_color=cor_disable)
    bt_meta.place(relx=0.25, rely=0.05, anchor=W)

    bt_tarefa = CTkButton(fundo_cad, text='Tarefa', fg_color=cor_bg, text_font=(
        'Fira Code', 15), hover_color=cor_disable)
    bt_tarefa.place(relx=0.45, rely=0.05, anchor=W)

    txt_nome = Label(fundo_cad, text='Nome:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_nome.place(relx=0.2, rely=0.2, anchor=E)
    entry_nome = CTkEntry(fundo_cad, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0, width=300,
                          text_color='black', text_font=('Fira Code', 12))
    entry_nome.place(relx=0.21, rely=0.2, anchor=W)

    txt_desc = Label(fundo_cad, text='descrição:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_desc.place(relx=0.2, rely=0.25, anchor=NE)
    entry_desc = CTkTextbox(fundo_cad, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0,
                            width=300, height=150, text_color='black', text_font=('Fira Code', 10))
    entry_real_desc = Text(fundo_cad, bg=cor_fg1,
                           borderwidth=0, font=('Fira Code', 10))
    entry_real_desc.place(relx=0.215, rely=0.255,
                          anchor=NW, width=290, height=140)
    entry_desc.place(relx=0.21, rely=0.25, anchor=NW)

    txt_date = Label(fundo_cad, text='Data:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_date.place(relx=0.2, rely=0.55, anchor=E)

    def atualizar_ent_dt(e):
        entry_date['text'] = calendario_agd.selection_get()

    calendario_agd = Calendar(fundo_cad, background=cor_fg2, disabledbackground="black", bordercolor="black",
                              headersbackground="black", normalbackground=cor_fg1, foreground='white',
                              normalforeground='black', headersforeground='white', firstweekday='sunday',
                              showweeknumbers=False, font=('Fira Code', 10), selectbackground=cor_fg2,
                              weekendbackground=cor_fg1, weekendforeground='black', othermonthbackground=cor_disable,
                              othermonthforeground=cor_fg2, othermonthwebackground=cor_disable, othermonthweforeground=cor_fg2,
                              date_pattern='y-mm-dd')
    calendario_agd.place(anchor=W, width=230,
                         height=200, rely=0.35, relx=0.6)
    calendario_agd.bind('<<CalendarSelected>>', atualizar_ent_dt)

    entry_date = Label(fundo_cad, fg='white', bg=cor_fg2,
                       text=calendario_agd.selection_get(), font=('Fira Code', 12))
    entry_date.place(relx=0.21, rely=0.55, anchor=W)

    txt_hora = Label(fundo_cad, text='Hora:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_hora.place(relx=0.2, rely=0.65, anchor=E)
    entry_hora = CTkEntry(fundo_cad, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0,
                          width=80, text_color='black', text_font=('Fira Code', 12), placeholder_text='00:00')
    entry_hora.place(relx=0.21, rely=0.65, anchor=W)

    def fn_salvar():
        pass

    def fn_cancelar():
        root.destroy()

    salvar_bt = CTkButton(fundo_cad, text='Salvar', fg_color=cor_fg1,
                          text_color='black', text_font=('Fira Code', 15), command=fn_salvar, hover_color=cor_disable)
    salvar_bt.place(rely=0.9, relx=0.95, anchor=E)

    cancelar_bt = CTkButton(fundo_cad, text='Cancelar', fg_color=cor_fg1,
                            text_color='black', text_font=('Fira Code', 15), command=fn_cancelar, hover_color=cor_disable)
    cancelar_bt.place(rely=0.9, relx=0.75, anchor=E)


def tela_tarfa():
    fundo_cad = Frame(root, bg=cor_fg2)
    fundo_cad.pack(fill=BOTH, expand=1, pady=10, padx=10)

    bt_evento = CTkButton(fundo_cad, text='Evento', fg_color=cor_bg, text_font=(
        'Fira Code', 15), hover_color=cor_disable)
    bt_evento.place(relx=0.05, rely=0.05, anchor=W)

    bt_meta = CTkButton(fundo_cad, text='Meta', fg_color=cor_bg, text_font=(
        'Fira Code', 15), hover_color=cor_disable)
    bt_meta.place(relx=0.25, rely=0.05, anchor=W)

    bt_tarefa = CTkButton(fundo_cad, text='Tarefa', fg_color=cor_bg, text_font=(
        'Fira Code', 15), hover_color=cor_disable)
    bt_tarefa.place(relx=0.45, rely=0.05, anchor=W)

    txt_nome = Label(fundo_cad, text='Nome:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_nome.place(relx=0.2, rely=0.2, anchor=E)
    entry_nome = CTkEntry(fundo_cad, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0, width=300,
                          text_color='black', text_font=('Fira Code', 12))
    entry_nome.place(relx=0.21, rely=0.2, anchor=W)

    txt_desc = Label(fundo_cad, text='descrição:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_desc.place(relx=0.2, rely=0.25, anchor=NE)
    entry_desc = CTkTextbox(fundo_cad, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0,
                            width=300, height=150, text_color='black', text_font=('Fira Code', 10))
    entry_real_desc = Text(fundo_cad, bg=cor_fg1,
                           borderwidth=0, font=('Fira Code', 10))
    entry_real_desc.place(relx=0.215, rely=0.255,
                          anchor=NW, width=290, height=140)
    entry_desc.place(relx=0.21, rely=0.25, anchor=NW)

    txt_date = Label(fundo_cad, text='Data:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_date.place(relx=0.2, rely=0.55, anchor=E)

    def atualizar_ent_dt(e):
        entry_date['text'] = calendario_agd.selection_get()

    calendario_agd = Calendar(fundo_cad, background=cor_fg2, disabledbackground="black", bordercolor="black",
                              headersbackground="black", normalbackground=cor_fg1, foreground='white',
                              normalforeground='black', headersforeground='white', firstweekday='sunday',
                              showweeknumbers=False, font=('Fira Code', 10), selectbackground=cor_fg2,
                              weekendbackground=cor_fg1, weekendforeground='black', othermonthbackground=cor_disable,
                              othermonthforeground=cor_fg2, othermonthwebackground=cor_disable, othermonthweforeground=cor_fg2,
                              date_pattern='y-mm-dd')
    calendario_agd.place(anchor=W, width=230,
                         height=200, rely=0.35, relx=0.6)
    calendario_agd.bind('<<CalendarSelected>>', atualizar_ent_dt)

    entry_date = Label(fundo_cad, fg='white', bg=cor_fg2,
                       text=calendario_agd.selection_get(), font=('Fira Code', 12))
    entry_date.place(relx=0.21, rely=0.55, anchor=W)

    txt_hora = Label(fundo_cad, text='Hora:', fg='white',
                     bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
    txt_hora.place(relx=0.2, rely=0.65, anchor=E)
    entry_hora = CTkEntry(fundo_cad, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0,
                          width=80, text_color='black', text_font=('Fira Code', 12), placeholder_text='00:00')
    entry_hora.place(relx=0.21, rely=0.65, anchor=W)

    def fn_salvar():
        pass

    def fn_cancelar():
        root.destroy()

    salvar_bt = CTkButton(fundo_cad, text='Salvar', fg_color=cor_fg1,
                          text_color='black', text_font=('Fira Code', 15), command=fn_salvar, hover_color=cor_disable)
    salvar_bt.place(rely=0.9, relx=0.95, anchor=E)

    cancelar_bt = CTkButton(fundo_cad, text='Cancelar', fg_color=cor_fg1,
                            text_color='black', text_font=('Fira Code', 15), command=fn_cancelar, hover_color=cor_disable)
    cancelar_bt.place(rely=0.9, relx=0.75, anchor=E)


tela_evento()

root.mainloop()
