from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Create (Add) Product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/product_form.html', {'form': form})

# Read (List) Products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

# Update Product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/product_form.html', {'form': form})

# Delete Product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product/product_confirm_delete.html', {'product': product})
