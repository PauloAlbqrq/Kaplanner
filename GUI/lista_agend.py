from tkinter import *
from customtkinter import *
from GUI.constantes import *
from tkcalendar import Calendar
from PIL import Image, ImageTk
from GUI.conexao import *
from tkinter import messagebox

'''root = debug_win()
root.title(os.path.basename(__file__))'''


def ins_lista_agend(root):
    agend_scr = Frame(root, bg=cor_bg, width=20, height=20)
    agend_scr.pack(fill=BOTH, expand=1)

    lado_esq = Frame(agend_scr, bg=cor_fg2)
    lado_esq.grid(column=0, sticky=NSEW)
    lista_canvas = Canvas(lado_esq, bg=cor_fg2)
    lista_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    lista_esq = Frame(lista_canvas, bg=cor_fg2)
    lista_canvas.create_window(
        (0, 0), window=lista_esq, anchor='nw', width=380)
    #lista_esq.pack(fill=BOTH, expand=1)

    agend_scr.columnconfigure(0, weight=0)
    agend_scr.columnconfigure(1, weight=1)
    agend_scr.rowconfigure(0, weight=1)

    # sel_cal=StringVar('2022-11-23')

    calendario = Calendar(agend_scr, background=cor_fg2, disabledbackground="black", bordercolor="black",
                          headersbackground="black", normalbackground=cor_fg1, foreground='white',
                          normalforeground='black', headersforeground='white', firstweekday='sunday',
                          showweeknumbers=False, font=('Fira Code', 15), selectbackground=cor_fg2,
                          weekendbackground=cor_fg1, weekendforeground='black', othermonthbackground=cor_disable,
                          othermonthforeground=cor_fg2, othermonthwebackground=cor_disable, othermonthweforeground=cor_fg2,
                          date_pattern='y-mm-dd')
    calendario.grid(column=1, row=0, sticky=NSEW, padx=20, pady=50)

    add_agd = Frame(lista_esq, bg=cor_fg2, height=60)
    add_agd.pack(fill='x')

    def auto_destruir():
        agend_scr.destroy()

    plus_btn = CTkButton(add_agd, text='+', border_width=3, width=35, height=35, border_color='white',
                         fg_color=cor_fg2, text_font=('Fira Code Bold', 15), hover_color=cor_disable, command=auto_destruir)
    plus_btn.place(rely=0.5, relx=0.1, anchor=CENTER)
    texto_add = Label(add_agd, text='Adicionar compromisso',
                      font=('Fira Code', 11), fg='white', bg=cor_fg2)
    texto_add.place(rely=0.5, relx=0.2, anchor=W)

    frame_comp = Frame(lista_esq, bg=cor_fg2)
    frame_comp.pack(fill=BOTH, expand=1)

    def att_comp(e):
        data_cal = calendario.selection_get()
        for y in frame_comp.winfo_children():
            y.destroy()
        print(calendario.selection_get())
        global pri_sel
        pri_sel = True

        conexao_comp = conectar_db()
        try:
            for x in (buscar_dados(conexao_comp, f"select * from evento where data_evento = '{data_cal}';")+buscar_dados(conexao_comp, f"select * from meta where prazo = '{data_cal}';")+buscar_dados(conexao_comp, f"select * from tarefa where data_tarefa = '{data_cal}';")):
                nome_comp2 = buscar_dados(
                    conexao_comp, f"select * from compromisso where id_compromisso = {x[-1]}")[0][1]
                pack_comp(nome_comp2, x[0], x[-1])
        except:
            pass
        desconectar_db(conexao_comp)

    calendario.bind('<<CalendarSelected>>', att_comp)

    def pack_comp(nome_comp, data_comp, id_comp):
        bloco_comp = Frame(frame_comp, bg=cor_fg2, height=60)
        bloco_comp.pack(fill='x', anchor=N, pady=15)
        date = Label(bloco_comp, text=data_comp,
                     font=('Fira Code', 13), bg=cor_fg2, fg='white')
        date.place(relx=0.05, rely=0.3, anchor=W)
        nome = Label(bloco_comp, text=nome_comp, font=(
            'Fira Code Bold', 13), bg=cor_fg2, fg='white')
        nome.place(relx=0.05, rely=0.8, anchor=W)

        def delete_comp():
            confirm = messagebox.askokcancel(
                'Exclusão!', 'Este compromisso será excluído!')
            print(confirm, id_comp)
            for y in frame_comp.winfo_children():
                y.destroy()

            if confirm == True:
                ins_conn = conectar_db()
                manipular_dados(
                    ins_conn, f"delete from compromisso where id_compromisso = {id_comp}")

                manipular_dados(
                    ins_conn, f"delete from tarefa where id_compromisso = {id_comp}")
                manipular_dados(
                    ins_conn, f"delete from meta where id_compromisso = {id_comp}")
                manipular_dados(
                    ins_conn, f"delete from evento where id_compromisso = {id_comp}")
            if pri_sel == True:
                data_cal = calendario.selection_get()
                for x in (buscar_dados(ins_conn, f"select * from evento where data_evento = '{data_cal}';")+buscar_dados(ins_conn, f"select * from meta where prazo = '{data_cal}';")+buscar_dados(ins_conn, f"select * from tarefa where data_tarefa = '{data_cal}';")):
                    nome_comp2 = buscar_dados(
                        ins_conn, f"select * from compromisso where id_compromisso = {x[-1]}")[0][1]
                    pack_comp(nome_comp2, x[0], x[-1])
            else:
                for x in (buscar_dados(ins_conn, "select * from evento")+buscar_dados(ins_conn, "select * from meta")+buscar_dados(ins_conn, "select * from tarefa")):
                    nome_comp = buscar_dados(
                        ins_conn, f"select * from compromisso where id_compromisso = {x[-1]}")[0][1]
                    pack_comp(nome_comp, x[0], x[-1])
            desconectar_db(ins_conn)

        lixeira_o = Image.open(
            'assets/lixeira.png').resize((15, 15), Image.ANTIALIAS)
        lixeira_ic = ImageTk.PhotoImage(lixeira_o)
        lixeira_bt = CTkButton(bloco_comp, height=10, width=10, image=lixeira_ic,
                               text=None, fg_color=cor_fg2, hover_color=cor_fg1, command=delete_comp)
        lixeira_bt.place(relx=0.98, rely=0.8, anchor=E)

        editar_o = Image.open(
            'assets/editar.png').resize((15, 15), Image.ANTIALIAS)
        editar_ic = ImageTk.PhotoImage(editar_o)
        editar_bt = CTkButton(bloco_comp, height=10, width=10, image=editar_ic,
                              text=None, fg_color=cor_fg2, hover_color=cor_fg1, command=lambda: editar_comp_fn(id_comp))
        editar_bt.place(relx=0.90, rely=0.8, anchor=E)

    '''for x in range(50):
        pack_comp('lorem ipsum', '2022-11-22')'''

    conexao_comp = conectar_db()
    try:
        for x in (buscar_dados(conexao_comp, "select * from evento")+buscar_dados(conexao_comp, "select * from meta")+buscar_dados(conexao_comp, "select * from tarefa")):
            nome_comp = buscar_dados(
                conexao_comp, f"select * from compromisso where id_compromisso = {x[-1]}")[0][1]
            pack_comp(nome_comp, x[0], x[-1])
    except:
        pass
    desconectar_db(conexao_comp)

    scroll_lista = CTkScrollbar(
        lado_esq, scrollbar_color=cor_disable, fg_color=cor_fg1, orientation=VERTICAL, command=lista_canvas.yview)
    scroll_lista.pack(side=RIGHT, fill=Y)

    lista_canvas.configure(yscrollcommand=scroll_lista.set)
    lista_canvas.bind('<Configure>', lambda e: lista_canvas.configure(
        scrollregion=lista_canvas.bbox('all')))

    def editar_comp_fn(id_comp):
        editar_comp2 = Toplevel()
        editar_comp2.geometry('900x600')
        editar_comp2.resizable(False, False)
        editar_comp2.configure(bg=cor_bg)

        fundo_edt = Frame(editar_comp2, bg=cor_fg2)
        fundo_edt.pack(fill=BOTH, expand=1, pady=10, padx=10)

        conexao_comp = conectar_db()
        nome = buscar_dados(
            conexao_comp, f"select * from compromisso where id_compromisso = {id_comp}")[0][1]
        desc = buscar_dados(
            conexao_comp, f"select * from compromisso where id_compromisso = {id_comp}")[0][2]
        comp_sub = buscar_dados(conexao_comp, f"select * from evento where id_compromisso = {id_comp}")+buscar_dados(
            conexao_comp, f"select * from tarefa where id_compromisso = {id_comp}")+buscar_dados(conexao_comp, f"select * from meta where id_compromisso = {id_comp}")
        date = comp_sub[0][0]
        hora = comp_sub[0][1]

        titulo = Label(fundo_edt, bg=cor_fg2, text='Editar Compromisso',
                       fg='white', font=('Fira Code', 30))
        titulo.pack(side=TOP, pady=10)

        txt_nome = Label(fundo_edt, text='Nome:', fg='white',
                         bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
        txt_nome.place(relx=0.2, rely=0.2, anchor=E)
        entry_nome = CTkEntry(fundo_edt, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0, width=300,
                              textvariable=StringVar(value=nome), text_color='black', text_font=('Fira Code', 12))
        entry_nome.place(relx=0.21, rely=0.2, anchor=W)

        txt_desc = Label(fundo_edt, text='descrição:', fg='white',
                         bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
        txt_desc.place(relx=0.2, rely=0.25, anchor=NE)
        entry_desc = CTkTextbox(fundo_edt, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0,
                                width=300, height=150, text_color='black', text_font=('Fira Code', 10))
        entry_real_desc = Text(fundo_edt, bg=cor_fg1,
                               borderwidth=0, font=('Fira Code', 10))
        entry_real_desc.place(relx=0.215, rely=0.255,
                              anchor=NW, width=290, height=140)
        entry_real_desc.insert('0.0', desc)
        entry_desc.place(relx=0.21, rely=0.25, anchor=NW)

        txt_date = Label(fundo_edt, text='Data:', fg='white',
                         bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
        txt_date.place(relx=0.2, rely=0.55, anchor=E)

        def atualizar_ent_dt(e):
            entry_date['text'] = calendario_agd.selection_get()

        calendario_agd = Calendar(fundo_edt, background=cor_fg2, disabledbackground="black", bordercolor="black",
                                  headersbackground="black", normalbackground=cor_fg1, foreground='white',
                                  normalforeground='black', headersforeground='white', firstweekday='sunday',
                                  showweeknumbers=False, font=('Fira Code', 10), selectbackground=cor_fg2,
                                  weekendbackground=cor_fg1, weekendforeground='black', othermonthbackground=cor_disable,
                                  othermonthforeground=cor_fg2, othermonthwebackground=cor_disable, othermonthweforeground=cor_fg2,
                                  date_pattern='y-mm-dd', year=int(date.split(sep='-')[0]), month=int(date.split(sep='-')[1]), day=int(date.split(sep='-')[2]))
        calendario_agd.place(anchor=W, width=230,
                             height=200, rely=0.35, relx=0.6)
        calendario_agd.bind('<<CalendarSelected>>', atualizar_ent_dt)

        entry_date = Label(fundo_edt, fg='white', bg=cor_fg2,
                           text=calendario_agd.selection_get(), font=('Fira Code', 12))
        entry_date.place(relx=0.21, rely=0.55, anchor=W)

        txt_hora = Label(fundo_edt, text='Hora:', fg='white',
                         bg=cor_fg2, font=('Fira Code', 17), justify=RIGHT)
        txt_hora.place(relx=0.2, rely=0.65, anchor=E)
        entry_hora = CTkEntry(fundo_edt, fg_color=cor_fg1, bg_color=cor_fg2, border_width=0, width=80,
                              textvariable=StringVar(value=hora), text_color='black', text_font=('Fira Code', 12))
        if ':' in hora:
            entry_hora.place(relx=0.21, rely=0.65, anchor=W)

        def fn_salvar():
            if datetime.datetime.strptime(str(calendario_agd.selection_get()), "%Y-%m-%d").date() >= datetime.datetime.strptime(data_hj, "%Y-%m-%d").date():
                conexao_salvar = conectar_db()
                manipular_dados(
                    conexao_salvar, f"update compromisso set nome_compromisso='{entry_nome.get()}', desc_compromisso='{entry_real_desc.get('0.0', 'end')}' where id_compromisso={id_comp};")
                manipular_dados(
                    conexao_salvar, f"update evento set data_evento='{calendario_agd.selection_get()}', hora_evento='{entry_hora.get()}' where id_compromisso={id_comp};")
                manipular_dados(
                    conexao_salvar, f"update meta set prazo='{calendario_agd.selection_get()}' where id_compromisso={id_comp};")
                manipular_dados(
                    conexao_salvar, f"update tarefa set data_tarefa='{calendario_agd.selection_get()}', hora_tarefa='{entry_hora.get()}' where id_compromisso={id_comp};")

                for y in frame_comp.winfo_children():
                    y.destroy()

                if pri_sel == True:
                    data_cal = calendario.selection_get()
                    for x in (buscar_dados(conexao_salvar, f"select * from evento where data_evento = '{data_cal}';")+buscar_dados(conexao_salvar, f"select * from meta where prazo = '{data_cal}';")+buscar_dados(conexao_salvar, f"select * from tarefa where data_tarefa = '{data_cal}';")):
                        nome_comp2 = buscar_dados(
                            conexao_salvar, f"select * from compromisso where id_compromisso = {x[-1]}")[0][1]
                        pack_comp(nome_comp2, x[0], x[-1])
                else:
                    for x in (buscar_dados(conexao_salvar, "select * from evento")+buscar_dados(conexao_salvar, "select * from meta")+buscar_dados(conexao_salvar, "select * from tarefa")):
                        nome_comp = buscar_dados(
                            conexao_salvar, f"select * from compromisso where id_compromisso = {x[-1]}")[0][1]
                        pack_comp(nome_comp, x[0], x[-1])

                desconectar_db(conexao_salvar)
            else:
                messagebox.showinfo(
                    'erro', 'Você inseriu uma data já passada.')
                editar_comp2.focus_force()

            editar_comp2.destroy()

        def fn_cancelar():
            editar_comp2.destroy()

        salvar_bt = CTkButton(fundo_edt, text='Salvar', fg_color=cor_fg1,
                              text_color='black', text_font=('Fira Code', 15), command=fn_salvar, hover_color=cor_disable)
        salvar_bt.place(rely=0.9, relx=0.95, anchor=E)

        cancelar_bt = CTkButton(fundo_edt, text='Cancelar', fg_color=cor_fg1,
                                text_color='black', text_font=('Fira Code', 15), command=fn_cancelar, hover_color=cor_disable)
        cancelar_bt.place(rely=0.9, relx=0.75, anchor=E)

        print(data_hj)

        print(date)
        print(nome)
        print(desc)
        print(hora)


'''ins_lista_agend()

root.mainloop()'''
