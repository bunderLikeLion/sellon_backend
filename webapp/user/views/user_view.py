from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from dealing.models import Dealing
from dealing.models.dealing_evaluation import DealingEvaluation
from user.serializers import UserAbstractSerializer
from user.models import User


class DestroyUserAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(username=self.request.user.username)
            return instance
        except User.DoesNotExist:
            content = {'No User Exist': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


class RetrieveUserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAbstractSerializer


class DealingsCountAPIView(APIView):
    def get(self, request, pk):
        """
        유저의 거래 횟수를 반환합니다.
        """
        user = get_object_or_404(User, pk=pk)
        product_count = Dealing.objects.filter(product__user=user).count()
        product_group_count = Dealing.objects.filter(product_group__user=user).count()
        count = product_count + product_group_count
        return Response({'count': count})


class RatingAPIView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        qs = DealingEvaluation.objects.filter(evaluated_user=user).values('rate')
        if qs:
            return Response({'rating': qs})
        else:
            return Response({'rating': 0})
