from django.urls import path, include


urlpatterns = [
    
    path('', include('products.urls')),
    path('', include('orders.urls'))
]
