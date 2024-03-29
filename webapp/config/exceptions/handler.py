from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.forms import ValidationError
from django.http import Http404

from rest_framework import exceptions

from http import HTTPStatus
from typing import Any

from rest_framework.views import Response, set_rollback


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
    if isinstance(exc, ValidationError):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait
        data = exc.message_dict
        return Response(data, status=422, headers=headers)
    if isinstance(exc, IntegrityError):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait
        data = str(exc.args)

        # FIXME: 나중에 unique constraints 관련 오류 핸들링 방식을 찾아보기

        if 'unique_product_group_in_auction_by_user' in data:
            data = {'auction': ['이미 참가하고 있는 경매장입니다']}
        if 'unique_interested_auction_by_user' in data:
            data = {'auction': ['이미 관심 설정한 경매장입니다']}

        if 'user_evaluations.evaluated_user_id, user_evaluations.dealing_id' in data:
            data = {'evaluation': ['이미 평가를 완료한 항목입니다. 수정 요청만 허용됩니다.']}

        return Response(data, status=422, headers=headers)

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    return None


def api_exception_handler(exc: Exception, context: dict[str, Any]) -> Response:
    """Custom API exception handler."""

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        # Using the description's of the HTTPStatus class as error message.
        http_code_to_message = {v.value: v.description for v in HTTPStatus}

        error_payload = {
            'error': {
                'status_code': 0,
                'message': '',
                'details': [],
            }
        }
        error = error_payload['error']
        status_code = response.status_code

        error['status_code'] = status_code
        error['message'] = http_code_to_message[status_code]
        error['details'] = response.data
        response.data = error_payload
    return response
