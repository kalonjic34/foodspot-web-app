from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = ["Pizza", "pasta", "bread", "salad", "jam", "sushi"]

    context = {"foods":data}
    return render(request,"workspace/index.html",context)