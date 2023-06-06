from django.contrib import admin

from .models import Contact, Faq, Settings, Information


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    pass


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    pass
