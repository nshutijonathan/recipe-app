from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView, DetailView  # to display lists
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
# Create your views here.


class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/recipe.html'  # specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/recipe-detail.html'


urlpatterns = [
    path('recipes/list', RecipeListView.as_view()),
]
