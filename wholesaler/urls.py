from django.urls import path
from wholesaler.views import *
from application.views import Product_index, productListings_index

urlpatterns=[
    path('', w_index),
    path('w_add_product', w_add_product),
    path('w_inventory', w_inventory),
    path('w_stockDetail/', w_stockDetail),
    path('w_transaction/', w_transaction),
    path('w_transactionDetail/', w_transactionDetail),
    path('w_add_quantity/', w_add_quantity),
    path('w_product_listing/', w_product_listing),
    path('w_update_price/', w_update_price),
    path('w_invoice/',w_invoice),
    path('w_subcat/',w_subcat),
    path('w_product_index/', Product_index),
    path('w_productListings_index/', productListings_index),

]
