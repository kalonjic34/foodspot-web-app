from django.shortcuts import redirect, render

from foodspot_app.forms import CategoryForm, RecipeForm
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

def add_category(request):
    if request.method =="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("foodspot_app:index")
        else:
            return render(request, "foodspot_app/add_category.html",context)
    else:
        form=CategoryForm()
        context={"form":form}
        return render(request, "foodspot_app/add_category.html",context)
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("foodspot_app:index")
    else:
        form = RecipeForm()

    return render(request, "foodspot_app/add_recipe.html", {"form": form})