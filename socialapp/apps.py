from django.apps import AppConfig

class SocialAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'socialapp'

    def ready(self):
        import socialapp.signals  