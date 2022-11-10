from tkinter import *
from customtkinter import *
import datetime
import os

cor_bg='#0f0c24'
cor_fg1='#e2daf8'

dia = datetime.datetime.now().strftime('%d')

root=Tk()
root.iconbitmap(f'assets/icones_dias/{dia}.ico')
root.geometry('1280x720')
root.configure(bg=cor_bg)



root.mainloop()
