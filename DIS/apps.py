from django.apps import AppConfig


class DisConfig(AppConfig):
    name = 'DIS'

    def ready(self):
        import DIS.signals
