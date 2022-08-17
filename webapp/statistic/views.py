from django.contrib.auth import get_user_model
from django.db.models import Q, Count
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from user.serializers import UserAbstractSerializer, UserDealingRankingSerializer
from dealing.models import Dealing
from auction.models import Auction
from django.utils import timezone

User = get_user_model()


class UserDealingStatisticSerailizer(serializers.Serializer):
    user = UserAbstractSerializer(read_only=True)
    count = serializers.IntegerField()

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
        print(request)

        return Response({
            'user': UserAbstractSerializer(user, context={'request': request}).data,
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
        print(request)
        return Response({
            'user': UserAbstractSerializer(user, context={'request': request}).data,
            'count': most_product_group_dealing_statitic['count']
        })


class MonthlyChampionAPIView(RetrieveAPIView):
    serializer_class = UserDealingStatisticSerailizer

    def get(self, request):
        """
        이번 달 가장 많은 참여자를 보유한 경매에서 낙찰된 사람을 반환합니다.
        """
        try:
            max_participant_count_compeleted_auction = Auction.objects.filter(
                Q(dealing__completed_at__month=timezone.now().month) & Q(dealing__completed_at__isnull=False)
            ).order_by('-product_groups_count')[0]

            user = max_participant_count_compeleted_auction.dealing.product_group.user

            return Response({
                'user': UserAbstractSerializer(user, context={'request': request}).data,
                'count': max_participant_count_compeleted_auction.product_groups_count

            })
        except Exception as e:
            return Response({'error': str(e)}, status=404)


class DealingRankingAPIView(ListAPIView):

    serializer_class = UserDealingRankingSerializer

    def get_queryset(self):
        return User.objects.all().order_by('-completed_dealings_count')
