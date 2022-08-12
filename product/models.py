from django.db import models

# Create your models here.
from user.models import User


class Product(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(max_length=300)
    price = models.IntegerField()
    is_active = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    
class SubscribedProduct(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribe_at = models.DateTimeField(auto_now=True)
    