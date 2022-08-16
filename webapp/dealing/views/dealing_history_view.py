from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from dealing.models import Dealing
from dealing.serializers import DealingSerializer


class DealingHistoryListAPIView(ListAPIView):
    serializer_class = DealingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Dealing.objects \
            .filter(product_group__user=self.request.user, completed_at__isnull=False)
