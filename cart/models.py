from django.db import models
from user.models import User


class Good(models.Model):
    good_id = models.AutoField(primary_key=True)
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
    goods = models.ManyToManyField(Good, through='CartGood')
    is_current = models.BooleanField(default=False)

    # slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartGood(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.good.name} in {self.cart}"


