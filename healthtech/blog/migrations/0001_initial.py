# Generated by Django 4.1.9 on 2023-06-05 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(max_length=15000)),
                ("slug", models.SlugField(blank=True, editable=False, max_length=100, unique=True)),
                ("views_count", models.IntegerField(default=0, editable=False)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "verbose_name_plural": "Posts",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, unique=True)),
                ("slug", models.SlugField(blank=True, editable=False)),
            ],
            options={
                "verbose_name_plural": "Categories",
                "ordering": ["-name"],
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("img", models.ImageField(upload_to="img/blog")),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="image", to="blog.blog"
                    ),
                ),
            ],
            options={
                "ordering": ["-img"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="comment", to="blog.blog"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.AddField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="blog", to="blog.category"
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
