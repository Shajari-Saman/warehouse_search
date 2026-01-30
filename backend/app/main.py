# Third Library
from fastapi import FastAPI

from app.api.v1.search import router as search_router

app = FastAPI(title="Product Search API")

app.include_router(search_router, prefix="/api/v1")
