from rest_framework.routers import DefaultRouter

from auction.views import AuctionViewSet

router = DefaultRouter()
router.register('', AuctionViewSet)

urlpatterns = []

urlpatterns += router.urls
