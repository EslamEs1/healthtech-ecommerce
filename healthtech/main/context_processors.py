from django.db.models import Sum
from healthtech.cart.cart import Cart
from healthtech.product.models import Wishlist, Inventory, Category

from .models import Settings


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

    settings = Settings.objects.first()
    category = Category.objects.all()
    cart = Cart(request)
    return {
        "wishlist": product,
        "total": total_price,
        "settings": settings,
        "category": category,
        "item_cart": cart,
    }
