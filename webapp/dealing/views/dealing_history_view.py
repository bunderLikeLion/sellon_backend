from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from dealing.models import Dealing
from dealing.serializers import DealingSerializer


class DealingHistoryListAPIView(ListAPIView):
    serializer_class = DealingSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Dealing.objects.all()\
            .filter(product_group__user=self.request.user, completed_at__isnull=False)

