from django.shortcuts import render


# Create your views here.
def view_bag(request):
    """
    A view to retun bag content 
    """
    return render(request, 'bag/bag.html')
