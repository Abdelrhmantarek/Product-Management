from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from rest_framework import generics
from .serializers import *

# List the products - Read
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Create a product - Create
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list-create')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'form_title': 'Create Product'})

# Update a product - Update
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list-create')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'form_title': 'Update Product'})

# Delete a product - Delete
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list-create')
    return render(request, 'products/product_delete.html', {'product': product})



# API views
# List all products or create a new one
"""
ProductListAPIView
Inherits from generics.ListCreateAPIView, which gives you:
GET /products/ → List all products
POST /products/ → Create a new product
queryset: Defines which data to retrieve (all products)
serializer_class: Says which serializer to use
"""
class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

"""
View
│
├── queryset → The data it grabs from the database
│
└── serializer_class → The instructions for converting that data to/from JSON
"""

# Retrieve, update or delete a single product
"""
ProductDetailAPIView
Inherits from generics.RetrieveUpdateDestroyAPIView, which gives you:
GET /products/<id>/ → Retrieve one product
PUT /products/<id>/ or PATCH /products/<id>/ → Update a product
DELETE /products/<id>/ → Delete a product
Same structure: queryset + serializer_class
"""
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# List the products - Read
# class ProductListCreateView(ListView):
#     model = Product
#     template_name = 'products/product_list.html'
#     context_object_name = 'products'


# Create a product - Create
# class ProductCreateView(CreateView):
#     model = Product
#     template_name = 'products/product_form.html'
#     form_class = ProductForm
#     success_url = reverse_lazy('product-list-create')
    
#     def form_valid(self, form):
#         return super().form_valid(form)

# Update a product - Update
# class ProductUpdateView(UpdateView):
#     model = Product
#     template_name = 'products/product_form.html'
#     form_class = ProductForm
#     success_url = reverse_lazy('product-list-create')

# Delete a product - Delete
# class ProductDeleteView(DeleteView):
#     model = Product
#     template_name = 'products/product_delete.html.html'
#     success_url = reverse_lazy('product-list-create')
