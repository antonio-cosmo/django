from django.shortcuts import render
from utils.recipes.factory import make_recipe

from .models import Recipe


def home(req):
    recipes = Recipe.objects.all()
    return render(req, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def recipe_show(req, id):
    recipe = Recipe.objects.get(id=id)
    return render(req, 'recipes/pages/recipe_show.html', context={
        'recipe': recipe,
        'is_detail': True
    })


def category(req):
    return render(req, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(9)]
    })
