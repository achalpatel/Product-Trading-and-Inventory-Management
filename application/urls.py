from django.urls import path
from application.views import *

urlpatterns=[
    path('index_view/',index_view ),
    path('product_index/',Product_index ),
    path('productListings_index/',productListings_index),
    path('stock_index/', stock_index),
    path('stock_detail_index/', stock_detail_index),
    path('transaction/', transaction),
    path('transaction_detail/', transaction_detail),
    path('admin_dashboard/',admin_dashboard),

]
