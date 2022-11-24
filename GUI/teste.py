from conexao import *

email_l='aaa@gmail.com'
conexao_log = conectar_db()
print(buscar_dados(conexao_log, f"""select senha from usuario where email='{email_l}'""")[0][0])