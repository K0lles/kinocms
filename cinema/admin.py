from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(Cinema)
class CinemaAdmin(TranslationAdmin):
    list_display = [field.name for field in Cinema._meta.get_fields()]


admin.site.register(Hall)
admin.site.register(Gallery)
admin.site.register(Photo)
admin.site.register(SEO)
