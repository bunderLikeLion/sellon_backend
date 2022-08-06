from django.urls import path
from rest_framework.routers import DefaultRouter

from dealing.views import DealingViewSet, DealingCompleteAPIView

from dealing.views import CountCompletedAPIView

router = DefaultRouter()
router.register('', DealingViewSet, basename='dealing')

urlpatterns = [
    path('today_completed_count/', CountCompletedAPIView.as_view()),
    path('<int:pk>/complete/', DealingCompleteAPIView.as_view())
]

urlpatterns += router.urls
