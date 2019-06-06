from django.db import models

# Create your models here.
# Regular Pizza, Sicilian Pizza, Subs, Salads...
class FoodType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

# (Regular Pizza) Cheese, 1 topping, 2 toppings, (Subs) Chees, italian etc
class FoodSubtype(model.Model):
    name = models.CharField(max_length=64)
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.foodtype} - {self.name}"


# Pizza toppings
class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Price(models.Model):
    price = models.DecimalField(max_digits=4, decimal_places=2)
    price_large = models.DecimalField(max_digits=4, decimal_places=2)
    foodsubtype = models.ForeignKey(FoodSubtype, on_delete=models.CASCADE)
    
    def __str__(self, size="small"):
        if size=="small":
            return f"{self.price}"
        else:
            return f"{self.price_large}"

class SubsExtra(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    price_large = models.DecimalField(max_digits=4, decimal_places=2)
    sub = models.ManyToManyField(FoodSubtype, related_name="extras")

    def __str__(self, size="small"):
        if size=="small":
            return f"{self.price}"
        else:
            return f"{self.price_large}"