from django.urls import path
from django.contrib import admin
from products import views
# app_name ='products'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search'),
    path('Women/', views.Women, name='Women'),
    path('Mens/', views.Mens, name='Mens'),
    path('Kids/', views.Kids, name='Kids'),
    path('<str:category>/<str:subcategory>/', views.subcategory_page, name='subcategory_page'),
    path('<str:category>/', views.category_page, name='category_page'),
]
