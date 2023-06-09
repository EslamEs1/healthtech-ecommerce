# Generated by Django 4.1.9 on 2023-06-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("subject", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Faq",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("question", models.CharField(max_length=200)),
                ("answer", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Settings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("icon", models.ImageField(upload_to="img/main/icon/")),
                ("main_logo", models.ImageField(upload_to="img/main/logo/")),
                ("second_logo", models.ImageField(upload_to="img/main/logo/")),
                ("about", models.TextField()),
                ("facebook", models.URLField()),
                ("twitter", models.URLField()),
                ("instagram", models.URLField()),
                ("whatsapp", models.IntegerField()),
                ("developer", models.URLField()),
                ("developer_logo", models.ImageField(upload_to="img/main/icon/")),
                ("address", models.CharField(max_length=255)),
                ("phone", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("working_hours", models.CharField(max_length=250)),
            ],
        ),
    ]
