from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
from app.core.security import decode_access_token
from app.models.enums import Role

bearer = HTTPBearer()


def require_role(*roles: Role):
    def guard(creds: HTTPAuthorizationCredentials = Security(bearer)) -> dict:
        try:
            payload = decode_access_token(creds.credentials)
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

        if payload.get("role") not in [r.value for r in roles]:
            raise HTTPException(status_code=403, detail="Forbidden")

        return payload

    return guard


def get_current_user(creds: HTTPAuthorizationCredentials = Security(bearer)) -> dict:
    try:
        return decode_access_token(creds.credentials)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
