from typing import Annotated
from fastapi import FastAPI, Cookie, File, UploadFile, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer
from .routers.api import user
from app.metadata.general import general_metadata
from app.metadata.tags import tags_metadata

app = FastAPI(openapi_tags=tags_metadata)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app.include_router(user.router)
