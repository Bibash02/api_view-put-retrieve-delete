from django.shortcuts import render
from rest_framework.response import Response    
from rest_framework.decorators import api_view
from .models import *
from .serializers import CategorySerializer
from rest_framework import status
from rest_framework.validators import ValidationError

# Create your views here.
# def home(request):
#     return Response("Hi")

# @api_view(['GET'])
# def getData(request):
#     person = {'name': 'Bibash', 'age':20}
#     return Response(person)

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail: New category created."}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def category_detail(request, pk):
    if request.method == "GET":
        try:
            category = Category.objects.get(pk = pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except:
            return Response({"detail: category not found."}, status=status.HTTP_404_NOT_FOUND)
        if category == None:
            return ValidationError({"detail: category not found."}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "DELETE":
        category == Category.objects.get(pk = pk)
        orderitem = OrderItem.objects.filter(food__category = category).count()
        if orderitem > 0:
            return Response({"detail: This category exist in the order. can not delete the category"})
        category.delete()
        return Response({"detail: Category deleted."}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
                        "detail: Category updated."
                         "data": serializer.data
                        }, status=status.HTTP_200_OK)
