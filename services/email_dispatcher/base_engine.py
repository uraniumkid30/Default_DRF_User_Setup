from abc import ABCMeta, abstractmethod
from typing import List

from django.conf import settings
from django.template.loader import render_to_string


class EmailEngine(metaclass=ABCMeta):
    ERRORS = []
    FROM_EMAIL = getattr(settings, "EMAIL_HOST_USER", None)

    @classmethod
    @abstractmethod
    def get_configurations(cls):
        pass

    @classmethod
    @abstractmethod
    def get_email_sending_parameters(
        cls, to_email: str, from_email: str = "", **kwargs
    ):
        pass

    @classmethod
    @abstractmethod
    def __send_mail(cls, to_email: str, from_email: str = "", **kwargs):
        pass

    @classmethod
    def send_mail(cls, to_email: str, from_email: str = "", **kwargs):
        can_send_emails = cls.get_email_status()
        if can_send_emails:
            cls.__send_mail(to_email, from_email, **kwargs)
        else:
            print(f"Fix the following ERRORS : {cls.ERRORS} ")

    @staticmethod
    def get_html_message(template_path: str, template_parameters: dict = {}) -> str:
        msg_html = render_to_string(template_path, template_parameters)
        return msg_html

    @classmethod
    def __is_sufficient(cls, resource: dict = {}, marker: str = "") -> bool:
        if all(resource.values()):
            return True
        else:
            for _key in resource:
                cls.ERRORS.append(f"{_key} is missing in {marker}")
            else:
                return False

    @classmethod
    def is_configuration_sufficient(cls) -> bool:
        configurations = cls.get_configuration()
        return cls.__is_sufficient(resource=configurations, marker="Settings")

    @classmethod
    def is_email_sending_parameters_sufficient(cls) -> bool:
        email_sending_parameters = cls.get_email_sending_parameters()
        return cls.__is_sufficient(
            resource=email_sending_parameters, marker="Email sending parameters"
        )

    @classmethod
    def get_email_status(cls):
        cls.is_configuration_sufficient()
        cls.is_email_sending_parameters_sufficient()
        if len(cls.ERRORS):
            return False
        return True
