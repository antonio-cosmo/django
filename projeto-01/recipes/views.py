from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Recipe

# from utils.recipes.factory import make_recipe


def home(req):
    recipes = Recipe.objects.filter(is_published=True)
    return render(req, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def recipe_show(req, id):
    try:
        recipe = Recipe.objects.get(id=id)
        return render(req, 'recipes/pages/recipe_show.html', context={
            'recipe': recipe,
            'is_detail': True
        })
    except Recipe.DoesNotExist:
        return HttpResponse(content='Pagina Não Encontrada', status='404')


def category(req, id):
    recipes = Recipe.objects.filter(category__id=id, is_published=True)
    return render(req, 'recipes/pages/category.html', context={
        'recipes': recipes
    })
