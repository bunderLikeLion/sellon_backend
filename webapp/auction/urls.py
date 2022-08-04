from rest_framework.routers import DefaultRouter
from django.urls import path

from auction.views import AuctionViewSet, InterestedAuctionViewSet, MostPopularAPIView

router = DefaultRouter()
router.register('', AuctionViewSet)
router.register('interested', InterestedAuctionViewSet)

urlpatterns = [
    path('popular/', MostPopularAPIView.as_view())
]

urlpatterns += router.urls
