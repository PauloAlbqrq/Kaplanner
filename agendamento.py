from compromisso import *

agendamentos = []
class agendamento:
 def __init__(self, data, hora, usuario, compromissos):
   self.data_agendamento=data
   self.hora_agendamento=hora
   self.agendador=usuario
   self.compromissos=compromissos
    
 def insert_agendamento(self):
   agendamentos.append(self)
   
 def consult_agendamento(self):
   return {'data':self.data_agendamento, 'hora':self.hora_agendamento, 'agendador':self.agendador}

#Função para salvar agendamento
 def save_agendamento(self):
  comp=[]
  for item in self.compromissos:
   if isinstance(item, evento):
    comp.append(f'evento("{item.nome}", "{item.descricao}", "{item.data}", "{item.hora}")')
     
   elif isinstance(item, tarefa):
     comp.append(f'tarefa("{item.nome}", "{item.descricao}", "{item.data}", "{item.hora}", "{item.repeticao}")')
     
   elif isinstance(item, meta):
     comp.append(f'meta("{item.nome}", "{item.descricao}", "{item.prazo}", "{item.estado}")')            
     cad_data=open('agendados.txt', 'a+', encoding='utf-8')
     cad_data.write(f'agendamentos.append(agendamento("{self.data_agendamento}", "{self.hora_agendamento}", user("{self.agendador.nome}", "{self.agendador._sobrenome}", "{self.agendador._email}", "{self.agendador.get_senha()}"), {comp}))\n')
     cad_data.close()
     
  def remove_agendamento(self):
    agendamentos.remove(self)

    