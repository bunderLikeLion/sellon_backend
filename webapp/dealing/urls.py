from django.urls import path
from rest_framework.routers import DefaultRouter

from dealing.views import DealingViewSet, DealingCompleteAPIView, DealingEvaluationView

from dealing.views import CountCompletedAPIView

router = DefaultRouter()
router.register('', DealingViewSet, basename='dealing')
router.register('evaluation', DealingEvaluationView, basename='evaluation')


urlpatterns = [
    path('today_completed_count/', CountCompletedAPIView.as_view()),
    path('<int:pk>/complete/', DealingCompleteAPIView.as_view())
]

urlpatterns += router.urls
