from __future__ import annotations

import uuid
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class CorrelationIdMiddleware(MiddlewareMixin):
    RESPONSE_HEADER = "X-Correlation-ID"

    def process_request(self, request):
        header_key = getattr(settings, "CORRELATION_ID_HEADER", "HTTP_X_CORRELATION_ID")
        inbound = request.META.get(header_key, "")
        correlation_id = inbound.strip() if inbound else str(uuid.uuid4())
        request.correlation_id = correlation_id

    def process_response(self, request, response):
        correlation_id = getattr(request, "correlation_id", None)
        if correlation_id:
            response[self.RESPONSE_HEADER] = correlation_id
        return response
