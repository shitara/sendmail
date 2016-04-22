
import smtplib
from email.mime.text import MIMEText

class Gmail(object):
    def __init__(self, **kwargs):
        self.username = kwargs['username']
        self.password = kwargs['password']

    def send(self, to, subject, body):
        server = smtplib.SMTP('smtp.gmail.com:587')

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to

        server.starttls()
        server.ehlo()
        server.login(self.username, self.password)
        server.send_message(msg)
        server.quit()

