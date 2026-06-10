from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.monitor import router as monitor_router
from app.api.v1.auth import router as auth_router


def get_application():
    _app = FastAPI()

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(router=monitor_router, prefix="/api/v1")
    _app.include_router(router=auth_router, prefix="/api/v1")

    return _app

app = get_application()