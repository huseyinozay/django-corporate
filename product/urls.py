from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('index/', product_index, name='index'),
    path('<slug:slug>/', product_detail, name='detail'),
]