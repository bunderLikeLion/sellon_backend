from django.urls import path, include

from .views import DestroyUserAPIView, RetrieveUserAPIView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('user/destroy/', DestroyUserAPIView.as_view(), name='destroy'),
    path('user/<int:pk>', RetrieveUserAPIView.as_view(), name='retrieve'),
]
