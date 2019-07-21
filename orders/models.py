from django.db import models
from django.contrib.auth.models import User

# Regular Pizza, Sicilian Pizza, Subs, Salads...
class MenuCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

# (Regular Pizza) Cheese, 1 topping, 2 toppings, (Subs) Cheese, italian etc
class MenuItems(models.Model):
    name = models.CharField(max_length=64)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    price_large = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    extra_for = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.menu_category} - {self.name}, extra for {self.extra_for} Small/Normal: {self.price}/Large: {self.price_large}"

# https://stackoverflow.com/questions/4910905/in-django-how-do-you-make-a-model-refer-to-itself
# class Cart(models.Model):
#     # customer_id
#     item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)

    
    