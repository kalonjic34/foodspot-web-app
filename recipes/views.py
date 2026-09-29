from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from comments.forms import CommentForm
from foodspot_app.forms import RecipeForm
from foodspot_app.models import Category
from django.db.models import Q

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