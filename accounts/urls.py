from accounts import views

from . views import register

from django.urls import path, include
app_name ="accounts"
urlpatterns = [
    path("register/", register, name="register"),
    path("", include("django.contrib.auth.urls")),
    path("edit-profile/", views.edit_user_profile, name="edit_user_profile")
]
