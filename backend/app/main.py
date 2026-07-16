from fastapi import FastAPI
from app.core.exceptions import AppException
from app.core.handlers import app_exception_handler
from app.core.logging import setup_logging
from app.core.middleware import RequestLoggingMiddleware
from app.schemas.api_response import ApiResponse
from app.api.v1.router import api_router

setup_logging()
app = FastAPI(
    title="PPE Safety Platform API",
    version="0.1.0",
)

app.add_middleware(
    RequestLoggingMiddleware
)
app.add_exception_handler(
    AppException,
    app_exception_handler,
)
app.include_router(
    api_router,
    prefix="/api/v1",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to PPE Safety Platform API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get(
    "/health",
    response_model=ApiResponse[dict],
)
def health():
    return ApiResponse(
        message="Service is healthy",
        data={
            "status": "ok",
        },
    )