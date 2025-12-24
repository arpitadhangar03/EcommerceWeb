from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'created_at', 'total_items_display', 'total_price_display')
    search_fields = ('user__username', 'session_key')
    readonly_fields = ('created_at',)

    def total_items_display(self, obj):
        return obj.total_items()
    total_items_display.short_description = 'Total Items'

    def total_price_display(self, obj):
        return f"₹{obj.total_price()}"
    total_price_display.short_description = 'Total Price'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'item_total_price')
    search_fields = ('product__name', 'cart__user__username')
    list_filter = ('cart',)

    def item_total_price(self, obj):
        return f"₹{obj.product.price * obj.quantity}"
    item_total_price.short_description = 'Total Price'
