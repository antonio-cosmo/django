from django.contrib import admin

from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
# Register your models here.
