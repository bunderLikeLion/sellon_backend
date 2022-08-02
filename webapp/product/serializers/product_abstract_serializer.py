from rest_framework import serializers

from config.serializers import IntegerChoiceField
from file_manager.serializers import ImageSerializer
from product.models import Product


class ProductAbstractSerializer(serializers.ModelSerializer):
    thumbnail = ImageSerializer(
        error_messages={
            'required': '썸네일을 첨부해주세요.',
            'blank': '썸네일을 첨부해주세요.',
            'empty': '썸네일을 첨부해주세요.',
        }
    )

    quality = IntegerChoiceField(choices=Product.QUALITY_CHOICES)
    status = IntegerChoiceField(choices=Product.STATUS_CHOICES, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'user',
            'thumbnail',
            'product_category',
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
