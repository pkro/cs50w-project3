from django.http import HttpResponse
from django.shortcuts import render
from orders.models import MenuItem, MenuCategory

# Create your views here.
def index(request):
    categories = MenuCategory.objects.all().exclude(name="Toppings")
    menu = {}
    for category in categories:
        menu[category.name] = {
            'categoryId': category.id,
            'menuItems': MenuItem.objects.filter(category__name=category.name),
        }
        
    toppings = MenuItem.objects.filter(category__name="Toppings")

    context = {
        'menu': menu,
        'toppings': toppings,
    }
    return render(request, 'orders/menu.html', context)

def cart(request):
    return HttpResponse("Shopping cart")
