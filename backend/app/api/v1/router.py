from fastapi import APIRouter

from app.api.v1.cameras import router as cameras_router
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.violations import router as violations_router
from app.api.v1.workers import router as workers_router


api_router = APIRouter()


api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(cameras_router)
api_router.include_router(violations_router)
api_router.include_router(workers_router)
