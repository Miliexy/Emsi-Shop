from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products.as_view(), name='all_products')
]

