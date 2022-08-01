from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register('', MessageViewSet)

urlpatterns = []

urlpatterns += router.urls
