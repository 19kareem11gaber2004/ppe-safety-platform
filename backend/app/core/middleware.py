import uuid
import time
import logging

from starlette.middleware.base import BaseHTTPMiddleware


logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        request_id = str(uuid.uuid4())

        start_time = time.time()


        response = await call_next(request)


        duration = (
            time.time() - start_time
        )


        logger.info(
            "API Request",
            extra={
                "request_id": request_id,
            },
        )


        response.headers[
            "X-Request-ID"
        ] = request_id


        return response
