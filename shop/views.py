from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from django.contrib.auth.decorators import login_required

def shop_page(request):
    category = Category.objects.all()
    products = Product.objects.filter(is_draft=False)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/shop.html', context)


def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    ctg = Category.objects.get(name=product_details.category)
    related_products = Product.objects.filter(category=ctg)
    invertory = product_details.inventory
    context = {
        'product': product_details,
        'related_products': related_products,
        'invertory':invertory
    }
    return render(request, 'shop/product-details.html', context)




def category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)
    return render(request, "shop/category.html", {'category': category, 'products': products})