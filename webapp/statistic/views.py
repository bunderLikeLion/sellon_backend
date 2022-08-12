from django.contrib.auth import get_user_model
from django.db.models import Q, Count
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from user.serializers.user_abstract_serializer import UserAbstractSerializer
from dealing.models import Dealing
from django.utils import timezone

User = get_user_model()


class UserDealingStatisticSerailizer(serializers.Serializer):
    user = UserAbstractSerializer(read_only=True)
    dealing_count = serializers.IntegerField()

    class Meta:
        fields = [
            'user',
            'count',
        ]


class MostProductDealingOfMonth(RetrieveAPIView):
    serializer_class = UserDealingStatisticSerailizer

    def get(self, request):
        """
        한달간 직접 경매를 올려 거래한 수가 가장 많은 유저와 거래횟수를 반환합니다.
        """
        dealing_product_statistics = Dealing.objects.filter(
            Q(completed_at__month=timezone.now().month) & Q(completed_at__isnull=False)
        ).values('product__user').annotate(count=Count('product__user')).order_by('-count')

        if len(dealing_product_statistics) == 0:
            raise Http404()

        most_dealing_product_statitic = dealing_product_statistics[0]

        user = get_object_or_404(User, pk=most_dealing_product_statitic['product__user'])

        return Response({
            'user': UserAbstractSerializer(user).data,
            'count': most_dealing_product_statitic['count']
        })


class MostProductGroupDealingOfMonth(RetrieveAPIView):
    serializer_class = UserDealingStatisticSerailizer

    def get(self, request):
        """
        한달간 가장 많이 거래한 유저와 거래횟수를 반환합니다.
        """
        most_product_group_dealing_statitics = Dealing.objects.filter(
            Q(completed_at__month=timezone.now().month) & Q(completed_at__isnull=False)
        ).values('product_group__user').annotate(count=Count('product_group__user')).order_by('-count')

        if len(most_product_group_dealing_statitics) == 0:
            return Response({
                'user': None,
                'count': None,
            })

        most_product_group_dealing_statitic = most_product_group_dealing_statitics[0]

        user = get_object_or_404(User, pk=most_product_group_dealing_statitic['product_group__user'])

        return Response({
            'user': UserAbstractSerializer(user).data,
            'count': most_product_group_dealing_statitic['count']
        })
