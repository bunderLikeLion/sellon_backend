from django.urls import path, include

from .views import DestroyUserAPIView, RetrieveUserAPIView, DealingsCountAPIView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('user/destroy/', DestroyUserAPIView.as_view(), name='destroy'),
    path('user/<int:pk>', RetrieveUserAPIView.as_view(), name='retrieve'),
    path('user/<int:pk>/dealings_count/', DealingsCountAPIView.as_view()),
]
