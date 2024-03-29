from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from dealing.models import Dealing


class CountCompletedAPIView(APIView):

    def get(self, request):
        """
        오늘 성사된 거래 개수를 반환합니다.
        """
        count = Dealing.objects.filter(completed_at__day=timezone.now().day).count()
        return Response({'count': count})
