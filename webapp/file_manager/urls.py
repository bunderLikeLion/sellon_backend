from django.urls import path
from .views import ImageCreateAPIView

urlpatterns = [
    path('', ImageCreateAPIView.as_view(), name='create'),
]
