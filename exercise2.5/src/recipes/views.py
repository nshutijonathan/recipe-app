from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView, DetailView  # to display lists

from .models import Recipe
# Create your views here.


class RecipeListView(ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/recipe.html'  # specify template


class RecipeDetailView(DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/recipe-detail.html'


urlpatterns = [
    path('recipes/list', RecipeListView.as_view()),
]
