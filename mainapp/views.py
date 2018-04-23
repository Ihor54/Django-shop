from django.shortcuts import render


# Create your views here.
def main(request):
    new_products = [
        {'href': '', 'src': "{% static 'img/index/products/mavic_pro.jpg' %}",
         'name': 'DJI Mavic Pro', 'price': '$.1300.00'},
        {'href': '', 'src': "{% static 'img/index/products/sky.jpg' %}",
         'name': 'Parrot Disco FPV Sky Controller', 'price': '$.1000.00'},
        {'href': '', 'src': "{% static 'img/index/products/parrot_ar2.jpg' %}",
         'name': 'Parrot AR.Drone 2.0', 'price': '$.400.00'},
        {'href': '', 'src': "{% static 'img/index/products/drocon.jpg' %}",
         'name': 'DROCON Blue Bugs', 'price': '$.140.00'},
        {'href': '', 'src': "{% static 'img/index/products/phantom3.jpg' %}",
         'name': 'DJI Phantom 3', 'price': '$.640.00'},
        {'href': '', 'src': "{% static 'img/index/products/syma_x5.jpg' %}",
         'name': 'Syma X5HW ', 'price': '$.110.00'}
    ]
    top_products = [
        {'href': '', 'src': "{% static 'img/index/products/mavic_pro.jpg' %}",
         'name': 'DJI Mavic Pro', 'price': '$.1300.00'},
        {'href': '', 'src': "{% static 'img/index/products/phantom3.jpg' %}",
         'name': 'DJI Phantom 3', 'price': '$.640.00'},
        {'href': '', 'src': "{% static 'img/index/products/sky.jpg' %}",
         'name': 'Parrot Disco FPV Sky Controller', 'price': '$.1000.00'}
    ]
    sale_products = [
        {'href': '', 'src': "{% static 'img/index/products/syma_x5.jpg' %}",
         'name': 'Syma X5HW ', 'price': '$.110.00'},
        {'href': '', 'src': "{% static 'img/index/products/parrot_ar2.jpg' %}",
         'name': 'Parrot AR.Drone 2.0', 'price': '$.400.00'},
        {'href': '', 'src': "{% static 'img/index/products/drocon.jpg' %}",
         'name': 'DROCON Blue Bugs', 'price': '$.140.00'},
    ]
    content = {'new_products': new_products, 'top_products': top_products, 'sale_products': sale_products}
    return render(request, 'mainapp/index.html', content)


def products(request):
    products = [
        {'href': '', 'src': "{% static 'img/index/products/mavic_pro.jpg' %}",
         'name': 'DJI Mavic Pro', 'price': '$.1300.00'},
        {'href': '', 'src': "{% static 'img/index/products/sky.jpg' %}",
         'name': 'Parrot Disco FPV Sky Controller', 'price': '$.1000.00'},
        {'href': '', 'src': "{% static 'img/index/products/parrot_ar2.jpg' %}",
         'name': 'Parrot AR.Drone 2.0', 'price': '$.400.00'},
        {'href': '', 'src': "{% static 'img/index/products/drocon.jpg' %}",
         'name': 'DROCON Blue Bugs', 'price': '$.140.00'},
        {'href': '', 'src': "{% static 'img/index/products/phantom3.jpg' %}",
         'name': 'DJI Phantom 3', 'price': '$.640.00'},
        {'href': '', 'src': "{% static 'img/index/products/syma_x5.jpg' %}",
         'name': 'Syma X5HW ', 'price': '$.110.00'},
        {'href': '', 'src': "", 'name': 'Product', 'price': '$.1000.00'},
        {'href': '', 'src': "", 'name': 'Product', 'price': '$.1000.00'},
        {'href': '', 'src': "", 'name': 'Product', 'price': '$.1000.00'},
        {'href': '', 'src': "", 'name': 'Product', 'price': '$.1000.00'},
        {'href': '', 'src': "", 'name': 'Product', 'price': '$.1000.00'},
        {'href': '', 'src': "", 'name': 'Product', 'price': '$.1000.00'},
        {'href': '', 'src': "", 'name': 'Product', 'price': '$.1000.00'},
        {'href': '', 'src': "", 'name': 'Product', 'price': '$.1000.00'},
        {'href': '', 'src': "", 'name': 'Product', 'price': '$.1000.00'}
    ]
    content = {'products': products}
    return render(request, 'mainapp/catalog.html', content)


def contacts(request):
    return render(request, 'mainapp/contact.html')
