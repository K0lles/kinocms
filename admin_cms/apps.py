from django.apps import AppConfig


class AdminCmsConfig(AppConfig):
    login_required = True
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_cms'
