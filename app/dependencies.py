from fastapi import Header, HTTPException
from typing_extensions import Annotated
from sqlalchemy.orm import scoped_session
from app.configs.sqlalchemy import session_local


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")


# Dependency
def get_db_connection():
    db = scoped_session(session_local)
    try:
        yield db
    finally:
        db.close()
