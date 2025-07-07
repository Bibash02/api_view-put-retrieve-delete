from django.shortcuts import render
from rest_framework.response import Response    
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.validators import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters import rest_framework as filter
from .filters import FoodFilter

class CategoryViewSets(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request, pk):
        category = Category.objects.get(pk = pk)
        orderitem = OrderItem.objects.filter(food__category = category).count()
        if orderitem > 0:
            return Response({'detail: this category exists in the order. Can not delete the category.'})
        category.delete()
        return Response({'details: Category deleted.'}, status=status.HTTP_204_NO_CONTENT)

class FoodViewSets(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filter.DjangoFilterBackend]
    search_fields = ['name', 'description']
    #filterset_fields = ['name']
    filterset_class = FoodFilter

# class category(ListAPIView):
#     queryset = Category.objects
#     serializer_class = CategorySerializer


# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == "GET":
#         category = Category.objects.all()
#         serializer = CategorySerializer(category,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"detail: New category created."}, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'DELETE', 'PUT'])
# def category_detail(request, pk):
#     if request.method == "GET":
#         try:
#             category = Category.objects.get(pk = pk)
#             serializer = CategorySerializer(category)
#             return Response(serializer.data)
#         except:
#             return Response({"detail: category not found."}, status=status.HTTP_404_NOT_FOUND)
#         if category == None:
#             return ValidationError({"detail: category not found."}, status=status.HTTP_404_NOT_FOUND)
#     elif request.method == "DELETE":
#         category == Category.objects.get(pk = pk)
#         orderitem = OrderItem.objects.filter(food__category = category).count()
#         if orderitem > 0:
#             return Response({"detail: This category exist in the order. can not delete the category"})
#         category.delete()
#         return Response({"detail: Category deleted."}, status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "PUT":
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#                         "detail: Category updated."
#                          "data": serializer.data
#                         }, status=status.HTTP_200_OK)
