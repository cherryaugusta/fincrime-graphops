from __future__ import annotations

import time
from dataclasses import asdict, dataclass
from typing import Any, Dict

import redis
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError
from rest_framework.response import Response
from rest_framework.views import APIView


@dataclass(frozen=True)
class DependencyStatus:
    ok: bool
    latency_ms: int
    detail: str


class HealthCheckView(APIView):
    authentication_classes: list = []
    permission_classes: list = []

    def get(self, request):
        deps: Dict[str, Any] = {}
        overall_ok = True

        db_start = time.perf_counter()
        try:
            conn = connections["default"]
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1;")
                cursor.fetchone()
            db_ok = True
            db_detail = "ok"
        except OperationalError as e:
            db_ok = False
            db_detail = f"db_error:{type(e).__name__}"
        db_latency = int((time.perf_counter() - db_start) * 1000)
        deps["database"] = asdict(
            DependencyStatus(
                ok=db_ok,
                latency_ms=db_latency,
                detail=db_detail,
            )
        )
        overall_ok = overall_ok and db_ok

        r_start = time.perf_counter()
        try:
            r = redis.Redis.from_url(
                settings.REDIS_URL,
                socket_connect_timeout=1,
                socket_timeout=1,
                retry_on_timeout=False,
            )
            pong = r.ping()
            redis_ok = bool(pong)
            redis_detail = "ok" if redis_ok else "redis_ping_failed"
        except Exception as e:
            redis_ok = False
            redis_detail = f"redis_error:{type(e).__name__}"
        redis_latency = int((time.perf_counter() - r_start) * 1000)
        deps["redis"] = asdict(
            DependencyStatus(
                ok=redis_ok,
                latency_ms=redis_latency,
                detail=redis_detail,
            )
        )
        overall_ok = overall_ok and redis_ok

        body = {
            "service": "fincrime-graphops-api",
            "ok": overall_ok,
            "dependencies": deps,
            "correlation_id": getattr(request, "correlation_id", None),
        }
        return Response(body, status=200 if overall_ok else 503)
