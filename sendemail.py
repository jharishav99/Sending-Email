import smtplib
import getpass
from email.mime.text import MIMEText


def send_email():
    sender_address = 'jharishav99@gmail.com'
password = getpass.getpass()

subject = 'Sending Mails using Python'
msg =  '''Hi
This E-mail is generated From Python 
Thanks you!
Rishav 
'''

# server initializationO
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('jharishav99@gmail.com',password)


# draft my message body

msg = MIMEText (msg)
msg['Subject'] = subject
msg['From'] = 'jharishav99@gmail.com'
msg['To'] = 'jharishav99@gmail.com'
recipients = ['tinchugaming99@gmail.com']

server.sendmail('jharishav99@gmail.com',recipients,msg.as_string())

send_email()



