from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apoloniaBeach.common'

    def ready(self):
        import apoloniaBeach.common.signals
