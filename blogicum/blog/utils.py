from django.utils import timezone
from blog.models import Category, Post


def query_post():
    """Функция для получения опубликованных постов."""
    # Получение текущего времени с учетом временной зоны
    time_now = timezone.now()
    # Создание QuerySet для получения постов с оптимизацией запросов
    query_set = (
        # Используем select_related для уменьшения количества запросов
        Post.objects.select_related(
            'category',  # Оптимизация для поля category
            'location',  # Оптимизация для поля location
            'author',  # Оптимизация для поля author
        )
        .filter(
            # Посты с датой публикации не позднее текущего времени
            pub_date__lte=time_now,
            # Только опубликованные посты
            is_published=True,
            # Только посты из опубликованных категорий
            category__is_published=True,
        )
    )
    return query_set


def query_category():
    """Функция для получения опубликованных категорий."""
    query_set = Category.objects.filter(
        is_published=True  # Только опубликованные категории
    )
    return query_set
