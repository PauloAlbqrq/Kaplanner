from tkinter import *
from customtkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter import *
from PIL import ImageTk
from conexao import *



# DEFININDO AS VARIAVÉIS DAS CORES:
branco = '#FFFFFF'
roxo = '#0F0C24'
lilas = '#686295'
lilas2 = '#E2DAF8'
preto = '#000000'
cinza = '#BBB4B4'
azul = '#38B6FF'

#DEFININDO TELA:
tela = Tk()
tela.geometry('1400x800')
tela.config(bg = roxo)
tela.resizable(width=True,height=True)

#CHAMANDO AS IMAGENS E DEFININDO SUAS VARIAVÉIS:
icon = PhotoImage(file='imagens\\icon.png') #icon
se = PhotoImage(file='imagens\\se.png') #d1: Superior - Esquerda
sd = PhotoImage(file='imagens\\sd.png') #d2: Superior - Direita
ine = PhotoImage(file='imagens\\ine.png') #d3: Inferior - Esquerda
ind = PhotoImage(file='imagens\\ind.png') #d4: Inferior - Direita
lint = PhotoImage(file='imagens\\linhaint.png') #l1: Linha inteira
linp = PhotoImage(file='imagens\\linhapnt.png') #l2: Linha pontilhada
closeeye = PhotoImage(file='imagens\\closeye.png') #Olho fechado (mascara a senha)
openeye = PhotoImage(file='imagens\\openeye.png') #Olho aberto (exibe a senha)

################ FUNÇÕES USADAS NAS TELAS DE CADASTRO E LOGIN ################

#POSICIONANDO AS IMAGENS NOS CANTOS DA TELA (d1, d2, d3, d4):
def posicionando():
  d1 = Label(tela, image=se, bg=roxo)
  d1.place(relx=0, rely=0, anchor=NW)

  d2 = Label(tela, image=sd, bg=roxo)
  d2.place(relx=1, rely=0, anchor=NE)

  d3 = Label(tela, image=ine, bg=roxo)
  d3.place(relx=0, rely=1, anchor=SW)

  d4 = Label(tela, image=ind, bg=roxo)
  d4.place(relx=1, rely=1, anchor=SE)

#EXIBIR E ESCONDER A SENHA:
##### da tela cadastro
def exibir_senha():
  closeeye.config(file='imagens\\openeye.png')
  senha_ent.configure(show='')
  botao_olho.config(command=mask)
  
def mask():
  closeeye.config(file='imagens\\closeye.png')
  senha_ent.configure(show='*')
  botao_olho.config(command=exibir_senha)

##### da tela login
def exibir_senha1():
  closeeye.config(file='imagens\\openeye.png')
  senha_ent1.configure(show='')
  botao_olho1.config(command=mask1)

def mask1():
  closeeye.config(file='imagens\\closeye.png')
  senha_ent1.configure(show='*')
  botao_olho1.config(command=exibir_senha1)

  

#COMANDO DO BOTÃO 'CADASTRAR':
def cadastrar_user():
  nomeuser_info = nomeuser.get()
  sobrenome_info = sobrenome.get()
  email_info = email.get()
  senha_info = senha.get()

  conexao_cad=conectar_db()
  manipular_dados(conexao_cad, f"""insert into usuario(nome, sobrenome, email, senha) values('{nomeuser_info}', '{sobrenome_info}', '{email_info}', '{senha_info}')""")
  desconectar_db(conexao_cad)
  
  '''cads = open('cadastros.txt','w')
  cads.write(f'{nomeuser_info}, {sobrenome_info}, {email_info}, {senha_info}')
  cads.close()'''

  
  
#FUNÇÃO CADASTRO:
def tela_cadastro():
  
  #CONFIGURAÇÕES DO FRAME DA TELA DE CADASTRO PARA ADICIONAR NA TELA PRINCIPAL (tela):
  reg_scr = Frame(tela, bg = roxo)
  reg_scr.place(relx=0.5, rely=0.38, anchor=CENTER)
  posicionando()
  #FRAME PARA ADICIONAR AS LABELS E AS ENTRYS NA TELA DE CADASTRO: (não era necesário criar esse frame, mas foi por uma escolha estética, já que não estava ficando centralizado quando redimensionava a tela) 
  dados = Frame(tela,bg=roxo) 
  dados.place(relx=0.5, rely=0.47, anchor=CENTER)
 
  #GLOBALIZANDO AS VARIÁVEIS:
  global nomeuser   
  global sobrenome
  global email
  global senha
  global nome_ent
  global sobre_ent
  global email_ent
  global senha_ent
  global botao_olho
  
  #VARIÁVEIS:
  nomeuser = StringVar()
  sobrenome = StringVar()
  email = StringVar()
  senha = StringVar()
  
  #POSICIONANDO A IMAGEM DO ICONE PADRÃO E AS LABELS QUE FICAM DO LADO DO ICONE:
  icone = Label(dados, image=icon, bg=roxo)
  icone.pack(pady=40)
  
  l1 = Label(dados, image=lint, bg=roxo)
  l1.place(relx=0.64, rely=0.15, anchor=NW)

  button_cad = CTkButton(dados, text='CADASTRO',text_font=('Fira Code', 15),border_width=0, border_color=lilas2, fg_color=roxo, text_color=branco,bg_color=roxo, width=30, height=30)
  button_cad.place(relx=0.66, rely=0.11, anchor=NW)

  l2 = Label(dados, image=linp, bg=roxo)
  l2.place(relx=0.000, rely=0.15, anchor=NW)
  
  ##teste##button_log = Button(dados, text='LOGIN', font=('Fira Code', 15), borderwidth=0, fg = branco,bg=roxo, command=tela_login, activebackground=roxo, cursor='hand2' )
  button_log = CTkButton(dados, text='LOGIN',text_font=('Fira Code', 15),border_width=0, border_color=lilas2, fg_color=roxo, text_color=branco,bg_color=roxo, width=30, height=30, command=tela_login)
  button_log.place(relx=0.07, rely=0.11, anchor=NW)
  
  #ENTRYS, LABELS E BOTÕES:
  #Orde de definição: 
  # - Label: frame a ser inserido, variável, texto, fonte(estilo, tamanho), cor de fundo, cor da fonte.
  # - Entry: frame a ser inserido, variável, fonte(estilo, tamanho), cor de fundo da entry, tamanho da borda, tamanho da caixa, altura da caixa.
  # *Foi usado place para as Labels e o pack para as entrys.
  #NOME:
  #Label:
  nome_lab=Label(dados, text = 'NOME', font=('Fira Code', 15), bg = roxo, fg = branco)
  nome_lab.place(x=32, y=186, anchor=CENTER)
  nono = Label(dados, text='*', font=('Fira Code', 15), bg = roxo, fg = 'red') #Não dava para colocar um texto com cor diferente na mesma label, então para o * ser vermelho foi preciso criar outra label só pra ele
  nono.place(x=75, y=186, anchor=CENTER)
  #Entry:
  nome_ent=CTkEntry(dados, textvariable=nomeuser, text_font=('Fira Code', 14),fg_color=lilas, border_width=0, width=400, height=35)
  nome_ent.pack(pady=10, anchor=CENTER)
  
  
  #SOBRENOME:
  #Label:
  sobre_lab=Label(dados, text = 'SOBRENOME', font=('Fira Code',15), bg = roxo, fg = branco)
  sobre_lab.place(x=65, y=272, anchor=CENTER)
  soso = Label(dados, text='*', font=('Fira Code', 15), bg = roxo, fg = 'red')
  soso.place(x=145, y=272, anchor=CENTER)
  #Entry:
  sobre_ent=CTkEntry(dados, textvariable=sobrenome, text_font=('Fira Code', 14), fg_color=lilas, border_width=0, width=400, height=35)
  sobre_ent.pack(pady=40,anchor=CENTER)
  
  
  #E-MAIL:
  #Label:
  email_lab=Label(dados, text = 'E-MAIL', font=('Fira Code',15), bg = roxo, fg = branco)
  email_lab.place(x=36, y=355, anchor=CENTER)
  emem = Label(dados, text='*', font=('Fira Code', 15), bg = roxo, fg = 'red')
  emem.place(x=84, y=355, anchor=CENTER)
  #Entry:
  email_ent=CTkEntry(dados, textvariable=email, text_font=('Fira Code', 14), text_color=branco, fg_color=lilas,border_width=0, width=400, height=35)
  email_ent.pack(pady=10, anchor=CENTER)
  
  
  #SENHA:
  #Label:
  senha_lab=Label(dados, text = 'SENHA', font=('fira code',15), bg = roxo, fg = branco)
  senha_lab.place(x=33, y=442, anchor=CENTER)
  sese = Label(dados, text='*', font=('Fira Code', 15), bg = roxo, fg = 'red')
  sese.place(x=80, y=442, anchor=CENTER)
  #Entry:
  senha_ent=CTkEntry(dados, textvariable=senha, text_font=('Fira Code', 14), fg_color=lilas, border_width=0, width=400, height=35,show='*')
  senha_ent.pack(pady=40, anchor=CENTER)
  #Botão olho:
  botao_olho = Button(dados, image=closeeye, bd=0, bg=lilas, activebackground=lilas, cursor='hand2', command=exibir_senha)
  botao_olho.place(x=360, y=460)
  
  
  #SALVAR CADASTRO
  button_cad1 = CTkButton(dados, text='CADASTRAR',text_font=('Fira Code', 14),border_width=1, border_color=lilas2, fg_color=roxo, text_color=branco,bg_color=roxo, width=30, height=30, command=lambda:[cadastrar_user(), tela_login()]) #O botão "CADASTRAR" recebe dois comando, o de cadastrar o usuário no bd e enviar o usuário para a tela de login.
  button_cad1.pack(anchor=CENTER)
  
  #LINHA:
  ######################
  ou=Label(dados,text='''---------------------- OU ----------------------
           
           ''',font= ('Fira Code', 14), fg = lilas, bg=roxo)
  ou.pack(pady=5, anchor=CENTER)
  ######################
  
  #Já possui cadastro?
  possui=Label(dados, text='Já possui cadastro?', font=('fira code',14), bg = roxo, fg = branco)
  possui.place(x=75, y=596)
  
  #Botão "Login" em azul que direciona o usuário para a página de login:
  button_possui=CTkButton(dados, text='Login',text_font=('Fira Code', 14),border_width=0, fg_color=roxo, text_color=azul,bg_color=roxo, width=30, height=30, command=tela_login)
  button_possui.place(x=250, y=594)
  
  
  
#FUNÇÃO LOGIN:
def tela_login():
  global senha_ent1
  global botao_olho1
      
  log_scr = Frame(tela, bg=roxo)
  log_scr.pack(fill='both', expand=1)
  posicionando()
  dados1 = Frame(log_scr, bg=roxo)
  dados1.place(relx=0.5, rely=0.37, anchor=CENTER)
  
  
  icone = Label(dados1, image=icon, bg=roxo)
  icone.pack(pady=40)
  
  l1 = Label(dados1, image=linp, bg=roxo)
  l1.place(relx=0.64, rely=0.19, anchor=NW)

  def logtocad():
    log_scr.destroy()
    tela_cadastro()

  button_cad = CTkButton(dados1, text='CADASTRO',text_font=('Fira Code', 15),border_width=0, border_color=lilas2, fg_color=roxo, text_color=branco,bg_color=roxo, width=30, height=30, command=logtocad)
  button_cad.place(relx=0.66, rely=0.14, anchor=NW)

  l2 = Label(dados1, image=lint, bg=roxo)
  l2.place(relx=0.0000100, rely=0.20, anchor=NW)
  
  button_log = CTkButton(dados1, text='LOGIN',text_font=('Fira Code', 15),border_width=0, border_color=lilas2, fg_color=roxo, text_color=branco,bg_color=roxo, width=30, height=30)
  button_log.place(relx=0.07, rely=0.14, anchor=NW)
  
  
  #E-MAIL:
  #Label:
  email_lab=Label(dados1, text = 'E-MAIL', font=('Fira Code',15), bg = roxo, fg = branco)
  email_lab.place(x=36, y=180, anchor=CENTER)
  emem = Label(dados1, text='*', font=('Fira Code', 15), bg = roxo, fg = 'red')
  emem.place(x=84, y=180, anchor=CENTER)
  #Entry:
  email_ent=CTkEntry(dados1, textvariable=email, text_font=('Fira Code', 14), text_color=branco, fg_color=lilas,border_width=0, width=400, height=35)
  email_ent.pack(pady=10, anchor=CENTER)
  
  
  #SENHA:
  #Label:
  senha_lab1=Label(dados1, text = 'SENHA', font=('fira code',15), bg = roxo, fg = branco)
  senha_lab1.place(x=33, y=267, anchor=CENTER)
  sese1 = Label(dados1, text='*', font=('Fira Code', 15), bg = roxo, fg = 'red')
  sese1.place(x=80, y=267, anchor=CENTER)
  #Entry:
  senha_ent1=CTkEntry(dados1, textvariable=senha, text_font=('Fira Code', 14), fg_color=lilas, border_width=0, width=400, height=35)
  senha_ent1.pack(pady=40, anchor=CENTER)
  #Botão para mascarar ou exibir a senha:
  botao_olho = Button(dados1, image=closeeye, bd=0, bg=lilas, activebackground=lilas)
  botao_olho.place(x=360, y=290)
  
  #Botão que realiza o login do usuário:
  button_log1 = CTkButton(dados1, text='ENTRAR',text_font=('Fira Code', 14),border_width=1, border_color=lilas2, fg_color=roxo, text_color=branco,bg_color=roxo, width=30, height=30) #command=lambda:) #O botão "CADASTRAR" recebe dois comando, o de cadastrar o usuário no bd e enviar o usuário para a tela de login.
  button_log1.pack(anchor=CENTER)
  
  botao_olho1 = Button(dados1, image=closeeye, bd=0, bg=lilas, activebackground=lilas, cursor='hand2', command=exibir_senha1)
  botao_olho1.place(x=360, y=290)
  
  
  #LINHA:
  ######################
  ou1=Label(dados1,text='''---------------------- OU ----------------------
           
          
           ''',font= ('Fira Code', 14), fg = lilas, bg=roxo)
  ou1.pack(pady=5, anchor=CENTER)
  ######################
  
  #Não tem uma conta?
  npossui=Label(dados1, text='Não tem uma conta?', font=('fira code',14), bg = roxo, fg = branco)
  npossui.place(x=56, y=425)
  
  #Botão "cadastre-se" em azul que direciona o usuário para a página de cadastro:
  button_npossui=CTkButton(dados1, text='cadastre-se',text_font=('Fira Code', 14),border_width=0, fg_color=roxo, text_color=azul,bg_color=roxo, width=30, height=30, command=logtocad)
  button_npossui.place(x=232, y=425)
  
  #Botão "esqueceu sua senha?" que direciona o usuário para a recuperação de senha:
  button_esqueceu=CTkButton(dados1, text='Esqueceu sua senha?',text_font=('Fira Code', 14),border_width=0, fg_color=roxo, text_color=azul,bg_color=roxo, width=30, height=30)
  button_esqueceu.place(x=90, y=460)
  
  
 
 
 
 
tela_cadastro()

tela.mainloop()