from django.db import models
from django.contrib.auth.models import User

# Regular Pizza, Sicilian Pizza, Subs, Salads...
class MenuCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

# (Regular Pizza) Cheese, 1 topping, 2 toppings, (Subs) Cheese, italian etc
class MenuItem(models.Model):
    name = models.CharField(max_length=64)
    # optional menu_category so toppings and stand-alone items are better represented.
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_large = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    extra_for = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    is_topping = models.BooleanField(choices=((True, 'Yes'), (False, 'No')), default=False)

    def __str__(self):
        if self.is_topping:
            return f'Pizza topping: {self.name}'
        else:
            return f'''{self.menu_category} - {self.name}
                    { ', extra for ' + self.extra_for if self.extra_for else ''}
                    , Small/Normal: {self.price}/Large: {self.price_large}'''

# https://stackoverflow.com/questions/4910905/in-django-how-do-you-make-a-model-refer-to-itself
class Cart(models.Model):
    # customer_id
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    extra_for = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    
    