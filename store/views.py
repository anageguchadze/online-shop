from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Orders
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Category.objects.create(name=name, description=description)
        return redirect('add_category')
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})


def remove_category(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('add_category')

def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        category_id = request.POST.get('category')  

        try:
            category = Category.objects.get(pk=category_id)
        except ObjectDoesNotExist:
            return render(request, 'product.html', {
                'error': 'Selected category does not exist.',
                'products': Product.objects.all(),
                'category': Category.objects.all(),
            })
        
        Product.objects.create(title=title, description=description, price=price, stock=stock, category=category)
        return redirect('add_product')

    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product.html', {'products': products, 'category': categories})

def remove_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('add_product')

def select_product(request, id):
    if request.method == 'POST':
        selected_product = get_object_or_404(Product, pk=id)
        quantity = request.POST.get('quantity')
        total_price = float(select_product.price) * quantity
        Orders.objects.create(product=selected_product, quantity=quantity, total_price=total_price)
        return redirect('add_product')
    