from django.db import models
from user.models import User

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='items', null=True, blank=True)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.ingredient_id}"

class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='items', blank=True, null=True)
    name = models.CharField(max_length=250, null=True)
    price = models.PositiveIntegerField(max_length=250, default=0)
    def __str__(self):
        return f"{self.pizza_id}"


class PizzaIngredient(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pizza', 'ingredient'], name='pizza_ingredient_key'
            )
        ]