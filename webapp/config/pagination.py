from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'per_page'
    max_page_size = 30
    # 임시 설정

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'current_page': self.page.number,
            'per_page': self.page_size,
            'total_pages': self.page.paginator.num_pages,
            'results': data,
        })
