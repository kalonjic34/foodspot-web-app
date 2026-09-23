from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from foodspot_app.forms import RecipeForm
from foodspot_app.models import Category

from .models import Recipe

def recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes":recipes}
    return render(request,"recipes/recipes.html",context)

def recipe(request, recipe_id):
    recipe= Recipe.objects.get(id=recipe_id)
    context = {
        "recipe":recipe
    }
    return render(request, "recipes/recipe.html",context)