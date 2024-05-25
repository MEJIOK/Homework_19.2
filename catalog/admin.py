from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Отображение id и наименования
    list_filter = ('name',)
    search_fields = ('name', 'description')  # Поиск по наименованию и описанию (опционально)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # Отображение id, названия, цены и категории
    list_filter = ('name', 'price', 'category')  # Фильтрация
    search_fields = ('name', 'description', 'category', 'price')  # Поиск по названию  описанию и тд.
