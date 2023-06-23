from django.db import models
from datetime import datetime


class cat(models.Model):
    cat_name = models.CharField(max_length=255)
    cat_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.cat_name

        
    

class Product(models.Model):

    ship = models.ForeignKey(cat,related_name="lio",default=1,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product,related_name="comments",on_delete=models.CASCADE)
    u_name = models.CharField(max_length=255)
    u_body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


