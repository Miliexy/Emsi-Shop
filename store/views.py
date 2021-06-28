from django.shortcuts import render
from django.views import View


from .models import Category,Product

class all_products(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request, 'store/home.html', {'products': products})


