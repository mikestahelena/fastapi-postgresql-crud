customers = []


def get_all_customers():
    return customers


def get_customer_by_document(document: str) -> dict:
    return next(
        (customer for customer in customers if customer["document"] == document),
        None)


def create_customer(customer: dict) -> dict:
    if len(customers) == 0:
        max_id = 0
    else:
        max_id = max(customer["id"] for customer in customers)

    new_customer = {"id": max_id + 1, **customer}
    customers.append(new_customer)
    return new_customer


def update_customer(document: str, customer: dict) -> dict:
    customer_to_update = get_customer_by_document(document)
    customer_to_update["first_name"] = customer["first_name"]
    customer_to_update["last_name"] = customer["last_name"]
    customer_to_update["birthdate"] = customer["birthdate"]
    return customer_to_update


def delete_customer(document: str) -> None:
    for customer in customers:
        if customer["document"] == document:
            customers.remove(customer)
            break
