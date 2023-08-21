from django.db import models

class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.dish_name


class Order(models.Model):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered')
    ]

    customer_name = models.CharField(max_length=100)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return f"Order ID: {self.pk}, Customer: {self.customer_name}, Status: {self.get_order_status_display()}"
