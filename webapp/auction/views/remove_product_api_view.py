from django.db import transaction
from django.http import QueryDict
from rest_framework.generics import GenericAPIView
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.settings import api_settings

from product.models.product_group import ProductGroup, Product
from product.serializers import ProductGroupSerializer


class RemoveProductSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        source='product',
        write_only=True,
        queryset=Product.objects.all(),
    )

    class Meta:
        model = ProductGroup
        fields = [
            'product_id',
        ]


class RemoveProductAPIView(GenericAPIView):
    serializer_class = RemoveProductSerializer

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    @transaction.atomic
    def post(self, request, auction_id, *args, **kwargs):
        product_id = request.data.get('product_id') or None
        # TODO: product 없는 경우 에러 처리
        # TODO: 익명 유저 에러처리

        product_group, _created = ProductGroup.objects.get_or_create(
            auction_id=auction_id,
            user=request.user,
        )
        product_ids = set(list(map(str, product_group.products.values_list('id', flat=True))))
        product_ids.discard(product_id)

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
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
