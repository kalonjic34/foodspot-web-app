from . views import register

from django.urls import path, include
app_name ="accounts"
urlpatterns = [
    path("register/", register, name="register"),
    path("", include("django.contrib.auth.urls"))
]
