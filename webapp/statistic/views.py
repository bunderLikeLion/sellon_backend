from django.db.models import Q, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from dealing.models import Dealing
from django.utils import timezone


class MostProductDealingOfMonth(APIView):

    def get(self, request):
        """
        한달간 직접 경매를 올려 거래한 수가 가장 많은 유저와 거래횟수를 반환합니다.
        """
        most_product_dealing = Dealing.objects.filter(
            Q(completed_at__month=timezone.now().month) & Q(completed_at__isnull=False)
        ).values('product__user').annotate(count=Count('product__user')).order_by('-count')[0]
        return Response(most_product_dealing)


class MostProductGroupDealingOfMonth(APIView):

    def get(self, request):
        """
        한달간 가장 많이 거래한 유저와 거래횟수를 반환합니다.
        """
        most_product_group_dealing = Dealing.objects.filter(
            Q(completed_at__month=timezone.now().month) & Q(completed_at__isnull=False)
        ).values('product_group__user').annotate(count=Count('product_group__user')).order_by('-count')[0]
        return Response(most_product_group_dealing)
