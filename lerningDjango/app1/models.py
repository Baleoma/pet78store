from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=512)
    price = models.FloatField()
    stock = models.IntegerField()
    sale = models.FloatField(default=0.00)
    forkids = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.name

    @property
    def price_with_discount(self):
        if self.sale > 0:
            return round(float(self.price) - float(self.price) * float(self.sale), 2)
        else:
            return self.price

    @property
    def sale_display(self):
        if self.sale > 0:
            return round(self.sale * 100)
        else:
            return self


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


