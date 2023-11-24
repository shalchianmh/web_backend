from django.db import models
from user.models import User

class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='items')
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Item)
    # slug = models.SlugField(unique=True)


class Ingredient(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='items')
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

class Pizza(Item):
    pizza_id = models.IntegerField(primary_key=True)
    ingredients = models.ManyToManyField(Ingredient)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.slug
    #
    # def get_absolute_url(self):
    #     return reverse('shop:product_detail', kwargs={'slug': self.slug})
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

