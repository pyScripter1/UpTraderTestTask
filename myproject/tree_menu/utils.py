from django.urls import resolve, Resolver404
from tree_menu.models import MenuItem


def get_current_menu_item(menu_items, current_path):
    """
    Определяет текущий пункт меню на основе URL
    """
    for item in menu_items:
        if item.get_url() == current_path:
            return item
    return None


def build_menu_tree(menu_items, current_item=None):
    """
    Строит дерево меню с учетом текущего пункта
    """
    tree = []
    lookup = {}

    # Создаем lookup таблицу для быстрого поиска
    for item in menu_items:
        lookup[item.id] = {
            'item': item,
            'children': []
        }

    # Строим дерево
    for item in menu_items:
        if item.parent_id:
            lookup[item.parent_id]['children'].append(lookup[item.id])
        else:
            tree.append(lookup[item.id])

    # Размечаем активные пункты
    if current_item:
        mark_active_items(tree, current_item)

    return tree


def mark_active_items(tree, current_item):
    """
    Помечает активные пункты меню (текущий и его родителей)
    """
    for node in tree:
        if node['item'].id == current_item.id:
            node['is_active'] = True
            node['is_expanded'] = True
            return True

        if mark_active_items(node['children'], current_item):
            node['is_active_parent'] = True
            node['is_expanded'] = True
            return True

    return False