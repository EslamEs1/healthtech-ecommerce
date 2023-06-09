from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from healthtech.product.models import Product
from healthtech.coupons.forms import CouponApplyForm
from healthtech.cart.cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


def cart_add_links(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, override_quantity=False)
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_detail(request):
    context = {}
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
    coupon_apply_form = CouponApplyForm()

    context["cart"] = cart
    context["coupon_apply_form"] = coupon_apply_form
    return render(request, 'cart/detail.html', context)
