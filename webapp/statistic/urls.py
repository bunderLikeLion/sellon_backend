from statistic.views import MostProductDealingOfMonth, MostProductGroupDealingOfMonth
from django.urls import path


urlpatterns = [
    path('most_product_dealing/', MostProductDealingOfMonth.as_view()),
    path('most_product_group_dealing/', MostProductGroupDealingOfMonth.as_view()),
]
