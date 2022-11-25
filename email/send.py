import os
import smtplib
import email.message
import random


def enviar_email():
    codigo = []
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    tam_cod = 8
    cod = "".join(random.sample(chars,tam_cod))
    codigo.append(cod)
    
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



##########################################################################################################3
'''def recup_senha():
  topl=Toplevel()
  topl.geometry('500x300')
  
  tel_email_rec = Frame(topl, bg=roxo)
  tel_email_rec.pack(fill=BOTH, expand=1)
  
  tel_cod_rec = Frame(topl, bg=roxo)
  #tel_cod_rec.pack(fill=BOTH, expand=1)
  
  
  email_rec = StringVar()
  email_rec_info = email_rec.get()
  
  cod_recp = StringVar()
  cod_recp_info = cod_recp.get()
  
  def enviar_cod():
    tela_email_rec.destroy()
    if '@' in email_rec_info:
      def enviar_email():
        codigo = []
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        tam_cod = 8
        cod = "".join(random.sample(chars,tam_cod))
        codigo.append(cod)
        
        corpo_email = (f'''
                      {cod}''')
        
        msg = email.message.Message()
        msg['Subject'] = '[KaPlanner] - Seu código para atualização de senha'
        msg['From'] = 'kaplanner.recovery@gmail.com'
        msg['To'] = email_rec_info
        password = 'cmkhywjlemzuykue'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)
        
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        
        # Loging credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))  
      enviar_email()
      tela_cod_rec.pack(fill=BOTH, expand=1)
    
    else:
      messagebox.showinfo('erro', 'Email inválido')
      raise erros.Email_Invalido('Email inserido não possui @')
  
  Label(tel_email_rec, text='Insira um email ao qual você tem acesso *', font=('Fira Code', 15), bg = roxo, fg = branco).pack(pady=35)
  email_recupera = CTkEntry(tel_email_rec, textvariable=email_rec, text_font=('Fira Code', 14), text_color=branco, fg_color=lilas,border_width=0, width=400, height=35)
  email_recupera.pack()
  mudar = CTkButton (tel_email_rec, text='Enviar',text_font=('Fira Code', 14),border_width=1, border_color=lilas2, fg_color=roxo, text_color=branco,bg_color=roxo, width=30, height=30, command=enviar_cod)
  mudar.place()
  
  Label(tel_cod_rec, text='Insira o código enviado para o seu e-mail *', font=('Fira Code', 15), bg = roxo, fg = branco).pack() 
  cod_recp = CTkEntry(tel_cod_rec, textvariable=cod_recp, text_font=('Fira Code', 14), text_color=branco, fg_color=lilas,border_width=0, width=400, height=35)
  cod_recp.pack()
  verify_cod = CTkButton (tela_cod_rec, text='Enviar',text_font=('Fira Code', 14),border_width=1, border_color=lilas2, fg_color=roxo, text_color=branco,bg_color=roxo, width=30, height=30)
  Verify_cod.pack(anchor=CENTER)
  '''
