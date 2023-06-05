from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

from healthtech.utils.storages import slugify_instance_name

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, blank=True, editable=False)

    class Meta:
        ordering = ["-name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def filter(self):
        return reverse("blog:filter", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:filter", args=[self.slug])


# Start Blog
class Blog(models.Model):
    category = models.ForeignKey(Category, related_name="blog", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, blank=True, unique=True, editable=False)
    tags = TaggableManager()
    views_count = models.IntegerField(editable=False, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:blog_detail", args=[self.slug])

    def count_comment(self):
        return self.comment.all().count()


@receiver(pre_save, sender=Blog)
def check_slug(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_name(instance, save=False)


@receiver(post_save, sender=Blog)
def course_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_name(instance, save=True)


class Image(models.Model):
    blog = models.ForeignKey(Blog, related_name="image", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="img/blog")
    is_feature = models.BooleanField(default=False)

    class Meta:
        ordering = ["-img"]

    def __str__(self):
        return self.blog.name + "image"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comment", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.author + self.blog


class InstagramImage(models.Model):
    img = models.ImageField(upload_to="img/instagram")

    class Meta:
        ordering = ["-img"]
