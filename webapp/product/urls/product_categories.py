from django.urls import path
from product.views.product_categories_view_set import ProductCategoryListAPIView, ProductCategoryRetrieveAPIView


urlpatterns = [
    path('', ProductCategoryListAPIView.as_view(), name='category-list'),
    path('<int:pk>', ProductCategoryRetrieveAPIView.as_view(), name='category-retrieve'),
]
