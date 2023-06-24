from django.contrib import admin

from .models import Blog, Image, Category, Comment, InstagramImage


class BlogImageInline(admin.TabularInline):
    model = Image
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline, CommentInline]


@admin.register(InstagramImage)
class InstagramImageAdmin(admin.ModelAdmin):
    pass
