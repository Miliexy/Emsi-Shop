from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Category, Product




class all_products(View):
    def get(self,request):
        products = Product.products.all()
        return render(request, 'store/home.html', {'products': products})


class product(View):
    def get(self,request,slug):
        product = get_object_or_404(Product,slug=slug, in_stock=True)
        return render(request, 'store/products/single.html',{'product': product})

class category(View):
    def get(self,request,slug):
        category = get_object_or_404(Category,slug=slug)
        products = Product.objects.filter(category=category)
        return render(request, 'store/products/category.html', {'category': category, 'products': products})



