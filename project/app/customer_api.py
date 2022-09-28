from typing import List

import fastapi
from .models.tortoise import Customer

router = fastapi.APIRouter()

MESSAGE_CUSTOMER_NOT_FOUND = "Customer not found"
MESSAGE_DOCUMENT_IS_REQUIRED = "Document is required"


@router.get("/customers")
async def get_customers_api() -> List[Customer]:
    return await Customer.all()


@router.get("/customer/{document}")
async def get_customer_api(document: str) -> Customer:
    if not document.isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if (customer := await Customer.filter(document=document).first()) is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=MESSAGE_CUSTOMER_NOT_FOUND)

    return customer


@router.post("/customer")
async def create_customer_api(customer: dict) -> Customer:
    if customer.get("document") is None or not customer.get(
            "document").isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if await Customer.filter(document=customer["document"]).exists() is not None:
        raise fastapi.HTTPException(
            status_code=409,
            detail="Customer already exists")

    return await Customer.create(**customer)


@router.put("/customer/{document}")
async def update_customer_api(document: str, customer: dict) -> Customer:
    if not document.isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if await Customer.filter(document=customer["document"]).exists() is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=MESSAGE_CUSTOMER_NOT_FOUND)

    updated_id = await Customer.filter(document=document).update(**customer)
    if updated_id == 0:
        raise fastapi.HTTPException(
            status_code=500,
            detail="Customer not updated")

    return await Customer.filter(document=document).first()


@router.delete("/customer/{document}")
async def delete_customer_api(document: str) -> dict:
    if not document.isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if (customer_data := await Customer.filter(document=document).first()) is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=MESSAGE_CUSTOMER_NOT_FOUND)

    await Customer.delete(customer_data)
    return {"message": "Customer deleted!"}
