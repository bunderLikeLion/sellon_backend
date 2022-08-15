from django.db import transaction
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from config.serializers import IntegerChoiceField
from file_manager.serializers.image_serializer import ImageSerializer
from file_manager.models import Image, ProductImage
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
    status = IntegerChoiceField(choices=Product.STATUS_CHOICES, read_only=True)

    images = ImageSerializer(many=True, required=False)
    image_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Image.objects.all(),
        write_only=True
    )

    def clear_existing_images(self, instance, remaing_ids):
        for product_image in instance.product_image_items.exclude(image_id__in=remaing_ids):
            product_image.delete()

    @transaction.atomic
    def update(self, instance, validated_data):
        remaining_images = validated_data.pop('image_ids', [])
        images = validated_data.pop('images', [])

        # NOTE: image_ids 가 validation을 거쳐 Image 객체로 나옴.
        remaining_image_ids = [*map(lambda image: image.id, remaining_images)]

        self.clear_existing_images(instance, remaining_image_ids)

        for image_file in images:
            image = Image(file=image_file['file'])
            image.save()
            ProductImage.objects.get_or_create(product=instance, image=image)

        return super().update(instance, validated_data)

    class Meta:
        model = Product
        fields = [
            'id',
            'user',
            'thumbnail',
            'image_ids',
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
