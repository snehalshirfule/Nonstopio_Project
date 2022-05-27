from django.db import models

# Create your models here.
class products(models.Model):
    shape = models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    price = models.BigIntegerField()

    class Meta:
        db_table = "products"

class user(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = "user"

# class recommendations(models.Model):
#     products = models.ForeignKey(products,on_delete= models.CASCADE)
#     user = models.ForeignKey(user,on_delete= models.CASCADE)

#     class Meta:
#         db_table = "recommendations"