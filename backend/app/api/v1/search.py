# Third Library
from fastapi import APIRouter, Query

from app.services.product_service import CostCenterService, ProductService

router = APIRouter()
product_service = ProductService()
cost_service = CostCenterService()


@router.get("/search")
def search_products(q: str = Query(..., min_length=1)):
    result = product_service.search(q)
    return {"count": len(result), "items": result.to_dicts()}


@router.get("/cost")
def search_cost_center(q: str = Query(..., min_length=1)):
    result = cost_service.search(q)
    return {"count": len(result), "items": result.to_dicts()}
