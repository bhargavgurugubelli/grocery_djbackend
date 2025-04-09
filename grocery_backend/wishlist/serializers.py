from rest_framework import serializers
from . import models


class WishListSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='product.id')
    title = serializers.ReadOnlyField(source='product.title')
    description = serializers.ReadOnlyField(source='product.description')
   
    price = serializers.ReadOnlyField(source='product.price')
    ratings = serializers.ReadOnlyField(source='product.ratings')
    category = serializers.ReadOnlyField(source='product.category.id')
   
    imageUrls = serializers.ReadOnlyField(source='product.imageUrls')
    created_at = serializers.ReadOnlyField(source='product.created_at')

    class Meta:
        model = models.WishList
        fields = ['id', 'title','description','price',  'ratings', 'category', 'imageUrls', 'created_at' ]