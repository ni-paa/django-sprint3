from django.shortcuts import get_object_or_404, render
from blog.utils import query_category, query_post

# Константа, определяющая количество постов на главной странице
POSTS_MAIN_PAGE = 5


def index(request):
    """Представление для главной страницы."""
    # Получаем список постов, отсортированных по дате публикации
    # и ограничиваем количество POSTS_MAIN_PAGE
    post_list = query_post()[:POSTS_MAIN_PAGE]
    # Создаем контекст для передачи в шаблон
    context = {'post_list': post_list}
    # Рендерим шаблон blog/index.html с переданным контекстом
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    """Представление для детальной страницы поста."""
    # Получаем пост по id или возвращаем 404, если пост не найден
    post_list = get_object_or_404(
        query_post(),  # Используем наш фильтрованный QuerySet
        pk=id,  # Ищем пост с указанным id
    )
    # Создаем контекст для передачи в шаблон
    context = {'post': post_list}
    # Рендерим шаблон blog/detail.html с переданным контекстом
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Представление для страницы категории."""
    # Получаем категорию по slug или возвращаем 404, если категория не найдена
    category = get_object_or_404(
        # Используем наш фильтрованный QuerySet для категорий
        query_category(),
        # Ищем категорию с указанным slug
        slug=category_slug,
    )
    # Получаем посты для этой категории, отсортированные по дате публикации
    post_list = (
        query_post()
        .filter(category=category)  # Фильтруем посты по категории
        .order_by('-pub_date')
    )
    # Создаем контекст для передачи в шаблон
    context = {'category': category, 'post_list': post_list}
    # Рендерим шаблон blog/category.html с переданным контекстом
    return render(request, 'blog/category.html', context)
