from django.shortcuts import render

def index(request):
    return render(request, "foodspot_app/index.html")