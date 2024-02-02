from django.db import models
from user.models import User
from cart.models import *


class Order(models.Model):
    STATUSES = [
        (u'Pr', u'Prepared'),
        (u'Pa', u'Paid'),
        (u'S', u'Sent')
    ]
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, null=True, choices=STATUSES, default='E')
