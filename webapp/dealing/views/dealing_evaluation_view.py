from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from dealing.models import Dealing, DealingEvaluation
from dealing.permissions import IsEvaluationEditable
from dealing.serializers.dealing_evaluation_serializer import DealingEvaluationSerializer


class DealingEvaluationView(CreateModelMixin, UpdateModelMixin, GenericViewSet, RetrieveAPIView):
    queryset = DealingEvaluation.objects.all()
    serializer_class = DealingEvaluationSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsEvaluationEditable,
    ]

    lookup_field = 'dealing'

    def get_object(self):
        queryset = DealingEvaluation.objects.filter(dealing_id=self.kwargs['dealing'], evaluator=self.request.user)

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (self.__class__.__name__, lookup_url_kwarg)

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj

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
