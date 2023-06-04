# Generated by Django 4.1.9 on 2023-06-03 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_alter_image_inventory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="inventory",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="product.inventory"),
        ),
        migrations.AlterField(
            model_name="stockcontrol",
            name="inventory",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, related_name="stock", to="product.inventory"
            ),
        ),
    ]
