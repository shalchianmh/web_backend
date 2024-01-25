from django.db import models
from user.models import User


class Good(models.Model):
    item_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='items', blank=True, null=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    goods = models.ManyToManyField(Good, through='CartItem')
    is_current = models.BooleanField(default=False)

    # slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.good.name} in {self.cart}"


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='items', null=True, blank=True)
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ingredient_id}"


class Pizza(Good):
    pizza_id = models.AutoField(primary_key=True)
    ingredients = models.ManyToManyField(Ingredient, through='PizzaIngredient', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class PizzaIngredient(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
