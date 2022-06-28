from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(req):
    return render(req, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(9)]
    })


def recipe_show(req, id):
    return render(req, 'recipes/pages/recipe_show.html', context={
        'recipe': make_recipe(),
        'is_detail': True
    })
