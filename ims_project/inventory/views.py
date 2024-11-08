# myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from .forms import ProductForm
from .decorators import admin_required  # Import the custom admin_required decorator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# View for the product list (accessible to all users)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


# View to display product details
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

# View for adding a product (restricted to admin only)
@admin_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list after saving
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

# View for editing a product (restricted to admin only)
@admin_required
def product_edit(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # After saving, redirect to the list page
    else:
        form = ProductForm(instance=product)  # Pre-populate form with existing product data
    return render(request, 'product_form.html', {'form': form, 'title': 'Edit Product'})

# View for deleting a product (restricted to admin only)
@admin_required
def delete_product(request, product_id):
    product = Product.objects.filter(product_id=product_id).first()
    if product:
        product.delete()
        return redirect('product_list')
    else:
        return HttpResponse("Product not found", status=404)

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')  # Redirect to product list after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('product_list')  # Redirect to product list after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
