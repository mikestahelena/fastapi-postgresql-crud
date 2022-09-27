import fastapi
from .customer_service import get_all_customers, get_customer_by_document, create_customer, update_customer, delete_customer

router = fastapi.APIRouter()

MESSAGE_CUSTOMER_NOT_FOUND = "Customer not found"
MESSAGE_DOCUMENT_IS_REQUIRED = "Document is required"


@router.get("/customers")
async def get_customers_api() -> list:
    return await get_all_customers()


@router.get("/customer/{document}")
async def get_customer_api(document: str) -> dict:
    if not document.isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if (customer := await get_customer_by_document(document)) is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=MESSAGE_CUSTOMER_NOT_FOUND)

    return customer


@router.post("/customer")
async def create_customer_api(customer: dict) -> dict:
    if customer.get("document") is None or not customer.get(
            "document").isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if await get_customer_by_document(
            customer["document"]) is not None:
        raise fastapi.HTTPException(
            status_code=409,
            detail="Customer already exists")

    return await create_customer(customer)


@router.put("/customer/{document}")
async def update_customer_api(document: str, customer: dict) -> dict:
    if not document.isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if await get_customer_by_document(document) is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=MESSAGE_CUSTOMER_NOT_FOUND)

    return await update_customer(document, customer)


@router.delete("/customer/{document}")
async def delete_customer_api(document: str) -> dict:
    if not document.isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if await get_customer_by_document(document) is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=MESSAGE_CUSTOMER_NOT_FOUND)

    await delete_customer(document)
    return {"message": "Customer deleted!"}
