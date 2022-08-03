from rest_framework.generics import ListAPIView

from product.models import ProductCategory
from product.serializers import ProductCategorySerializer


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        """
        상품 카테고리 목록을 반환합니다.
        """
        return self.list(request, *args, **kwargs)
