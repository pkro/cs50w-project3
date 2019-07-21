from django.contrib import admin

# Register your models here.
from .models import MenuCategory, MenuItems, Cart
admin.site.register(MenuCategory)
admin.site.register(MenuItems)
admin.site.register(Cart)



