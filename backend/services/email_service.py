```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService:
    def __init__(self, server, port, username, password):
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.connection = self._connect_to_smtp_server()

    def _connect_to_smtp_server(self):
        connection = smtplib.SMTP(self.server, self.port)
        connection.starttls()
        connection.login(self.username, self.password)
        return connection

    def send_email(self, recipient_email, subject, body, content_type='html'):
        message = MIMEMultipart()
        message['From'] = self.username
        message['To'] = recipient_email
        message['Subject'] = subject

        if content_type == 'html':
            message.attach(MIMEText(body, 'html'))
        else:
            message.attach(MIMEText(body, 'plain'))

        try:
            self.connection.send_message(message)
            return True
        except Exception as e:
            print(f"An error occurred while sending email: {e}")
            return False

    def __del__(self):
        self.connection.quit()

# Example usage:
# email_service = EmailService('smtp.example.com', 587, 'your_email@example.com', 'your_password')
# email_service.send_email('recipient@example.com', 'Survey Invitation', '<h1>You are invited to participate in a survey!</h1>')
```