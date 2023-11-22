from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    This is the view will get the user to a specific product details page
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
