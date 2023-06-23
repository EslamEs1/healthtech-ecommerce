from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F, Prefetch, Sum, Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from healthtech.cart.forms import CartAddProductForm

from .models import Brand, Category, Product, Color, ProductReview, Wishlist, Inventory
from healthtech.order.models import OrderItem


class ProductListView(ListView):
    model = Product
    paginate_by = 12
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        brand = self.request.GET.get("brand")
        price = self.request.GET.get("price", "")
        color = self.request.GET.get("color", "")

        filters = Q()
        if category:
            filters &= Q(category__name__icontains=category)
        if brand:
            filters &= Q(brand__name__icontains=brand)
        if color:
            filters &= Q(product__color__color=color)

        queryset = queryset.filter(filters)

        if price:
            try:
                min_price, max_price = map(int, price.split(";"))
                queryset = queryset.filter(product__price__range=(min_price, max_price))
            except ValueError:
                pass

        return queryset.select_related("brand").prefetch_related(
            Prefetch(
                "inventory",
                queryset=Inventory.objects.select_related("product").prefetch_related("color", "image_set"),
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context["category"] = Category.objects.only("name")
        context["brands"] = Brand.objects.only("name")
        context["colors"] = Color.objects.values("color").distinct()
        context["count"] = queryset.count()
        context["featured"] = queryset.filter(is_featured=True).first()
        context["bestseller"] = OrderItem.objects.only('product').distinct("product__name")[:3]
        return context


class ProductDetailView(FormMixin, DetailView):
    model = Product
    form_class = CartAddProductForm

    def post(self, request, *args, **kwargs):
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        if not request.user.is_authenticated:
            messages.error(request, "You Have Login To Post Comment")
            return HttpResponseRedirect(request.headers.get("referer"))

        if request.method == "POST":
            if comment:
                if not rating:
                    rating = 0
                if ProductReview.objects.filter(user=request.user, product=self.get_object()).exists():
                    messages.error(request, "You have already reviewed this product.")
                else:
                    messages.success(request, "Your review has been added successfully!")
                    ProductReview.objects.create(
                        product=self.get_object(), user=request.user, rating=rating, review=comment
                    )
            else:
                messages.error(request, "Invalid review.")

            return HttpResponseRedirect(request.headers.get("referer"))

    def get(self, request, *args, **kwargs):
        self.get_object().num_views = F("num_views") + 1
        self.get_object().save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        category_ids = product.category.all().values_list("id", flat=True)
        context["products"] = Product.objects.filter(category__in=category_ids).exclude(id=product.id)[:12]
        return context


@login_required
def toggle_wishlist(request, slug):
    product = get_object_or_404(Product, slug=slug)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, "Product removed from wishlist.")
    else:
        wishlist.products.add(product)
        messages.success(request, "Product added to wishlist.")

    return HttpResponseRedirect(request.headers.get("referer"))


# class CategoryListView(ListView):
#     model = Category
