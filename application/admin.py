from django.contrib import admin
from application.models import *
from django.contrib.admin import AdminSite
# Register your models here.

AdminSite.site_url = '/index_view/'

admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductListings)
admin.site.register(Stock)
admin.site.register(StockDetail)
admin.site.register(Transaction)
admin.site.register(TransactionDetail)
