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

    def __str__(self):
        return f"{self.foodtype} - {self.name}, Small/Normal: {self.price}/Large: {self.price_large}"

# for Items that are the same for different categories ("extra cheese"), just add a distinct item for each
class MenuExtras(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    price_large = models.DecimalField(max_digits=4, decimal_places=2)
    valid_food_items = models.ManyToManyField(MenuItems, related_name="menu_extras")

    def __str__(self):
        return f"{self.name} - Small/Normal: {self.price}/{self.price_large}"