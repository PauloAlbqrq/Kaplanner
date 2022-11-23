from tkinter import *
from customtkinter import *
import datetime
import os

dia = datetime.datetime.now().strftime('%d')
cor_bg='#0f0c24'
cor_fg1='#e2daf8'
cor_fg2='#686295'
cor_disable='#a7a0ba'

def debug_win():
    root=Tk()
    try:
        root.iconbitmap(f'assets/icones_dias/{dia}.ico')
    except:
        pass
    root.geometry('1280x720')
    root.configure(bg=cor_bg)
    return root