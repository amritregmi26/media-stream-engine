from fastapi import APIRouter

router = APIRouter(prefix="/monitor")

@router.get("/health")
async def health():
    return {"message": "API is working fine."}