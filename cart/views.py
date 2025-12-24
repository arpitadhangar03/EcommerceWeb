from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .models import Cart, CartItem
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages

def _get_user_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key or request.session.save()
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

@require_POST
def add_to_cart(request, product_id):
    cart = _get_user_cart(request)
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f"{product.name} added to cart!")
    return redirect(request.META.get('HTTP_REFERER', reverse('home')))

def view_cart(request):
    cart = _get_user_cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

@require_POST
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart=_get_user_cart(request))
    quantity = int(request.POST.get('quantity', 1))
    if quantity < 1:
        item.delete()
    else:
        item.quantity = quantity
        item.save()
    return redirect('cart:view_cart')

@require_POST
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart=_get_user_cart(request))
    item.delete()
    messages.info(request, f"{item.product.name} removed from cart!")
    return redirect('cart:view_cart')
