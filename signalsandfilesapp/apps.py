from django.apps import AppConfig


class SignalsandfilesappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signalsandfilesapp'

    def ready(self):
        import signalsandfilesapp.signals
