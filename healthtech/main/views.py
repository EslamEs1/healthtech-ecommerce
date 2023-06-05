from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Contact, Faq, Settings


def home(request):
    return render(request, "index.html", {})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if request.user.is_authenticated:
            if subject and message:
                user = request.user
                Contact.objects.create(name=user.name, email=user.email, subject=subject, message=message)
                messages.success(request, "Your inquiry has been sent successfully")
        else:
            if name and email and subject and message:
                Contact.objects.create(name=name, email=email, subject=subject, message=message)
                messages.success(request, "Your inquiry has been sent successfully")

        messages.error(request, "Please enter valid data")
        return HttpResponseRedirect(request.headers.get("referer"))

    # Retrieve the settings object
    settings = Settings.objects.first()
    return render(request, "contact.html", {"settings": settings})


def faq(request):
    faq = Faq.objects.all()
    return render(
        request, "faq.html", {
            "faq": faq,
        },
    )
