from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberPagination(PageNumberPagination):
    page_size = 3
    # 임시 설정

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('current_page', self.page.number),
            ('per_page', self.page_size),
            ('total_pages', self.page.paginator.num_pages),
        ]))
