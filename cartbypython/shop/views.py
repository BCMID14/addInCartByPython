from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import Product
import json
from django.core.serializers import serialize


def index(request):
    products = Product.objects.all()
    
    productCart = request.session.get('carts', [])
    
    product_data = [products for products in productCart]
    number_product_by_quantity = 0
    
    for product_in_cart in product_data:
        number_product_by_quantity += int(product_in_cart['quantity'])
    return render(request, "home/index.html", {'products': products, 'numberOfProduct': number_product_by_quantity})

def product(request, param):
    product_id = int(param)
    product = Product.objects.get(id=product_id)
    
    productCart = request.session.get('carts', [])
    
    product_data = [products for products in productCart]
    number_product_by_quantity = 0
    
    for products in product_data:
        number_product_by_quantity += int(products['quantity'])
    return render(request, "products/product.html", {'product': product, 'numberOfProduct': number_product_by_quantity})

def cart(request):
    productCart = request.session.get('carts', [])
    
    product_data = [products for products in productCart]
    
    soustotal_price = 0
    number_product_by_quantity = 0
    
    for products in product_data:
        soustotal_price += float(products['price'])
        number_product_by_quantity += int(products['quantity'])
        
    total_price = soustotal_price + 10
    return render(request, "cart/cart.html", {'productCart': product_data, 'soustotalPrice': soustotal_price, 'total_price': total_price, 'numberOfProduct': number_product_by_quantity})

def cartProduct(request, param):
    product_id = int(param)
    product = Product.objects.get(id=product_id)
    
    cartProducts = request.session.get('carts', [])
    new_quantity = 1
    price_unity_product = product.price
    
    
    product_ids = [product['id'] for product in cartProducts]
    if product_id not in product_ids:
          productCart_data = {
                    'id' : product.id,
                    'title' : product.title,
                    'description': product.description,
                    'price': product.price,
                    'image': product.image.url,
                    'quantity': 1
                }
          cartProducts.append(productCart_data)
    else:
        for productCart in cartProducts:
            if productCart['id'] == product_id:
                productCart['quantity'] += new_quantity
                new_price = price_unity_product * productCart['quantity']
                productCart['price'] = new_price
            
    request.session['carts'] = cartProducts
    return redirect('/panier')

def cartUpdateQuantityProduct(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('productIdentifiant')
        
        product_id_int = int(product_id)
        product = Product.objects.get(id=product_id_int)
        price_unity_product = product.price
        
        cartProducts = request.session.get('carts', [])
        new_quantity = int(quantity)

        for productCart in cartProducts:
            if productCart['id'] == product_id_int:
                new_price = price_unity_product * int(quantity)
                productCart['price'] = new_price
                productCart['quantity'] = new_quantity

    request.session['carts'] = cartProducts
    return redirect('/panier')
    
def removeProduct(request, param):
    cartProducts = request.session.get('carts', [])
    product_id = int(param)
    
    for product in cartProducts:
        if product['id'] == product_id:
            cartProducts.remove(product)
            break

    request.session['carts'] = cartProducts
    return redirect('/panier')