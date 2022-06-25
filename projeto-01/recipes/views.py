from django.shortcuts import render


def home(req):
    return render(req, 'recipes/pages/home.html')


def recipe_show(req, id):
    return render(req, 'recipes/pages/recipe_show.html')
