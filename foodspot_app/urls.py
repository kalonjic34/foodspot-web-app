from . import views
from django.urls import path

app_name = "foodspot_app"

urlpatterns = [
    path("",views.index, name="index"),
    path("recipes/<int:category_id>/",views.recipes, name="recipes"),
    path("add-category",views.add_category, name="add_category"),
    path("add_recipe",views.add_recipe, name="add_recipe_no_genre")
]
