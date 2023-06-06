from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .fields import HexColorField
from healthtech.utils.storages import slugify_instance_name

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="img/store/category")
    slug = models.SlugField(max_length=50, blank=True, editable=False)
    is_active = models.BooleanField()

    class Meta:
        ordering = ["-name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("product:product_list", args=[self.slug])


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    img = models.ImageField(upload_to="img/store/brand")
    slug = models.SlugField(max_length=50, blank=True, editable=False)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("product:product_list_brand", args=[self.category.slug, self.slug])


class IsActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    slug = models.SlugField(max_length=80)
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    num_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    objects = IsActiveManager()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:detail", args=[self.slug])

    def star(self):
        ratings = self.reviews.all()
        if ratings:
            return round(sum(r.rating for r in ratings) / len(ratings), 1)
        else:
            return "0.0"

    def count_rating(self):
        return self.reviews.all().count()


@receiver(pre_save, sender=Product)
def check_slug(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_name(instance, save=False)


@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_name(instance, save=True)


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Inventory(models.Model):
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,)
    sku = models.CharField(max_length=20, unique=True, )
    # sku = models.UUIDField(default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name="inventory", on_delete=models.CASCADE)
    attribute_values = models.ManyToManyField(Attribute)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = "Inventory"

    def __str__(self):
        return self.product.name


class Color(models.Model):
    inventory = models.ForeignKey(Inventory, related_name="color", on_delete=models.CASCADE)
    color = HexColorField()

    class Meta:
        ordering = ["-color"]

    def __str__(self):
        return self.inventory.product.name


class StockControl(models.Model):
    last_checked = models.DateTimeField(auto_now_add=True, editable=False)
    units = models.IntegerField(default=0)
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, related_name="stock")

    class Meta:
        verbose_name_plural = "Stock Control"


class Image(models.Model):
    url = models.ImageField(upload_to=None)
    alternative_text = models.CharField(max_length=50)
    is_feature = models.BooleanField(default=False)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)


class Additional_Information(models.Model):
    product = models.ForeignKey(Product, related_name="product_info", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='wishlists')


class ProductReview(models.Model):
    user = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ["-created_at"]
