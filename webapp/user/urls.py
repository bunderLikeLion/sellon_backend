from django.urls import path, include

from .views import DestroyUser, RetrieveUser

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('user/destroy/', DestroyUser.as_view(), name='destroy'),
    path('user/<int:pk>', RetrieveUser.as_view(), name='retrieve'),
]
