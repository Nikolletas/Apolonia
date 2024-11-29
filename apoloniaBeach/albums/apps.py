from django.apps import AppConfig


class AlbumsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apoloniaBeach.albums'

    def ready(self):
        import apoloniaBeach.albums.signals
