from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product
from cart.models import Cart ,CartItem # cart model import krna hoga

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remove_from_wishlist(request, product_id):
    Wishlist.objects.filter(user=request.user, product__id=product_id).delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def wishlist_page(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist_page.html', {'wishlist': wishlist_items})

@login_required
def move_to_cart(request, product_id):
    # Wishlist se remove
    Wishlist.objects.filter(user=request.user, product__id=product_id).delete()

    # User ka cart laao (ya banao agar nahi hai)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    # Product fetch
    product = get_object_or_404(Product, pk=product_id)

    # CartItem check karo (agar product already hai toh qty +1, warna new entry)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))
