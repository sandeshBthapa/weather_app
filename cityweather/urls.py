from django.urls import path
from .views import index,delete_city

urlpatterns = [
    path('', index, name='city'),
    path('delete/<city_name>', delete_city, name='delete_city')
]
