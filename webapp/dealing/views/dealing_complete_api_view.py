from django.shortcuts import get_object_or_404

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from dealing.models import Dealing


response_schema_dict = {
    '200': openapi.Response(
        description='200',
        examples={
            'application/json': {
                'message': '거래가 종료되었습니다.',
            }
        }
    ),
}


class DealingCompleteAPIView(APIView):
    @swagger_auto_schema(responses=response_schema_dict)
    def post(self, request, pk, *args, **kwargs):
        dealing = get_object_or_404(Dealing, pk=pk)
        dealing.complete()
        return Response({'massaeg': '거래가 종료되었습니다.'})
