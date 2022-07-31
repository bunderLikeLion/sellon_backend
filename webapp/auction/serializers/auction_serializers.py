from rest_framework.serializers import ModelSerializer

from auction.models import Auction
from product.serializers.product_abstract_serializer import ProductAbstractSerializer
from user.serializers import UserAbstractSerializer


class AuctionSerializer(ModelSerializer):
    owner = UserAbstractSerializer(read_only=True)
    product = ProductAbstractSerializer(read_only=True)

    class Meta:
        model = Auction
        fields = [
            'id',
            'owner',
            'product',
            'description',
            'start_at',
            'end_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'name': {
                'error_messages': {}
            },
        }
