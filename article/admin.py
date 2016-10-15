from django.contrib import admin


# Register your models here.
from article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'keyset', 'created_at')

admin.site.register(Article, ArticleAdmin)
