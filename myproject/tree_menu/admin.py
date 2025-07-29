from django.contrib import admin
from django import forms
from .models import Menu, MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get('url')
        named_url = cleaned_data.get('named_url')

        if url and named_url:
            raise forms.ValidationError(
                'Заполните только одно из полей: URL или Именованный URL'
            )
        if not url and not named_url:
            raise forms.ValidationError(
                'Необходимо заполнить одно из полей: URL или Именованный URL'
            )

        return cleaned_data


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    form = MenuItemForm
    extra = 1
    fields = ('title', 'parent', 'url', 'named_url', 'order')
    ordering = ('order',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    inlines = (MenuItemInline,)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'url', 'named_url', 'order')
    list_filter = ('menu',)
    form = MenuItemForm