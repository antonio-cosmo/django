from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe

# from utils.recipes.factory import make_recipe


def home(req):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(req, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def recipe_show(req, id):
    recipe = get_object_or_404(Recipe, id=id)

    return render(req, 'recipes/pages/recipe_show.html', context={
        'recipe': recipe,
        'is_detail': True
    })


def category(req, id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=id, is_published=True).order_by('-id')
    )
    return render(req, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'Categoria - {recipes[0].category.name}'
    })
