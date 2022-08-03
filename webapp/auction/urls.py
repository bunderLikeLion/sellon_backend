from rest_framework.routers import DefaultRouter
from django.urls import path

from auction.views import AuctionViewSet, MostPopularAPIView

router = DefaultRouter()
router.register('', AuctionViewSet)

urlpatterns = [
    path('popular/', MostPopularAPIView.as_view())
]

urlpatterns += router.urls
