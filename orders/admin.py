from django.contrib import admin

# Register your models here.
from .models import MenuCategory, MenuItem, Cart
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Cart)



