from django.urls import path
from retailer.views import *

urlpatterns=[
    path('',r_index),
    path('r_product_index/', r_product_index),
    path('r_productListings/', r_productListings),
    path('r_buy_product/', r_buy_product),
    path('r_inventory/', r_inventory),
    path('r_stockDetail/', r_stockDetail),
    path('r_transaction/', r_transaction),
    path('r_transactionDetail/', r_transactionDetail),
    path('r_sell_product_index/', r_sell_product_index),
    path('r_subcat/', r_subcat),
    path('r_invoice/', r_invoice),
]
