from django.http import HttpResponse
from django.shortcuts import render
from orders.models import MenuItem, MenuCategory

# Create your views here.
def index(request):
    categories = MenuCategory.objects.all()
    menu = {}
    for category in categories:
        menu[category.name] = {
            'categoryId': category.id,
            'menuItems': MenuItem.objects.filter(category__name=category.name),
        }
    context = {
        'menu': menu,
    }
    return render(request, 'orders/menu.html', context)

def cart(request):
    return HttpResponse("Shopping cart")
