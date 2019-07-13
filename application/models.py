from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

class Manufacturer(models.Model):
    manuName = models.CharField(max_length=50)
    manuContact = models.IntegerField(null =True, blank = True)
    def __str__(self):
        return self.manuName


class Category(models.Model):
    catName = models.CharField(max_length=50)
    catImg= models.FileField(upload_to='cat_media', blank=True, null=True)
    # isDisplay = models.BooleanField(default=True)

    def __str__(self):
        return self.catName

class SubCategory(models.Model):
    subCatName = models.CharField(max_length=50)
    subCatImg= models.FileField(upload_to='Subcat_media', blank=True, null=True)
    # isDisplay = models.BooleanField(default=True)
    catId= models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.subCatName

class Product(models.Model):
    pName = models.CharField(max_length=50, db_index=True)
    catId = models.ForeignKey(Category, on_delete = models.CASCADE)
    subCatId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pName

class ProductListings(models.Model):
    pId = models.ForeignKey(Product, on_delete = models.CASCADE)
    uName = models.ForeignKey(User, on_delete=models.CASCADE)
    b_price = models.DecimalField(max_digits=10, decimal_places=2)
    s_price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    manuName = models.ForeignKey(Manufacturer, on_delete = models.SET_NULL, null = True, blank= True)
    pdDescription = models.CharField(max_length=100, null=True, blank = True)
    pimg = models.FileField(upload_to='product_media', blank=True, null=True, default='product_media/default.jpg')
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pId)

class Stock(models.Model):
    uName = models.ForeignKey(User,on_delete=models.CASCADE)
    pListId = models.ForeignKey(ProductListings, on_delete = models.CASCADE)
    sQty = models.IntegerField()
    def __str__(self):
        return str(self.pListId)

class StockDetail(models.Model):
    stId = models.ForeignKey(Stock, on_delete=models.CASCADE)
    pNo = models.DecimalField(max_digits=10, decimal_places=5)
    def __str__(self):
        return str(self.stId)


class Transaction(models.Model):
    pListId = models.ForeignKey(ProductListings, on_delete = models.CASCADE)
    s_uId = models.CharField(max_length=50)
    b_uId = models.CharField(max_length=50)
    tDate = models.DateTimeField(auto_now_add = True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tQty = models.IntegerField()
    stock_left = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.pListId)



class TransactionDetail(models.Model):
    tId = models.ForeignKey(Transaction, on_delete = models.CASCADE)
    pNo = models.DecimalField(max_digits=10, decimal_places=5)
    def __str__(self):
        return str(self.tId)
