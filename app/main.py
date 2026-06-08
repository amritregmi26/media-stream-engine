from fastapi import FastAPI
from app.api.v1.monitor import router as monitor_router
from app.api.v1.auth import router as auth_router
from app.database import Base, engine


def get_application():
    _app = FastAPI()

    _app.include_router(router=monitor_router, prefix="/api/v1")
    _app.include_router(router=auth_router, prefix="/api/v1")

    return _app

app = get_application()