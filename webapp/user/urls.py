from django.urls import path, include
from django.views.decorators.http import require_http_methods

from user.views import DestroyUser


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('user/destroy/', require_http_methods(['DELETE'])(DestroyUser.as_view()), name='destroy'),
]
