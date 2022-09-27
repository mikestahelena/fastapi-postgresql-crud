customers = []


async def get_all_customers():
    return customers


async def get_customer_by_document(document: str) -> dict | None:
    if len(customers) == 0:
        return None
    return next(
        (customer for customer in customers if customer["document"] == document),
        None)


async def create_customer(customer: dict) -> dict:
    if len(customers) == 0:
        max_id = 0
    else:
        max_id = max(customer["id"] for customer in customers)

    new_customer = {"id": max_id + 1, **customer}
    customers.append(new_customer)
    return new_customer


async def update_customer(document: str, customer: dict) -> dict:
    customer_to_update = await get_customer_by_document(document)
    customer_to_update["first_name"] = customer["first_name"]
    customer_to_update["last_name"] = customer["last_name"]
    customer_to_update["birthdate"] = customer["birthdate"]
    return customer_to_update


async def delete_customer(document: str) -> None:
    for customer in customers:
        if customer["document"] == document:
            customers.remove(customer)
            break
