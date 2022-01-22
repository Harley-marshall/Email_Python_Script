import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import _tkinter

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '{Send_To_Name}'
email['to'] = '{Send_To_Email}'
email['subject'] = 'Money'

email.set_content(html.substitute({'name': 'Harley', }), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('{Send_From_Email}', '{Send_From_Password}')
    smtp.send_message(email)
    print("email sent!")
