from django.db.models import Sum

# from beitak.blog.models import Blog
# from beitak.blog.models import Category as Category_Blog
from healthtech.product.models import Brand, Category, Product, Wishlist, Inventory

# from .models import Settings


def context_processors(request):
    wishlist = None
    product = None
    total_price = 0

    if request.user.is_authenticated:
        try:
            wishlist = Wishlist.objects.get(user=request.user)
            product = wishlist.products.all()
            inventory = Inventory.objects.filter(product_id__in=product)
            total_price = inventory.aggregate(total=Sum("price"))["total"]
        except Wishlist.DoesNotExist:
            pass

    # settings = Settings.objects.first()
    featured = Product.objects.filter(is_featured=True)
    home_brand = Brand.objects.all()


    return {
        "wishlist": product,
        "total": total_price,
        # "settings": settings,
        "home_featured": featured,
        "home_brand": home_brand,
    }
