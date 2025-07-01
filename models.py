from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Table(models.Model):
    AVAILABLE = "A"
    AVAILABLE_NOT = "N"
    STATUS_CHOICE = {
        AVAILABLE: 'available',
        AVAILABLE_NOT: 'not available'
    }
    number = models.CharField(max_length=3)
    status = models.CharField(max_length=1, choices = STATUS_CHOICE, default=AVAILABLE)

class Order(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    PENDING = "P"
    DELEVIRED = "D"
    CANCLED = 'C'
    STATUS_CHOICE = {
        PENDING: 'pending',
        DELEVIRED: 'delevired',
        CANCLED: 'cancled',
    }
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=PENDING)

    PAYED = 'P'
    UNPAYED = 'U'
    PAYMENT_CHOICE = {
        PAYED : 'payed',
        UNPAYED : 'unpayed',
    }
    payment = models.CharField(max_length=1, choices= PAYMENT_CHOICE, default= UNPAYED)

    def __str__(self):
        return self.User.username

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)

    


