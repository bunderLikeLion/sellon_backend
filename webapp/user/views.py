from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserAbstractSerializer
from .models import User
from dealing.models import Dealing


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
        product_count = Dealing.objects.filter(product__user=request.user).count()
        product_group_count = Dealing.objects.filter(product_group__user=request.user).count()
        count = product_count + product_group_count
        return Response({'count': count})
