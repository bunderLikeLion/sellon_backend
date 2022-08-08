from message.views import MessageViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', MessageViewSet, basename='message')

urlpatterns = []

urlpatterns += router.urls
