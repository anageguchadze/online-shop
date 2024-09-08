from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product

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
        category_id = request.POST.get('item')
        category = Category.objects.get(pk=category_id)
        Product.objects.create(title=title, description=description, price=price, stock=stock, category=category)
        return redirect('add_product')
    product = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product.html', {'product': product, 'category': categories})
