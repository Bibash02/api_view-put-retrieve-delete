from django.urls import path
from .views import *

urlpatterns = [
    path('category_list', category_list),
    path('category_detail/<pk>', category_detail),

]
