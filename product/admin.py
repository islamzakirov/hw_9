from django.contrib import admin

from product.models import Burger, Category

# Register your models here.

class BurgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'price')
    list_display_links = ('name',)
    search_fields = ('name', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Burger, BurgerAdmin)