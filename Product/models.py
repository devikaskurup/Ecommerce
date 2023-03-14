from django.db import models
from django.contrib.auth.models import User

class ProductDetails(models.Model):
    
    option =(
        ("mens","mens"),
        ("womans","womans"),
        ("kids","kids")
        )

    productId = models.AutoField(primary_key=True)
    produc_tName = models.CharField(max_length=255)
    product_Brand = models.CharField(max_length=255)
    product_Discription = models.CharField(max_length=1000)
    product_price = models.IntegerField()
    product_category=models.CharField(max_length=255,choices=option)
    product_image = models.ImageField(upload_to="product_image")
    product_stock=models.PositiveIntegerField()
    merchant = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    
