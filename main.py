from tkinter import *
from customtkinter import *
from GUI.constantes import *
from GUI.lista_agend import *


root=Tk()
root.iconbitmap(f'assets/icones_dias/{dia}.ico')
root.geometry('1280x720')
root.configure(bg=cor_bg)

ins_lista_agend(root)



root.mainloop()
