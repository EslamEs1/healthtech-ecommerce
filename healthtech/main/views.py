from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import (
    Contact, Faq,
    Settings,
    About_US,
    Why_Choose_Us,
    Meet_Our_Doctors,
    Customer_Service,
    Information,
    History,
                    )
from healthtech.product.models import Product
from healthtech.blog.models import Blog
from healthtech.users.models import User


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
    context = {}
    context["faq"] = Faq.objects.all()
    return render(request, "faq.html", context)


def About(request):
    context = {}
    context["about"] = About_US.objects.first()
    context["why"] = Why_Choose_Us.objects.all()
    context["meet"] = Meet_Our_Doctors.objects.all()
    context["pro_count"] = Product.objects.all().count()
    context["blog_count"] = Blog.objects.all().count()
    context["users_count"] = User.objects.all().count()
    return render(request, "about.html", context)


def customer(request):
    context = {}
    context["customer"] = Customer_Service.objects.all()
    return render(request, "customer-service.html", context)


def information(request, str):
    if str not in ["purchase-guide", "privacy-policy", "terms-of-service"]:
        return redirect("/")
    context = {}
    context["str"] = str
    context["information"] = get_object_or_404(Information, title=str)
    return render(request, "information.html", context)


def history(request):
    context = {}
    context["history"] = History.objects.all()
    return render(request, "history.html", context)
