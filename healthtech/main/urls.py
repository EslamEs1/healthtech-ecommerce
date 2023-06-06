from django.urls import path

from .views import contact, faq, home, About, customer, information, history

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("faq/", faq, name="faq"),
    path("about/", About, name="about"),
    path("customer/", customer, name="customer"),
    path("information/<str:str>/", information, name="information"),
    path("history/", history, name="history"),
]
