import win32com.client as win32

# cria integração com outlook
outlook = win32.Dispatch('outlook.application')

# cria um email
email = outlook.CreatItem(0)

# configura informações do email
email.To = "destino1@gmail.com; destino2@gmail.com"
email.Subject = "assunto"
email.HTMLBody = """
<p>Corpo do E-mail</p>

<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit,</p>
<p>sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
<p>Ut enim ad minim veniam,</p>
<p>quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
<p>Excepteur sint occaecat cupidatat non proident,</p>
<p>sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
"""

# anexos para o email
anexo = "D:/arquivo.xlsx"
email.Attachments.Add(anexo)

email.Send()
print("E-mail enviado")