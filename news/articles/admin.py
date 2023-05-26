from django.contrib import admin
from .models import Article, Comment

# Register your models here.

#there are two inline tabularinline and stackeinline , I am using tabular one 
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
            CommentInline,
            ]

admin.site.register(Article)
admin.site.register(Comment)
