from django.urls import path

from .views import BlogDetailView, BlogListView

app_name = "blog"

urlpatterns = [
    path("list/", BlogListView.as_view(), name="blog_list"),
    path("list/filter/<slug:slug>/", BlogListView.as_view(), name="filter"),
    path("list/tag/<int:id>/", BlogListView.as_view(), name="tag_filter"),
    path("detail/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
]
