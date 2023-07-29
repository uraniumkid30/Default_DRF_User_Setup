from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.accounts"

    def ready(self):
        try:
            from applications.accounts import signals
        except ImportError as err:
            pass
