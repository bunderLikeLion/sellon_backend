from django.db.models import Q
from django.core.exceptions import ValidationError, PermissionDenied

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from rest_framework import mixins
from rest_framework.filters import OrderingFilter

from config.viewsets import BaseViewSet
from message.models import Message
from message.serializers import MessageSerializer


@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description='메세지를 생성합니다.'
))
@method_decorator(name='list', decorator=swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            'dealing_id',
            openapi.IN_QUERY,
            description='dealing_id',
            type=openapi.TYPE_INTEGER,
            required=True,
        )
    ],
    operation_description='메세지 목록을 반환합니다.'
))
class MessageViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, BaseViewSet):
    # NOTE: image는 일단 안하는걸로 했음.
    # NOTE: message 수정 / 삭제 / 상세는 지원하지 않는다.
    serializer_class = MessageSerializer
    filter_backends = [OrderingFilter]
    pagination_class = None
    ordering_fields = [
        'created_at',
        'updated_at',
    ]
    ordering = [
        '-updated_at',
    ]

    def get_queryset(self):
        dealing_id = self.request.query_params.get('dealing_id')

        if dealing_id is None:
            return Message.objects.none()

        if self.is_anonymous_user:
            return Message.objects.none()

        return Message.objects.filter(
            Q(dealing__id=dealing_id) & (
                Q(dealing__product__user=self.current_user) | Q(dealing__product_group__user=self.current_user)
            )
        )

    def perform_create(self, serializer):
        product = serializer.validated_data['dealing'].product
        product_group = serializer.validated_data['dealing'].product_group

        if product is None:
            raise ValidationError({'product': '상품이 없습니다.'})

        if product_group is None:
            raise ValidationError({'product_group': '상품 그룹이 없습니다.'})

        if product.user == self.current_user:
            receiver = product_group.user
        elif product_group.user == self.current_user:
            receiver = product.user
        else:
            raise PermissionDenied()

        return serializer.save(
            sender=self.current_user,
            receiver=receiver
        )
