# Generated by Django 4.1.9 on 2023-06-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_information_created_at_information_updated_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="information",
            name="title",
            field=models.CharField(default="pp", max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
