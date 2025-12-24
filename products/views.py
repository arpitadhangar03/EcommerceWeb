import requests
from django.shortcuts import render
from .models import Product
from django.db.models import Q
from .forms import ProductFilterForm
def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {"products": products})

def Women(request):
    products = Product.objects.filter(category="women") 
    return render(request, 'products/Women.html', {"products": products})

def Mens(request):
    products = Product.objects.filter(category="men") 
    return render(request, 'products/Mens.html', {"products": products})

def Kids(request):
    products = Product.objects.filter(category="kids") 
    return render(request, 'products/Kids.html', {"products": products})

def category_page(request, category):
    subcategories = Product.SUBCATEGORY_CHOICE
    return render(request, "products/category_page.html", {
        "category": category,
        "subcategories": subcategories
    })

def subcategory_page(request, category, subcategory):
    # Step 1: Try fetching from DB
    products = Product.objects.filter(category=category, sub_category=subcategory)

    # API category mapping (for fallback)
    api_category_map = {
        "tshirts": "men's clothing",
        "shirts": "men's clothing",
        "bottom": "men's clothing",
        "shoes": "men's shoes",
        "accessories": "jewelery",   # fakestore api men accessories jewelry me milta hai

        "tops_w": "women's clothing",
        "bottom_w": "women's clothing",
        "shirts_w": "women's clothing",
        "shoes_w": "women's shoes",
        "accessories_w": "jewelery"
    }

    # Step 2: API fallback if DB empty
    if not products.exists():
        try:
            api_category = api_category_map.get(subcategory, subcategory)
            api_url = f"https://fakestoreapi.com/products/category/{api_category}"
            response = requests.get(api_url, timeout=5)

            if response.status_code == 200:
                products = response.json()  # fakestore api list deta hai
            else:
                products = []
        except Exception as e:
            print("API Error:", e)
            products = []

    # ✅ get readable label from choices
    subcategory_label = dict(Product.SUBCATEGORY_CHOICE).get(subcategory, subcategory)

    return render(request, "products/subcategory_page.html", {
        "category": category,
        "subcategory": subcategory,
        "subcategory_label": subcategory_label,
        "products": products
    })
def search_results(request):
    query = request.GET.get('q')
    form = ProductFilterForm(request.GET)
    products = Product.objects.all()
    if form.is_valid():
        cd = form.cleaned_data
        if cd.get('query'):
           products = Product.objects.filter(
                Q(name__icontains=cd['query']) |
                Q(category__icontains=cd['query']) |
                Q(sub_category__icontains=cd['query'])
        )
        if cd['category']:
            products = products.filter(category=cd['category'])
        if cd['price']:
            price = cd['price']
            if price == '0-500':
                products = products.filter(price__lte=500)
            elif price == '500-1000':
                products = products.filter(price__gte=500, price__lte=1000)
            elif price == '1000-2000':
                products = products.filter(price__gte=1000, price__lte=2000)
            elif price == '2000-':
                products = products.filter(price__gte=2000)
    return render(request, 'products/search_results.html', {'products': products, 'form': form, 'query': cd.get('query', ''),
 })