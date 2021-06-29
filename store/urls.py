from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products.as_view(), name='all_products'),
    path('<slug:slug>', views.product.as_view(), name='product'),
    path('search/<slug:slug>/', views.category.as_view(), name='category')
]

