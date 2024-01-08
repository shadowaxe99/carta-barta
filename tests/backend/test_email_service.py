import unittest
from unittest.mock import patch
from backend.services.email_service import EmailService

class TestEmailService(unittest.TestCase):
    def setUp(self):
        self.email_service = EmailService()

    @patch('backend.services.email_service.smtplib')
    def test_send_email_invitation(self, mock_smtplib):
        # Setup mock SMTP server
        mock_server = mock_smtplib.SMTP.return_value.__enter__.return_value
        mock_server.sendmail.return_value = {}

        # Define email content
        sender = 'no-reply@olvy.co'
        recipient = 'test@example.com'
        subject = 'Survey Invitation'
        body = 'You are invited to participate in the survey.'
        message = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{body}"

        # Send email
        self.email_service.send_email_invitation(sender, recipient, subject, body)

        # Assert email was sent
        mock_server.sendmail.assert_called_once_with(sender, [recipient], message)

    @patch('backend.services.email_service.smtplib')
    def test_send_email_invitation_with_exception(self, mock_smtplib):
        # Setup mock SMTP server to raise an exception
        mock_server = mock_smtplib.SMTP.return_value.__enter__.return_value
        mock_server.sendmail.side_effect = Exception('SMTP exception')

        # Define email content
        sender = 'no-reply@olvy.co'
        recipient = 'test@example.com'
        subject = 'Survey Invitation'
        body = 'You are invited to participate in the survey.'

        # Attempt to send email and expect an exception
        with self.assertRaises(Exception) as context:
            self.email_service.send_email_invitation(sender, recipient, subject, body)

        # Assert that the exception message is correct
        self.assertTrue('SMTP exception' in str(context.exception))

if __name__ == '__main__':
    unittest.main()