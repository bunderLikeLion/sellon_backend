from django.urls import path
from product.views import ProductGroupsListAPIView


urlpatterns = [
    path('my/', ProductGroupsListAPIView.as_view(), name='product-groups')
]
