from django.shortcuts import render
from .models import Category
from recipes.models import Recipe

def index(request):
    categories = Category.objects.all()
    context ={"categories":categories}
    return render(request, "foodspot_app/index.html",context)

def recipes(request, category_id):
    recipes = Recipe.objects.filter(category=category_id)
    category= Category.objects.get(pk=category_id)
    context={"recipes":recipes, "category":category}
    return render(request,"foodspot_app/recipes.html",context)