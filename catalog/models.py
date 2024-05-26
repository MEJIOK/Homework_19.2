from django.db import models


NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=255, verbose_name="Название категории", )
    description = models.TextField(verbose_name="Описание категории", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта", **NULLABLE)
    image = models.ImageField(upload_to="products/", verbose_name="Фото продукта", **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория",
                                 related_name="Products", **NULLABLE)
    price = models.IntegerField(verbose_name="Цена продукта", **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", **NULLABLE)
    updated_at = models.DateField(verbose_name="Дата изменения", **NULLABLE)
    manufactured_at = models.DateField(verbose_name="Дата изготовления", **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = 'Продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Продукты'  # Настройка для наименования набора объектов
