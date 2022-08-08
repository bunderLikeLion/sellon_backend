from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from dealing.models import Dealing, DealingEvaluation
from dealing.permissions import IsEvaluationEditable
from dealing.serializers.dealing_evaluation_serializer import UserEvaluationSerializer


class DealingEvaluationView(CreateModelMixin, UpdateModelMixin, GenericViewSet, RetrieveAPIView):
    queryset = DealingEvaluation.objects.all()
    serializer_class = UserEvaluationSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsEvaluationEditable,
    ]

    lookup_field = 'dealing'

    def perform_create(self, serializer):

        dealing = Dealing.objects.select_related(
            'product', 'product_group',
            'product_group__user', 'product__user') \
            .get(id=self.request.data['dealing_id'])
        owner = dealing.product.user
        client = dealing.product_group.user

        if self.request.user != owner:
            instance = serializer.save(
                evaluator=self.request.user,
                evaluated_user=owner,
            )
        else:
            instance = serializer.save(
                evaluator=self.request.user,
                evaluated_user=client,
            )

        return instance
