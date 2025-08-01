# blog/admin.py
from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, Location, Post

# Этот вариант сработает для всех моделей приложения.
admin.site.empty_value_display = 'Не задано'
# Вместо пустого значения в админке будет отображена строка "Не задано".


def get_model_fields(model):
    return model._meta.get_fields()


class BlogAdmin(admin.ModelAdmin):
    list_editable = ('is_published',)


class PostAdmin(BlogAdmin):

    list_display = [
        field.name
        for field in get_model_fields(Post)
        if field.name not in ('id', 'text')
    ]
    list_display_links = ('title')
    search_fields = (
        'title',
        'text',
    )
    list_filter = (
        'is_published',
        'category',
        'location',
        'author',
    )


class CategoryAdmin(BlogAdmin):

    list_display = (
        'title',
        'is_published',
        'created_at',
        'slug',
    )


class LocationAdmin(BlogAdmin):

    list_display = (
        'name',
        'is_published',
        'created_at',
    )


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
