# Generated by Django 4.1.9 on 2023-06-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_image_is_feature"),
    ]

    operations = [
        migrations.CreateModel(
            name="InstagramImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("img", models.ImageField(upload_to="img/instagram")),
            ],
            options={
                "ordering": ["-img"],
            },
        ),
    ]