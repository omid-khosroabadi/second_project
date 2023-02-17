from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from product.models import Product
from .forms import AddToCart


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['product_update'] = AddToCart(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    form = AddToCart(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_quantity=cleaned_data['quantity'])
    return redirect('cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    cart.remove(product)
    return redirect('cart_detail')


