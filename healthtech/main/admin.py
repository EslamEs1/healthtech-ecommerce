from django.contrib import admin
from .models import Contact, Faq, Settings, Information, About_US, Customer_Service, History, Meet_Our_Doctors, Newsletter, Why_Choose_Us


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


@admin.register(About_US)
class About_USAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer_Service)
class Customer_ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Meet_Our_Doctors)
class Meet_Our_DoctorsAdmin(admin.ModelAdmin):
    pass


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    readonly_fields = ["email"]


@admin.register(Why_Choose_Us)
class Why_Choose_UsAdmin(admin.ModelAdmin):
    pass
