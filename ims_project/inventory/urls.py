# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),             # List all products
    path('products/add/', views.product_add, name='product_add'),            # Add a new product
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),  # View product details
    path('products/<int:product_id>/edit/', views.product_edit, name='product_edit'), # Edit a product
    path('products/<int:product_id>/delete/', views.delete_product, name='product_delete'),
    path('login/', views.login_view, name='login'),  # Add this line for login
    path('signup/', views.signup_view, name='signup'),  # Add this line for signup
]
