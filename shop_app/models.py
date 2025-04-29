from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.price}$'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f'{self.name} {self.description}'

