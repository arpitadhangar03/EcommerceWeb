from django.db import models

class Product(models.Model):
    CATEGORY_CHOICE = [ 
        ('men','Men'),
        ('women','Women'),
        ('kids','Kids'),
    ]
    SUBCATEGORY_CHOICE = [
        ('tshirts', 'T-Shirts'),
        ('shirts', 'Shirts'),
        ('bottom', 'Bottom Wear'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
        
        ('tops_w', 'Tops'),
        ('bottom_w', 'Bottom Wear'),
        ('shirts_w', 'Shirts'),
        ('shoes_w', 'Shoes'),
        ('accessories_w', 'Accessories'),
         ]
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category =models.CharField(max_length=20,choices=CATEGORY_CHOICE)
    sub_category = models.CharField(max_length=20, choices=SUBCATEGORY_CHOICE, default='tshirts')
    image = models.URLField(max_length=300)

    def __str__(self):
        return f"{self.name} ({self.category}-{self.sub_category})"


