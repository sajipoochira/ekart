from django.shortcuts import render
from pathlib import Path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializer import ProductSerializer
from products.models import Products

# Create your views here.

def index (request):
    return render (request, 'index.html')
@api_view(['GET','POST'])
def products (request):
    if request.method == 'GET':
        objproducts = Products.objects.all()
        serializer = ProductSerializer(objproducts, many = True)
        return Response(serializer.data) 
    
    if request.method == 'POST':
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 