from django.urls import path
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, ProductCategoryListAPIView

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('category/', ProductCategoryListAPIView.as_view(), name='category-list')
]

urlpatterns += router.urls
