from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from healthtech.payment.webhooks import stripe_webhook


urlpatterns = [
    path("", include("healthtech.main.urls", namespace="main")),
    path("products/", include("healthtech.product.urls", namespace="product")),
    path("blogs/", include("healthtech.blog.urls", namespace="blog")),
    path("payment/", include("healthtech.payment.urls", namespace="payment")),
    path("orders/", include("healthtech.order.urls", namespace="orders")),
    path("cart/", include("healthtech.cart.urls", namespace="cart")),
    path("coupon/", include("healthtech.coupons.urls", namespace="coupons")),

    path('payment/webhook/', stripe_webhook, name='stripe-webhook'),


    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("healthtech.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
