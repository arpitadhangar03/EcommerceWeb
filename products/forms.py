from django import forms

CATEGORY_CHOICES = [
    ('men', 'Men'),
    ('women', 'Women'),
    ('kids', 'Kids'),
]

PRICE_CHOICES = [
    ('', 'Any Price'),
    ('0-500', 'Under ₹500'),
    ('500-1000', '₹500-₹1000'),
    ('1000-2000', '₹1000-₹2000'),
    ('2000-', 'Above ₹2000'),
]

class ProductFilterForm(forms.Form):
    category = forms.ChoiceField(choices=[('', 'All Categories')] + CATEGORY_CHOICES, required=False)
    price = forms.ChoiceField(choices=PRICE_CHOICES, required=False)
