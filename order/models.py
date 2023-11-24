from django.db import models
from user.models import User
from cart.models import *

class Order(models.Model):
    STATUSES = (
        (u'E', u'Expected'),
        (u'C', u'Canceled'),
        (u'R', u'Rejected'),
        (u'P', u'Paid'),
        (u'S', u'Sent'),
    )
    order_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Item)
    status = models.CharField(max_length=2, null=True, choices=STATUSES, default='E')
    # slug = models.SlugField(unique=True)
