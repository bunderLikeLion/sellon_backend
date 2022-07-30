from user.serializers import UserAbstractSerializer
from file_manager.serializers import ImageSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from product.models import Product, ProductCategory


class ProductSerializer(WritableNestedModelSerializer):
    user = UserAbstractSerializer(read_only=True)
    thumbnail = ImageSerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'user',
            'thumbnail',
            'name',
            'description',
            'quantity',
            'quality',
            'abstract',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
        ]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']
