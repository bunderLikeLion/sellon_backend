from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method

from auction.models import Auction
from config.serializers import IntegerChoiceField
from product.models import Product
from product.serializers.product_abstract_serializer import ProductAbstractSerializer
from user.serializers import UserAbstractSerializer


class AuctionSerializer(ModelSerializer):
    owner = UserAbstractSerializer(read_only=True)
    product = ProductAbstractSerializer(read_only=True)

    dealing_type = IntegerChoiceField(choices=Auction.DEALING_TYPES)
    is_interested = serializers.SerializerMethodField(source='is_interested')

    product_id = serializers.PrimaryKeyRelatedField(
        source='product',
        queryset=Product.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Auction
        fields = [
            'id',
            'owner',
            'title',
            'product_id',
            'product',
            'description',
            'end_at',
            'created_at',
            'updated_at',
            'dealing_type',
            'is_interested',
            'product_groups_count',
            'interested_auctions_count'
        ]
        read_only_fields = [
            'start_at',
            'product_groups_count',
            'interested_auctions_count',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'end_at': {
                'required': True,
            }
        }

    @property
    def current_user(self):
        return self.context.get('request').user

    @property
    def is_anonymous_user(self):
        return self.current_user.is_anonymous

    @swagger_serializer_method(serializer_or_field=serializers.BooleanField)
    def get_is_interested(self, auction) -> bool:
        if self.is_anonymous_user:
            return False
        return auction.interested_auctions.filter(user=self.current_user).exists()
