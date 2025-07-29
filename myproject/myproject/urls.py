from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tree_menu.urls')),  # если вы создали urls.py в приложении
]