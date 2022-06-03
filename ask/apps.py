from django.apps import AppConfig


class AskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ask'

    def ready(self):
        import ask.signal