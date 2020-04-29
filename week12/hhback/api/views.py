from django.shortcuts import render

# Create your views here.

from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
def hello(request):
    return HttpResponse('<h1>Hello msg</h1>')

# def product_list(request):
#     return HttpResponse('<h1>product list</h1>')
#
# def product_detail(request, product_id):
#     return HttpResponse(f'<h1>product id:{product_id}</h1>')

# products = []
#
# for i in range(1, 5):
#     products.append(
#         {
#         'name': f'product {i}',
#         'id': i,
#         'price': i*1000,
#         'description': f'{i} is best of the best',
#         'count': i*10,
#         }
#     )

def category_list(request):
    pass

def category_detail(request, category_id):
    pass

def category_products(args):
    pass


products = [
        {
        'name': f'product {i}',
        'id': i,
        'price': i*1000,
        'description': f'{i} is best of the best',
        'count': i*10,
        } for i in range(1, 5)
]


def product_list(request):

    return JsonResponse(products, safe=False)

def product_detail(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product)
    return JsonResponse({'error': 'product does not exist'})