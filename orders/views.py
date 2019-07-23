from django.http import HttpResponse
from django.shortcuts import render
from orders.models import MenuItem, MenuCategory

# Create your views here.
def index(request):
    menuCategories = MenuCategory.objects.all()
    menu = {}
    for category in menuCategories:
        menu[category.name] = MenuItem.objects.filter(category__name=category.name)

    context = {
        'menu': menu,
    }
    return render(request, 'orders/menu.html', context)

def cart(request):
    return HttpResponse("Shopping cart")
