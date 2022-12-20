from django.apps import AppConfig


class ActivityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'activity'

class newsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
