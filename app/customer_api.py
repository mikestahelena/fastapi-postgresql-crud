import fastapi
from app import customer_service

router = fastapi.APIRouter()

MESSAGE_CUSTOMER_NOT_FOUND = "Customer not found"
MESSAGE_DOCUMENT_IS_REQUIRED = "Document is required"


@router.get("/customers")
def get_customers() -> list:
    return customer_service.get_all_customers()


@router.get("/customer/{document}")
def get_customer(document: str) -> dict:
    if not document.isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if (customer := customer_service.get_customer_by_document(document)) is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=MESSAGE_CUSTOMER_NOT_FOUND)

    return customer


@router.post("/customer")
def create_customer(customer: dict) -> dict:
    if customer.get("document") is None or not customer.get(
            "document").isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if customer_service.get_customer_by_document(
            customer["document"]) is not None:
        raise fastapi.HTTPException(
            status_code=409,
            detail="Customer already exists")

    return customer_service.create_customer(customer)


@router.put("/customer/{document}")
def update_customer(document: str, customer: dict) -> dict:
    if not document.isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if customer_service.get_customer_by_document(document) is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=MESSAGE_CUSTOMER_NOT_FOUND)

    return customer_service.update_customer(document, customer)


@router.delete("/customer/{document}")
def delete_customer(document: str) -> dict:
    if not document.isnumeric():
        raise fastapi.HTTPException(
            status_code=400, detail=MESSAGE_DOCUMENT_IS_REQUIRED)

    if customer_service.get_customer_by_document(document) is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=MESSAGE_CUSTOMER_NOT_FOUND)

    customer_service.delete_customer(document)
    return {"message": "Customer deleted!"}
