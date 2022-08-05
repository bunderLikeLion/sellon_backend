"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings


def ping(request):
    return HttpResponse('pong')


schema_view = get_schema_view(
    openapi.Info(
        title='Sellon API',
        default_version='v1',
        description='sellon api',
        contact=openapi.Contact(email='singun11@kookmin.ac.kr'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('ping', ping),
    path('admin/', admin.site.urls),
    path('users/', include('user.urls'), name='users'),
    path('images/', include('file_manager.urls'), name='images'),
    path('products/', include('product.urls.product'), name='products'),
    path('product_categories/', include('product.urls.product_categories'), name='product_categories'),
    path('product_groups/', include('product.urls.product_group'), name='product_groups'),
    path('auctions/', include('auction.urls'), name='auctions'),
    path('dealings/', include('dealing.urls'), name='dealings'),

]

if settings.DEBUG:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
