from django.db import transaction
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.settings import api_settings

from auction.models import Auction
from product.models.product_group import ProductGroup, Product
from product.serializers import ProductGroupSerializer


class AllInSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = []


class AllInAPIView(GenericAPIView):
    serializer_class = AllInSerializer

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    @transaction.atomic
    def post(self, request, auction_id, *args, **kwargs):
        auction = get_object_or_404(Auction, pk=auction_id)

        product_group, _created = ProductGroup.objects.get_or_create(
            auction=auction,
            user=request.user,
        )
        already_registered_product_ids = list(map(str, product_group.products.values_list('id', flat=True)))

        hidden_products = Product.objects.filter(user=request.user, status=Product.HIDDEN_STATUS)
        hidden_product_ids = list(map(str, hidden_products.values_list('id', flat=True)))
        product_ids = list(set(already_registered_product_ids + hidden_product_ids))

        if isinstance(request.data, QueryDict):
            request.data._mutable = True
            request.data.setlist('product_ids', product_ids)
            request.data._mutable = False
        else:
            request.data['product_ids'] = product_ids

        serializer = ProductGroupSerializer(
            product_group,
            data=request.data,
            partial=True,
            context=self.get_serializer_context()
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
