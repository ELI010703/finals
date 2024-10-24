from django.apps import AppConfig


class FrontendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frontend'

class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        import frontend.signals