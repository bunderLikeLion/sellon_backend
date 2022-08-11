from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from config.viewsets import BaseViewSet
from dealing.models import Dealing, DealingEvaluation
from dealing.permissions import IsEvaluationEditable
from dealing.serializers.dealing_evaluation_serializer import DealingEvaluationSerializer


class DealingEvaluationView(CreateModelMixin, UpdateModelMixin, RetrieveAPIView, BaseViewSet):
    serializer_class = DealingEvaluationSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsEvaluationEditable,
    ]

    lookup_field = 'dealing'

    def get_queryset(self):
        return DealingEvaluation.objects.filter(evaluator=self.current_user)

    def perform_create(self, serializer):
        dealing = Dealing.objects.get(id=self.request.data['dealing_id'])
        owner = dealing.product.user
        client = dealing.product_group.user

        if self.current_user == owner:
            instance = serializer.save(
                evaluator=self.current_user,
                evaluated_user=client,
            )
        elif self.current_user == client:
            instance = serializer.save(
                evaluator=self.current_user,
                evaluated_user=owner,
            )
        else:
            return DealingEvaluation()

        return instance
