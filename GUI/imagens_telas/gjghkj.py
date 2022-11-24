from cProfile import label
from faulthandler import disable
from tkinter import *
from turtle import down, left, width
from customtkinter import *
from tkcalendar import *
import datetime
import os
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


dia = datetime.datetime.now().strftime('%d')
cor_bg='#0f0c24'
cor_fg1='#e2daf8'
cor_fg2='#686295'
cor_disable='#a7a0ba'
cor_preta='#000000'
cor_branca='#ffffff'

root=Tk()
root.geometry('1280x720')
root.title('Cadastro de Agendamento')
root.configure(bg=cor_bg)
root.minsize(1280, 720)
root.resizable(width=True,height=True)


#frames
frame1=Frame(root, width=1280, height=720, bg=cor_bg)
frame1.pack(fill= BOTH, expand=1)
def frmEvent():
    global frameEvent
    frameEvent=Frame(frame1, width= 900, height=500, bg=cor_fg1)
    frameEvent.place(relx=0.5, rely=0.5, anchor=CENTER)
    frameEvent1=Frame(frameEvent, width=400, height=500, bg=cor_fg1)
    frameEvent1.place(relx=0, rely=0)
    tituEvent=Label(frameEvent1, text='Título:', font=('Fira Code Bold',14), bg=cor_fg1)
    tituEvent.place(relx=0.1, rely=0.1)
    descEvent=Label(frameEvent1, text='Descrição:', font=('Fira Code Bold',14), bg=cor_fg1)
    descEvent.place(relx=0.1, rely=0.2)
    dataEvent=Label(frameEvent1, text='Data:', font=('Fira Code Bold',14), bg=cor_fg1)
    dataEvent.place(relx=0.1, rely=0.3)
    '''entryData=CTkEntry(frameEvent1, placeholder_text='DD/MM/AAAA', width=95, height=20, corner_radius=0)
    entryData.place(relx=0.23, rely=0.31)'''
    entryDesc=CTkEntry(frameEvent1, placeholder_text='BLÁBLÁBLÁBLÁBLÁ BLÁBLÁ BLÁ BLÁ', width=230, height=20, corner_radius=0)
    entryDesc.place(relx=0.35, rely=0.21)
    entryTitu= CTkEntry(frameEvent1, placeholder_text='Evento blábláblá', width=120, height=20, corner_radius=0)
    entryTitu.place(relx=0.25, rely=0.11)
    calendar= Calendar(frameEvent1, background=cor_fg1, disabledbackground='black', bordercolor='black', 
                        headersbackground=cor_fg1, foreground='white', normalforeground='black', headersforeground='white', 
                        firstweekday='sunday', showweeknumbers=False, font=('Fira Code Bold', 10), selectbackground=cor_fg2,
                        weekendbackground=cor_fg1, weekendforeground='black', othermonthbackground=cor_disable,
                        othermonthforeground=cor_fg2, othermonthwebackground=cor_disable, othermonthweforeground=cor_fg2,
                        date_pattern='y-mm-dd', year=int(date.split(sep='-')[0]), month=int(date.split(sep='-')[1]), day=int(date.split(sep='-')[2]))
    calendar.place(anchor=W, width=23, height=20, relx=0.23, rely=0.31) 
def frmTema():
    global frameMeta
    frameMeta=Frame(frame1, width= 900, height=500, bg=cor_fg1)
    frameMeta.place(relx=0.5, rely=0.5, anchor=CENTER)
def frmPraz():
    global framePraz
    framePraz=Frame(frame1, width= 900, height=500, bg=cor_fg1)
    framePraz.place(relx=0.5, rely=0.5, anchor=CENTER)
#commands
def destruirE():
    frameEvent.destroy()
def destruirM():
    frameMeta.destroy()
def destruirP():
    framePraz.destroy()
#buttons
butEvent=CTkButton(frame1, width= 70, height=40,fg_color=cor_fg2, text='Criar Evento', text_font=('FIra Code Bold', 15), command=frmEvent, corner_radius=20)
butEvent.place(relx=0.3, rely=0.09, anchor= CENTER)
butPraz=CTkButton(frame1, width= 70, height=40,fg_color=cor_fg2, text='Criar Prazo', text_font=('FIra Code Bold', 15), command=frmPraz, corner_radius=20)
butPraz.place(relx=0.7, rely=0.09, anchor=CENTER)
butMeta=CTkButton(frame1, width=70, height=40, fg_color=cor_fg2, text='Criar Tema', text_font=('FIra Code Bold', 15), command=frmTema, corner_radius=20)
butMeta.place(relx=0.5, rely=0.09, anchor= CENTER)

root.mainloop()