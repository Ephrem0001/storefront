from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    invetorty = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = (
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default= MEMBERSHIP_BRONZE)
    
class Order(models.Model):
    payment_status_pending = 'P'
    payment_status_completed = 'C'
    payment_status_failed = 'F'

    payment_status_choices = (
        (payment_status_pending, 'Pending'),
        (payment_status_completed, 'Completed'),
        (payment_status_failed, 'Failed')
    )
    
    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=payment_status_choices, default=payment_status_pending)

