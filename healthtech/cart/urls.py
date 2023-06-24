from django.urls import path
from healthtech.cart.views import cart_detail, cart_add, cart_remove, cart_add_links

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('add-links/<int:product_id>/', cart_add_links, name='cart_add_links'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
]
