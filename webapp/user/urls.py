from django.urls import path, include

from .views import DestroyUserAPIView, RetrieveUserAPIView, UserEvaluationViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('evaluation', UserEvaluationViewSet)

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('user/destroy/', DestroyUserAPIView.as_view(), name='destroy'),
    path('user/<int:pk>', RetrieveUserAPIView.as_view(), name='retrieve'),
]

urlpatterns += router.urls
