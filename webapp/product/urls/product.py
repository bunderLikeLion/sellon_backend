from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet, basename='Product')

urlpatterns = []

urlpatterns += router.urls
