from django.urls import path

from .views import ProductDetailView, ProductListView, toggle_wishlist

app_name = "product"

urlpatterns = [
    path("list/", ProductListView.as_view(), name="list"),
    path("detail/<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    # path("categories/", CategoryListView.as_view(), name="categories"),
    path("toggle-wishlist/<slug:slug>/", toggle_wishlist, name="wishlist"),
]
