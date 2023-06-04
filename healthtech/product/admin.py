from django.contrib import admin
from . models import (Product, Image, Inventory, StockControl,
                    Category, Brand, Color,Wishlist, ProductReview, Attribute,Additional_Information)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass

@admin.register(StockControl)
class StockControlAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass




@admin.register(Additional_Information)
class Additional_InformationAdmin(admin.ModelAdmin):
    pass
