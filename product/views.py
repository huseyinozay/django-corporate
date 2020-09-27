from django.shortcuts import render,get_object_or_404
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def product_index(request):
    products_list = Product.objects.all()

    #Search
    query = request.GET.get('q')
    if query:
        products_list = products_list.filter(Q(name__icontains=query)).distinct()

    #Paginator
    paginator = Paginator(products_list, 12)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'product/index.html', {'products':products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'product/detail.html', context)