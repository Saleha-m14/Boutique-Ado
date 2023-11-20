from django.shortcuts import render
from .models import Product
# Create your views here.


def all_products(request):
    """
    This view will show all the products, including sorting and search queris
    """
    # return all products from the database
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
    
