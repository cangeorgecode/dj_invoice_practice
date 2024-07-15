from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_name
    
class Item(models.Model):
    item_name = models.CharField(max_length=255)

    def __str__(self):
        return self.item_name
    
class Invoice(models.Model):
    invoice_number = models.IntegerField()
    invoice_item = models.ManyToManyField(Item, related_name='item')
    invoice_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_customer.customer_name
