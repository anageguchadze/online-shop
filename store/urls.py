from django.urls import path
from .views import add_category, remove_category, select_product, add_product, remove_product

urlpatterns = [
    path('add_category/', add_category, name='add_category'),
    path('remove_category/<int:id>', remove_category, name='remove_category'),
    path('add_product/', add_product, name='add_product'),
    path('remove_product/<int:id>', remove_product, name='remove_product'),
    path('select_product/<int:id>', select_product, name='select_product'),
]