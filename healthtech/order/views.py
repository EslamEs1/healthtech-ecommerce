from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from healthtech.cart.cart import Cart
from django.urls import reverse
from .tasks import order_created
from django.contrib import messages


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = OrderCreateForm()
    return render(request, 'orders/checkout.html', {'cart': cart, 'form': form})
