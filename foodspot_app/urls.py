from . import views
from django.urls import path

app_name = "foodspot_app"

urlpatterns = [
    path("",views.index, name="index"),
    path("recipes/<int:category_id>/",views.recipes, name="recipes")
]
