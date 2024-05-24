import os
import smtplib
from email.message import EmailMessage

# configuração do gmail
# https://myaccount.google.com/apppasswords

# email com as senhas administradas
email = "teste@gmail.com "

# extrair a senha administrada do txt
with open('senha.txt') as f:
    senha = f.readlines()
    f.close()
senha_do_email = senha[0]
senha_do_email

# configurações do email
msg = EmailMessage()
msg['Subject'] = 'Enviando e-mail com python'
msg['From'] = 'teste@gmail.com'
msg['To'] = 'destino@gmail.com'
msg.set_content("Segue o relatório diário")

# anexos
with open('relatorio_diario.pdf', 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='application', subtype='pdf', filename='relatorio_diario.pdf')

with open('dolar.png', 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='application', subtype='png', filename='dolar.png')

# login no servidor do gmail e envio da mensagem
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, senha_do_email)
    smtp.send_message(msg)