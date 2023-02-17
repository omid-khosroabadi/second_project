from django.contrib import admin
from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['body', 'star', 'author']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'datetime_created', ]
    inlines = [
        CommentInline,
    ]
#
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     fields = ['body', 'star', 'author']
#
#


