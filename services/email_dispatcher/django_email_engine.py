from django.conf import settings
from django.core.mail import send_mail

from .base_engine import EmailEngine


class DjangoEmailEngine(EmailEngine):
    @classmethod
    def get_configuration(cls):
        configurations: dict = {}
        return configurations

    @classmethod
    def get_email_sending_parameters(
        cls, to_email: str, from_email: str = "", **kwargs
    ) -> dict:
        email_parameters = {
            "from_email": from_email or cls.FROM_EMAIL,
            "recipient_list": [
                to_email,
            ],
            "message": kwargs.get("message", ""),
            "subject": kwargs.get("subject", ""),
            "html_message": kwargs.get("html_message", ""),
        }
        return email_parameters

    @classmethod
    def __send_mail(cls, to_email: str, from_email: str = "", **kwargs):
        email_parameters = cls.get_email_sending_parameters(
            to_email, from_email, **kwargs
        )
        try:
            send_mail(**email_parameters)
        except Exception as Err:
            print(f"Email Sending Error {Err}")
        else:
            print("Email Sent")
