from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Menu")

def cart(request):
    return HttpResponse("Shopping cart")
