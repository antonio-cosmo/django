from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipes/<int:id>/', views.recipe_show, name='recipes-recipe'),

]
