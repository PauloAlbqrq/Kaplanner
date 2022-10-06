from datetime import datetime
from pwinput import pwinput
from agendamento import *
from usuario import *
import os
from planner import *
from compromisso import compromisso, evento, meta, tarefa, compromissos
from get_time import *

#Alunos: Barbara Mercez, Paulo Ximenes, Pedro Cruz, Priscila Geovana.
#2º ano Informática Matutino

ler_cad_agd=open('agendados.txt', 'r+', encoding='utf-8')
lido=ler_cad_agd.read()
leido=lido.replace("'", "")
exec(leido)
ler_cad_agd.close()

ler_cad_user=open('cadastrados.txt', 'r+', encoding='utf-8')
exec(ler_cad_user.read())
ler_cad_user.close()

def menu_vis():
  sel2=int(input('quais eventos deseja visualizar?\n1. do dia de hoje\n2. da semana\n3. do mês\n4. tudo\n> '))
  
  if sel2==1: #dia
    planner_sess.exibir_dia()
  elif sel2==2: #semana
    planner_sess.exibir_semana()
  elif sel2==3: #mês
    planner_sess.exibir_mes()
  elif sel2==4: #tudo
    planner_sess.exibir_planner()
  input('\n<Enter>')
  os.system('clear')
  submenu1()

def agendar():
  nome=input('digite o nome do compromisso: ')
  descricao=input('insira uma descrição: ')
  tipo=int(input('que tipo de compromisso deseja registrar?\n1.evento\n2.tarefa\n3.meta\n> '))

  if tipo==1: #evento
    data=input('insira a data (DD-MM-AAAA): ')
    while True:
      try:
        if not len(data.split('-'))==3:
          data=input('formato inválido!\ninsira a data (DD-MM-AAAA): ')
        else:
          break
      except:
        data=input('formato inválido!\ninsira a data (DD-MM-AAAA): ')
        
    hora=input('insira a hora (HH:MM): ')
    while True:
      try:
        if not len(hora.split(':'))==2:
          hora=input('formato inválido!\ninsira a hora (HH:MM): ')
        else:
          break
      except:
        hora=input('formato inválido!\ninsira a hora (HH:MM): ')
        
    agend_atual=evento(nome, descricao, data, hora)
    compromissos.append(agend_atual)
    agendamento_agr=agendamento(get_date(), get_time(), planner_sess.usuario_planner, [agend_atual])
    agendamentos.append(agendamento_agr)
    planner_sess.lista_agendamento=agendamentos
    agend_atual.exibir()
    agendamento_agr.save_agendamento()

  elif tipo==2:#tarefa
    data=input('insira a data (DD-MM-AAAA): ')
    while True:
      try:
        if not len(data.split('-'))==3:
          data=input('formato inválido!\ninsira a data (DD-MM-AAAA): ')
        else:
          break
      except:
        data=input('formato inválido!\ninsira a data (DD-MM-AAAA): ')
        
    hora=input('insira a hora (HH:MM): ')
    while True:
      try:
        if not len(hora.split(':'))==2:
          hora=input('formato inválido!\ninsira a hora (HH:MM): ')
        else:
          break
      except:
        hora=input('formato inválido!\ninsira a hora (HH:MM): ')
    repeticao=int(input('insira uma repetição:\n1.diariamente\n2.semanalmente\n3.mensalmente\n4.anualmente'))
    agend_atual=tarefa(nome, descricao, data, hora, repeticao)
    compromissos.append(agend_atual)
    agendamento_agr=agendamento(get_date(), get_time(), planner_sess.usuario_planner, [agend_atual])
    agendamentos.append(agendamento_agr)
    planner_sess.lista_agendamento=agendamentos
    agend_atual.exibir()
    agendamento_agr.save_agendamento()
    
  elif tipo==3:#meta
    prazo=input('insira um prazo para a meta (DD-MM-AAAA): ')
    while True:
      try:
        if not len(prazo.split('-'))==3:
          prazo=input('formato inválido!\ninsira um prazo para a meta (DD-MM-AAAA): ')
        else:
          break
      except:
        prazo=input('formato inválido!\ninsira um prazo para a meta (DD-MM-AAAA): ')
        
    agend_atual=meta(nome, descricao, prazo, 'NC')
    compromissos.append(agend_atual)
    agendamento_agr=agendamento(get_date(), get_time(), planner_sess.usuario_planner, [agend_atual])
    agendamentos.append(agendamento_agr)
    planner_sess.lista_agendamento=agendamentos
    agend_atual.exibir()
    agendamento_agr.save_agendamento()
    
  submenu1()
    
#Função global, cadastro
def cadastro():
    #Define os dados do usuário
    nome_cad = str(input('Digite seu nome: '))
    sur_cad = str(input('Digite seu sobrenome: '))
    mail_cad = input('Digite seu e-mail: ')
    pass_cad = pwinput(prompt='Digite sua senha: ', mask='•')
    #Adiciona os dados do usuário na lista c
    users[mail_cad] = user(nome_cad, sur_cad, mail_cad, pass_cad)
    users[mail_cad].save_user()
    #users[mail_cad].set_ID()
    users[mail_cad].exibir()
    print(users)
  
def submenu1():
  sel = int(
        input(
            'O que você deseja fazer?\n1. agendar evento\n2. excluir usuário\n3. trocar senha\n4. visualizar eventos\n5. sair\n> '
        ))
    #Seleção 1 (agendar evento)
  if sel == 1:
    agendar()
  elif sel == 2:
      #Executa apagar dados do usuário
    users[cred_mail].remove_db()
    print('excluído')
    submenu1()
    
  #Seleção 3 (trocar senha)
  elif sel == 3:
    #Executa a troca de senha (Get and Set)
    users[cred_mail].set_senha(
      pwinput(prompt='Insira nova senha: ', mask='•'))
    users[cred_mail].save_user()
    print('senha trocada!')
    menu()
  elif sel == 4:
    menu_vis()
  #seleção de debug
  elif sel == 900:
    while True:
      comando = input('Insira comando: ')
      if comando != 'sair':
        try:
          exec(comando)
        except:
          print('Comando inválido!')
      else:
        os.system('clear')
        submenu1()
        break
        
def menu():
  sel1=int(input('O que deseja fazer?\n1. Cadastrar-me\n2. Logar-me\n> '))

  if sel1==1:#cadastro
    cadastro()
    os.system('clear')
    menu()
  elif sel1==2:#login
    global cred_mail
    global cred_senha
    cred_mail, cred_senha=user.logar()
    try:
      users[cred_mail]=users[cred_mail]
      if users[cred_mail].get_senha() == cred_senha:
        os.system('clear')
        global planner_sess
        planner_sess=planner(usuario_planner=users[cred_mail], lista_agendamento=agendamentos)
        submenu1()
      else:
        os.system('clear')
        print('\ncredenciais inválidas\n')
        menu()
    except KeyError:
      os.system('clear')
      print('\nEmail inválido\n')
      menu()
  #seleção de debug
  elif sel1 == 900:
    while True:
      comando = input('Insira comando: ')
      if comando != 'sair':
        try:
          exec(comando)
        except:
          print('Comando inválido!')
      else:
        os.system('clear')
        menu()
        break
  else:
    print('valor inválido!')
    menu()
        
#Execução do menu
menu()
