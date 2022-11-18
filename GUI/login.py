from tkinter import *
from customtkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter import *

#Cores:
branco = '#FFFFFF'
roxo = '#0F0C24'
lilas = '#686295'
lilas2 = '#E2DAF8'

tela = Tk()
tela.geometry('900x500')
tela.config(bg = roxo)
tela.resizable(width=True,height=True)

#IMAGENS:
icon = PhotoImage(file='imagens\\icon.png')
se = PhotoImage(file='imagens\\se.png') #d1: Superior - Esquerda
sd = PhotoImage(file='imagens\\sd.png') #d2: Superior - Direita
ine = PhotoImage(file='imagens\\ine.png') #d3: Inferior - Esquerda
ind = PhotoImage(file='imagens\\ind.png') #d4: Inferior - Direita




#DETALHES DA TELA (d1, d2, d3, d4):
d1 = Label(tela, image=se, bg=roxo)
d1.place(width=160, height=160, x=1, y=0.5)

d2 = Label(tela, image=sd, bg=roxo)
d2.place(x=726, y=2)

d3 = Label(tela, image=ine, bg=roxo)
d3.place(x=1, y=332)

d4 = Label(tela, image=ind, bg=roxo)
d4.place(x=726,y=350)

#FUNÇÃO CADASTRO:
'''def cadastro():
        
  #CONFIGURAÇÕES DE TELA:
  reg_scr = Label(tela, image=icon, bg=roxo)
  reg_scr.pack()
  
  
  
  #VARIÁVEIS:
  nomeuser = StringVar()
  sobrenome = StringVar()
  email = StringVar()
  senha = StringVar()
  
  
cadastro()'''

tela.mainloop()