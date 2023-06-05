from django.urls import path

from .views import contact, faq, home

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("faq/", faq, name="faq"),
]
