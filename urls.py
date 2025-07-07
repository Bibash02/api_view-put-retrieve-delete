from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('category', CategoryViewSets)
router.register('food', FoodViewSets)

urlpatterns = [
    # path("category/", CategoryViewSets.as_view({'get': 'list', 'post': 'create', 'delete':'destroy'}))
    # path('category', category),
    # path('category_detail/<pk>', category_detail),

] + router.urls
