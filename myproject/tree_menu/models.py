from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.text import slugify


class Menu(models.Model):
    """
    Модель для хранения меню (контейнер для пунктов меню)
    """
    name = models.CharField('Название меню', max_length=100, unique=True)
    slug = models.SlugField('Слаг меню', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class MenuItem(models.Model):
    """
    Модель для хранения пунктов меню
    """
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        verbose_name='Меню',
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        related_name='children',
        verbose_name='Родительский пункт',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    title = models.CharField('Название пункта', max_length=100)
    url = models.CharField('Ссылка', max_length=255, blank=True)
    named_url = models.CharField('Именованная ссылка', max_length=100, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_url(self):
        """
        Возвращает URL для пункта меню
        """
        if self.named_url:
            try:
                url = reverse(self.named_url)
            except NoReverseMatch:
                url = self.url
            return url
        return self.url