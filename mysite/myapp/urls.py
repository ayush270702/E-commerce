
from django.urls import path

from . import views


app_name = 'myapp'

urlpatterns = [
    path('', views.index),
    
    path('product/', views.products, name='products'),
    # path('product/', views.ProductListView.as_view(), name='products'),
    
    # path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    
    path('product/add/', views.add_product, name='add_product'),
  
    path('product/<int:pk>/update', views.update_product, name='update_product'),
    path('product/<int:pk>/delete', views.del_product, name='del_product'),
    path('product/mylistings/', views.my_listings, name='mylistings'),
]

