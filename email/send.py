import os
import smtplib
import email.message
import random


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
tam_cod = 8
cod = "".join(random.sample(chars,tam_cod))
print(cod)

def enviar_email():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    tam_cod = 8
    cod = "".join(random.sample(chars,tam_cod))
    corpo_email = (f'''
                   {cod}''')
    
    msg = email.message.Message()
    msg['Subject'] = '[KaPlanner] - Seu código para atualização de senha'
    msg['From'] = 'kaplanner.recovery@gmail.com'
    msg['To'] = 'styletommoo@gmail.com'
    password = 'cmkhywjlemzuykue'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Loging credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
enviar_email()