from pwinput import pwinput

#Dicionário paraa armazenar os usuários
users={}

#Classe do usuário
class user:
#Construtor
 def __init__(self, nome, sobrenome, email, senha):
  self.nome = nome
  self._sobrenome = sobrenome
  self._email = email
  self.__senha = senha
  self._ID = 0

#Função de exibir
 def exibir(self):
  print(f'nome: {self.nome}\nsobrenome: {self._sobrenome}\nemail: {self._email}\nID de usuário: {self._ID}')

#função de remoção de usuário pelo e-mail
 def remove_db(self):        
  users.pop(self._email)
  cad_data=open('cadastrados.py', 'a+', encoding='utf-8')
  cad_data.write(f'users.pop("{self._email}")\n')
  cad_data.close()
      
#Sets e gets dos dados
#Redefine a senha do usuário
 def set_senha(self, senhaNova):
  self.__senha = senhaNova

 def get_senha(self):
  return self.__senha

#Redefine o sobrenome do usuário
 def set_sobrenome(self, newSur):
  self._sobrenome = newSur

 def get_sobrenome(self):
  return self._sobrenome

#Redefine o e-mail do usuário
 def set_email(self, emailNovo):
  self._email = emailNovo

 def get_email(self):
  return self._email
      
#Função de login
 def logar():
  log_email = input('E-mail: ')
  log_senha = pwinput(prompt='Senha: ', mask='•')
  return log_email, log_senha
    
 def save_user(self):
  cad_data=open('cadastrados.txt', 'a+', encoding='utf-8')
  cad_data.write(f'users["{self._email}"]=user("{self.nome}", "{self._sobrenome}", "{self._email}", "{self.__senha}")\n')
  cad_data.close()