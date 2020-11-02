from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField("Название типа", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Тип"


class Guide(models.Model):
    type = models.ForeignKey(Type, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    adress = models.TextField("Адрес")
    latitude = models.DecimalField("Ширина", max_digits=9, decimal_places=6, default=0.000000)
    longitude = models.DecimalField("Долгота", max_digits=9, decimal_places=6, default=0.000000)
    radius = models.SmallIntegerField("Радиус зоны звукопокрытия", default=0)

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name = "Справочник устройств"
        verbose_name_plural = "Справочник устройств"
