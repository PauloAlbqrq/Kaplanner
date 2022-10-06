#from agendamento import *
import notifypy
compromissos=[]
class compromisso:
  def __init__(self, nome, descricao):
    self.nome=nome
    self.descricao=descricao

    
  def notificar(self,nome,descricao):
    try:
      noti=notifypy.Notify()
      noti.title = self.nome
      noti.message = self.descricao
      noti.icon = 'assets/kaplanner_logo.png'
      noti.send()
    except:
      pass
    

class evento(compromisso):
  
  def __init__(self, nome, descricao, data, hora):
    self.data=data
    self.hora=hora
    super().__init__(nome, descricao)
    
  def exibir(self):
    print(f'nome: {self.nome}\ndescrição: {self.descricao}\ndata: {self.data}\nhora: {self.hora}')

class tarefa(compromisso):
  def __init__(self, nome, descricao, data, hora, repeticao):
    self.data=data
    self.hora=hora
    self.repeticao=repeticao
    super().__init__(nome, descricao)
    
  def exibir(self):
    print(f'nome: {self.nome}\ndescrição: {self.descricao}\ndata: {self.data}\nhora: {self.hora}')

class meta(compromisso):
  def __init__(self, nome, descricao, prazo, estado):
    self.prazo=prazo
    self.estado=estado
    super().__init__(nome, descricao)
    
  def exibir(self):
    print(f'nome: {self.nome}\ndescrição: {self.descricao}\nprazo: {self.prazo}\nestado: {self.estado}')

'''def insert_compromisso(self):

  def consult_compromisso(self):
    
  def edit_compromisso(self):
    
  def remove_compromisso(self):'''