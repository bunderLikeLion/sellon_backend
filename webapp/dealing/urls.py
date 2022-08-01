from django.urls import path

from dealing.views import CountCompletedAPIView

urlpatterns = [
    path('today_completed_count/', CountCompletedAPIView.as_view())
]
