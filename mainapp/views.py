from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import BasketItem


# Create your views here.
def main(request):
    products = Product.objects.all()
    title = 'Home page'
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)

    basket = []
    if request.user.is_authenticated:
        basket = BasketItem.objects.filter(user=request.user)

    title = 'Catalog'
    categories = ProductCategory.objects.all()

    if pk:
        if pk == '0':
            category = {'name': 'ALL PRODUCTS'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'categories_list': categories,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    else_products = Product.objects.all().order_by('price')
    content = {
        'title': title,
        'categories_list': categories,
        'products': else_products
    }
    return render(request, 'mainapp/catalog.html', content)


def contacts(request):
    title = 'Contacts'
    content = {'title': title}
    return render(request, 'mainapp/contact.html', content)


def getBasketItems(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def product(request, pk):
    title = 'products'
    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': getBasketItems(request.user),
    }
    return render(request, 'mainapp/product.html', content)
