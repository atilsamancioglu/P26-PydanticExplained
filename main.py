from pydantic import BaseModel


class Product(BaseModel):
    name: str  # Name must be a string
    price: float  # Price must be a float
    in_stock: bool  # In_stock must be a boolean


if __name__ == '__main__':
    # External data that we'll use to create a Product instance
    external_data = {
        'name': 'Laptop',
        'price': '999.99',  # This is a string, but Pydantic will convert it to a float
        'in_stock': 'True',  # This is a string, but Pydantic will convert it to a boolean
    }

    # product = Product(**external_data)  # Creating a Product instance
    product = Product(
        name=external_data.get('name', ""),
        price=external_data.get('price', 0),
        in_stock=external_data.get('in_stock', False)
    )

    print(product.name)  # 'Laptop'
    print(product.price)  # 999.99
    print(product.in_stock)  # True

    print(product.model_dump())

    print(type(product.name))
    print(type(product.price))
    print(type(product.in_stock))