from rest_framework.routers import DefaultRouter
from product.views import ProductGroupViewSet

router = DefaultRouter()
router.register('', ProductGroupViewSet)

urlpatterns = []

urlpatterns += router.urls
