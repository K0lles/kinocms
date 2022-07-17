from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    model = Page
    change_list_template = 'admin/page/page.html'


admin.site.register(Page, PageAdmin)
