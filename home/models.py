from django.db import models

class Item(models.Model):
    ctg_name=models.CharField(max_length=250)
    img=models.ImageField(blank=True,upload_to='item')

    def __str__(self):
        return str(self.ctg_name)

class Products(models.Model):
    item_id=models.ForeignKey(Item,on_delete=models.CASCADE)
    cost=models.CharField(max_length=100)
    name=models.CharField(max_length=250)
    desc=models.TextField()
    best_seller=models.BooleanField(default=0)
    img=models.ImageField(blank=True,upload_to='products')

    def __str__(self):
        return str(self.name)            

class FestivePack(models.Model):
    cost=models.IntegerField(default=0)
    name=models.CharField(max_length=500)
    desc=models.TextField()
    img=models.ImageField(blank=True,upload_to='FestivePack')

class Review(models.Model):
    pid=models.ForeignKey(Products,on_delete=models.CASCADE)
    rating=models.CharField(max_length=10,default="0")
    name=models.CharField(max_length=250)
    subject=models.TextField(default="")
    desc=models.TextField()
    email=models.CharField(max_length=250,blank=True    )
