from django import template
from django.core.cache import cache
from tree_menu.models import Menu
from ..utils import get_current_menu_item, build_menu_tree
register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path_info

    # Пробуем получить меню из кеша
    cache_key = f'menu_{menu_name}_{current_path}'
    cached_menu = cache.get(cache_key)
    if cached_menu:
        return cached_menu

    try:
        menu = Menu.objects.prefetch_related('items').get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': []}

    menu_items = menu.items.all()
    current_item = get_current_menu_item(menu_items, current_path)
    menu_tree = build_menu_tree(menu_items, current_item)

    # Кешируем результат
    result = {
        'menu_name': menu_name,
        'menu_tree': menu_tree,
        'current_path': current_path
    }
    cache.set(cache_key, result, 60 * 15)  # Кешируем на 15 минут

    return result