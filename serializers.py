from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        
    def save(self, **kwargs):
       # return super().save(**kwargs)
        validated_data = self.validated_data
    # def create(self, validated_data):
        total_number = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        if total_number > 0:
            raise serializers.ValidationError("Category already exists.")
        category = self.Meta.model(**validated_data)
        category.save()
        return category
    
class FoodSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = 'category'
    )

    class Meta:
        model = Food
        fields = ["name", "description", "price_with_tax", "price", "category_id", "category"]

    def get_price_with_tax(self, food:Food):
        return food.price * 1.03 + food.price 