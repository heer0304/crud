from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=25) 
    last_name = models.CharField(max_length=25)
    contact_no = models.CharField(max_length=15)
    pincode = models.IntegerField()

    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=8,decimal_places=2)
    qty = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=12,decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_id