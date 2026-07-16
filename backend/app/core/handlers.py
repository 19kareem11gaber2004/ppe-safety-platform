from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AppException
from app.schemas.api_response import ErrorResponse


async def app_exception_handler(
    request: Request,
    exc: AppException,
):

    response = ErrorResponse(
        message=exc.message
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump(mode="json"),
    )
