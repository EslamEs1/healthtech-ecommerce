from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from taggit.models import Tag

from .models import Blog, Category, Comment, InstagramImage


class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        slug = self.kwargs.get("slug")
        tag = self.kwargs.get("id")

        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(description__icontains=search))

        if slug:
            queryset = queryset.filter(category__slug=slug)

        if tag:
            queryset = queryset.filter(tags__in=[tag])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["popular"] = self.get_popular_blogs()[:3]
        context["category"] = Category.objects.only("name").annotate(count=Count("blog"))
        context["instmage"] = InstagramImage.objects.all()[:9]
        context["tags"] = Tag.objects.annotate(num_products=Count("name"), count=Count("blog")).filter(num_products=1)
        return context

    def get_popular_blogs(self):
        return self.get_queryset().order_by("-views_count")


class BlogDetailView(DetailView):
    model = Blog

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        blog = self.get_object()
        blog.views_count += 1
        blog.save()
        return response

    def post(self, request, *args, **kwargs):
        comment = self.request.POST.get("comment")
        blog = self.get_object()
        if comment:
            comment, created = Comment.objects.get_or_create(content=comment, author=request.user, blog=blog)
            if created:
                messages.success(request, "Your comment has been added successfully.")
            else:
                messages.error(request, "You already have a comment.")
        else:
            messages.error(request, "Your comment is invalid.")

        return redirect(self.request.headers.get("referer"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        context["popular"] = self.get_popular_blogs().exclude(id=blog.id)[:3]
        context["category"] = Category.objects.only("name").annotate(count=Count("blog"))
        context["tags"] = Tag.objects.annotate(num_products=Count("name"), count=Count("blog")).filter(num_products=1)
        context["prev"] = self.get_queryset().filter(created_at__lt=blog.created_at)
        context["next"] = self.get_queryset().filter(created_at__gt=blog.created_at)
        context["comments"] = Comment.objects.filter(blog_id=blog.id)
        return context

    def get_popular_blogs(self):
        return self.get_queryset().filter(category=self.object.category).order_by("-views_count")


def inst_img(request):
    context = {}
    context["images"] = InstagramImage.objects.all
    return render(request, "gallery.html", context)
