from drf_writable_nested.serializers import WritableNestedModelSerializer

from product.models import Product
from user.serializers import UserAbstractSerializer
from file_manager.serializers import ImageSerializer


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
