# UpTraderTestTask
Django-приложение для древовидного меню с рендерингом через {% draw_menu 'name' %}. Меню хранится в БД, редактируется в админке, определяет активный пункт по URL. Поддерживает несколько меню на странице. Вложенность: выше активного и первый уровень ниже — развернуты. Один запрос к БД на меню.


**Описание**
- Хранение структуры меню в БД
- Редактирование через стандартную админку Django
- Определение активного пункта по URL текущей страницы
- Поддержка нескольких меню на одной странице
- Оптимизированная загрузка (1 SQL-запрос на меню)
- Поддержка как прямых URL, так и именованных URL

**Установка**
```
git clone https://github.com/pyScripter1/UpTraderTestTask.git
cd UpTraderTestTask
```

**Создайте и активируйте виртуальное окружение**
```
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate      # Windows
```

**Установите зависимости**
```
pip install -r requirements.txt
```

**Применение миграций**
```
python manage.py migrate
```

**Создайте суперпользователя**
```
python manage.py createsuperuser
```

**Запуск**
```
python manage.py runserver
```
