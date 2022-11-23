from datetime import *
from get_time import *

class planner:
 #Construtor
 def __init__(self, usuario_planner, lista_agendamento:list=None):
  self.usuario_planner=usuario_planner
  self.lista_agendamento=lista_agendamento
   
 #Função para exibição do planner   
 def exibir_planner(self): 
  for item in self.lista_agendamento:
   for compromisso in item.compromissos:
    print('')
    compromisso.exibir()
    print('')

#Função para exibição de compromissos do dia
 def exibir_dia(self):
   for item in self.lista_agendamento:
    for compromisso in item.compromissos:
     try:
      data_comp=compromisso.data
     except:
      data_comp=compromisso.prazo
     finally:
      if data_comp==get_date():
       print('')
       compromisso.exibir()
       print('')
        
  #Função para exibição de compromissos da semana
 def exibir_semana(self):
   data_split=get_date().split('-')
   for item in self.lista_agendamento:
    for compromisso in item.compromissos:
     try:
      data_comp_split=compromisso.data.split('-')
     except:
      data_comp_split=compromisso.prazo.split('-')
     finally:
      if date(int(data_split[2]), int(data_split[1]), int(data_split[0])).isocalendar()[1]==date(int(data_comp_split[2]), int(data_comp_split[1]), int(data_comp_split[0])).isocalendar()[1]:
       print('')
       compromisso.exibir()
       print('')
        
  #Função para exibição de compromissos do mês
 def exibir_mes(self):
  data_split=get_date().split('-')
  for item in self.lista_agendamento:
   for compromisso in item.compromissos:
    try:
     data_comp_split=compromisso.data.split('-')
    except:
     data_comp_split=compromisso.prazo.split('-')
    finally:
     if data_comp_split[1]==data_split[1] and data_comp_split[2]==data_split[2]:
      print('')
      compromisso.exibir()
      print('')