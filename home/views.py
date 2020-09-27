from django.shortcuts import render,get_object_or_404
from product.models import Product


def home_view(request):
    product = Product.objects.all()
    context = {
        'products': product,
    }
    return render(request, 'home.html', context)
