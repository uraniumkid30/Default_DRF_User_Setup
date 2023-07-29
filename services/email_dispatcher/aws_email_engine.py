from django.conf import settings
from django.core.mail import send_mail

from .base_engine import EmailEngine


class AWSSESEmailEngine(EmailEngine):
    @classmethod
    def get_configuration(cls):
        configurations: dict = {
            "AWS_SES_ACCESS_KEY_ID": (
                getattr(settings, "AWS_SES_ACCESS_KEY_ID", None)
                or getattr(settings, "AWS_ACCESS_KEY_ID", None)
            ),
            "AWS_SES_SECRET_ACCESS_KEY": (
                getattr(settings, "AWS_SES_SECRET_ACCESS_KEY", None)
                or getattr(settings, "AWS_SECRET_ACCESS_KEY", None)
            ),
            "AWS_SES_REGION": (
                getattr(settings, "AWS_SES_REGION", None)
                or getattr(settings, "AWS_DEFAULT_REGION", "us-east-1")
            ),
            #             "AWS_SES_CONFIGURATION_SET_NAME": getattr(settings, "AWS_SES_CONFIGURATION_SET_NAME", None),
            #             "AWS_SES_TAGS": getattr(settings, "AWS_SES_TAGS", None),
        }

        return configurations

    @classmethod
    def get_email_sending_parameters(
        cls, to_email: str, from_email: str = "", **kwargs
    ):
        email_parameters = {
            "Source": from_email or cls.FROM_EMAIL,
            "Destination": {
                "ToAddresses": to_email
                if isinstance(to_email, list)
                else [
                    to_email,
                ],
                "CcAddresses": kwargs.get("ccs", ""),
                "BccAddresses": kwargs.get("bccs", ""),
            },
            "Message": {
                "Body": {
                    "Html": {
                        "Charset": "UTF-8",
                        "Data": kwargs.get("HtmlBody", ""),
                    }
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": kwargs.get("Subject", ""),
                },
            },
        }
        return email_parameters

    @staticmethod
    def get_aws_ses_client(cls):
        import boto3
        try:
            config = cls.get_configuration()
            access_key_id = config["AWS_SES_ACCESS_KEY_ID"]
            secret_access_key = config["AWS_SES_SECRET_ACCESS_KEY"]
            region_name = config["AWS_SES_REGION"]
            client = boto3.client(
                "ses",
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name,
            )
        except Exception as e:
            client = None
            print(f"{e} prevented aws ses client instantiation")
        finally:
            return client

    @classmethod
    def __send_mail(cls, to_email: str, from_email: str = "", **kwargs):
        email_parameters = cls.get_email_sending_parameters(
            to_email, from_email, **kwargs
        )
        try:
            aws_client = cls.get_aws_ses_client()
            aws_client.send_email(**email_parameters)
        except Exception as Err:
            print(f"Email Sending Error {Err}")
        else:
            print("Email Sent")