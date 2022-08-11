from auction.views import (
    AuctionViewSet,
    InterestedAuctionViewSet,
    MostPopularAPIView,
    AddProductAPIView,
    RemoveProductAPIView
)
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('interested', InterestedAuctionViewSet, basename='interested_auction')
router.register('', AuctionViewSet, basename='auction')

urlpatterns = [
    path('popular/', MostPopularAPIView.as_view()),
    path('<int:auction_id>/add_product/', AddProductAPIView.as_view()),
    path('<int:auction_id>/remove_product/', RemoveProductAPIView.as_view()),
]

urlpatterns += router.urls
