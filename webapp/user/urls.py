from django.urls import path, include
from webapp.user import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('deleteUser/', views.DeleteUser.as_view(), name='deleteUser'),
]
