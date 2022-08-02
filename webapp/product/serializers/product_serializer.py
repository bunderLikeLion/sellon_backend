from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from config.serializers import IntegerChoiceField
from file_manager.serializers import ImageSerializer
from product.models import Product, ProductCategory
from user.serializers import UserAbstractSerializer
from .product_category_serializer import ProductCategorySerializer


class ProductSerializer(WritableNestedModelSerializer):
    user = UserAbstractSerializer(read_only=True)
    thumbnail = ImageSerializer(
        error_messages={
            'required': '썸네일을 첨부해주세요.',
            'empty': '썸네일을 첨부해주세요.',
        }
    )
    product_category = ProductCategorySerializer(read_only=True)
    product_category_id = serializers.PrimaryKeyRelatedField(
        source='product_category',
        queryset=ProductCategory.objects.all(),
        write_only=True,
    )
    quality = IntegerChoiceField(choices=Product.QUALITY_CHOICES)
    status = IntegerChoiceField(choices=Product.STATUS_CHOICES)

    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'user',
            'thumbnail',
            'images',
            'product_category',
            'product_category_id',
            'name',
            'description',
            'quantity',
            'quality',
            'status',
            'abstract',
            'dealing_at',
            'dealed_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'status',
            'product_category',
            'dealing_at',
            'dealed_at',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'name': {
                'error_messages': {
                    'required': '상품명을 입력해주세요.',
                    'blank': '상품명을 입력해주세요.',
                }
            },
        }
