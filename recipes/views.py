from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from foodspot_app.forms import RecipeForm

from .models import Recipe

def recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes":recipes}
    return render(request,"recipes/recipes.html",context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.select_related('user').all()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.user = request.user
            new_comment.save()
            return redirect('recipes:recipe_detail', recipe_id=recipe.id)

    context = {
        'recipe': recipe,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'recipes/recipe.html', context)

def search_results(request):
    query=request.GET.get('query','')
    # results = Recipe.objects.filter(name__icontains=query) if query else []
    if query:
        results = Recipe.objects.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(ingredients__icontains=query)
            | Q(directions__icontains=query)
            | Q(category__name__icontains=query)
        )
        seen_ids  = set()
        unique_results = []
        for result in results:
            if result.id not in seen_ids:
                unique_results.append(result)
                seen_ids.add(result.id)
    else:
        unique_results=[]
    context={
        'query':query, 'results':unique_results
    }
    return render(request, 'recipes/search_results.html',context)
@login_required
def toggle_favorite(request,recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user in recipe.favorited_by.all():
        recipe.favorited_by.remove(request.user)
    else:
        recipe.favorited_by.add(request.user)
    return redirect("recipes:recipe_detail",recipe_id=recipe.id)

@login_required
def favorite_recipes(request):
    favorites = request.user.favorite_recipes.all()
    context = {"recipes": favorites}
    return render(request, "recipes/favorite_recipes.html", context)

@login_required
def delete_recipe(request,recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.user_id != request.user.id:
        return HttpResponseForbidden()
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes:index')
    context = {"recipe": recipe}
    return render(request, "recipes/recipe_confirmation_delete.html", context)

@login_required
def edit_recipe(request,recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if not request.user==recipe.user and not request.user.is_superuser:
        return HttpResponseForbidden()
        
    if request.method=="POST":
        form=RecipeForm(request.POST,request.FILES,instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipes:recipe_detail",recipe_id=recipe.id)
        
    else:
        form=RecipeForm(instance=recipe)
        
    context={
        'form':form,'recipe':recipe
        
    }
    return render(request,"recipes/recipe_form.html",context)