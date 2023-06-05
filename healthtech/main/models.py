from django.db import models


class Settings(models.Model):
    icon = models.ImageField(upload_to="img/main/icon/")
    main_logo = models.ImageField(upload_to="img/main/logo/")
    second_logo = models.ImageField(upload_to="img/main/logo/")
    about = models.TextField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    whatsapp = models.IntegerField()
    developer = models.URLField()
    developer_logo = models.ImageField(upload_to="img/main/icon/")
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    working_hours = models.CharField(max_length=250)

    def __str__(self):
        return "Settings"


class Contact(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.email}"


class Subscribe:
    email = models.EmailField()

    def __str__(self):
        return self.email


class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question


class About_US(models.Model):
    img = models.ImageField(upload_to="img/about/")
    title = models.CharField(max_length=150)
    text = models.TextField()


class Why_Choose_Us(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=250)


class Meet_Our_Doctors(models.Model):
    img = models.ImageField(upload_to="img/about/Doctors")
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()

