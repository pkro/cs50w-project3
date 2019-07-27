from django.db import models
from django.contrib.auth.models import User

# Regular Pizza, Sicilian Pizza, Subs, Salads...
class MenuCategory(models.Model):
    name = models.CharField(max_length=64)
    # order of the items in the menu
    order = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

# (Regular Pizza) Cheese, 1 topping, 2 toppings, (Subs) Cheese, italian etc
class MenuItem(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_large = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    extra_for = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    toppings_required = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'''{self.category} - {self.name}
                    { ', extra for ' + self.extra_for.name if self.extra_for else ''}
                    , Small/Normal: {self.price}/Large: {self.price_large}'''

class Cart(models.Model):
    pass
    # customer_id
    # created_on = models.DateTimeField(auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now=True)
    # active = models.BooleanField(default=True)

class CartItem(models.Model):
    pass
    # cart = models.ManyToManyField('Cart')
    # item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    # # Cart needs its own extra_for referring to items in the cart
    # extra_for = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    
    