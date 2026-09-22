from django.http import HttpResponse
from django.shortcuts import render

def comments(request):
    return HttpResponse("hello from comments")