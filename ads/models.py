from django.db import models


class Advertisement(models.Model):
    title = models.TextField(verbose_name="Заголовок")
    author = models.TextField(verbose_name="Автор")
    views_count = models.IntegerField(verbose_name="Количество просмотров")
    ad_position = models.IntegerField(verbose_name="Позиция в списке")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
