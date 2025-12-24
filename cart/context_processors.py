from .models import Cart

def cart_count(request):
    def _get_user_cart(request):
        if request.user.is_authenticated:
            try:
                return Cart.objects.get(user=request.user)
            except Cart.DoesNotExist:
                return None
        else:
            session_key = request.session.session_key or request.session.save()
            try:
                return Cart.objects.get(session_key=request.session.session_key)
            except Cart.DoesNotExist:
                return None
    cart = _get_user_cart(request)
    count = cart.total_items() if cart else 0
    return {'cart_count': count}
