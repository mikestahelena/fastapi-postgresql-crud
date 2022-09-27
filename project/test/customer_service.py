import pytest

from project.app import customer_service

customers = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "document": "12345678910",
        "birthdate": "1900-01-01",
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Doe",
        "document": "12345678911",
        "birthdate": "1900-01-01",
    },
]


@pytest.fixture
def get_customer() -> dict:
    return {
        "first_name": "John",
        "last_name": "Jones",
        "document": "12345678915",
        "birthdate": "1900-01-01",
    }


@pytest.fixture
def new_customer() -> dict:
    return {
        "first_name": "Ralph Waldo",
        "last_name": "Emerson",
        "document": "12345678920",
        "birthdate": "1900-01-03",
    }


@pytest.mark.asyncio
async def test_get_customer(new_customer: dict) -> None:
    created_customer = await customer_service.create_customer(new_customer)
    assert await customer_service.get_customer_by_document(
        "12345678920") == created_customer


@pytest.mark.asyncio
async def test_get_customer_not_found() -> None:
    assert await customer_service.get_customer_by_document("98765432100") is None


@pytest.mark.asyncio
async def test_create_customer(get_customer: dict) -> None:
    created_customer = await customer_service.create_customer(get_customer)
    assert created_customer["document"] == get_customer["document"]
    assert created_customer["first_name"] == get_customer["first_name"]
    assert created_customer["last_name"] == get_customer["last_name"]
    assert created_customer["birthdate"] == get_customer["birthdate"]


@pytest.mark.asyncio
async def test_update_customer(get_customer: dict) -> None:
    customer = await customer_service.create_customer({
        "first_name": "John",
        "last_name": "Jones",
        "document": "12345678919",
        "birthdate": "1900-01-01"})
    customer["first_name"] = "Joseph"
    assert await customer_service.update_customer(
        customer["document"], customer) == customer


@pytest.mark.asyncio
async def test_delete_customer() -> None:
    await customer_service.delete_customer("12345678910")
    assert await customer_service.get_customer_by_document("12345678910") is None
