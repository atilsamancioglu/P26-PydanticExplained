class ProductWithoutPydantic():

    def __init__(self, name: str, price: float, in_stock: bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock


if __name__ == '__main__':
    # External data that we'll use to create a Product instance
    external_data = {
        'name': 'Laptop',
        'price': '999.99',
        'in_stock': 'True',
    }

    product = ProductWithoutPydantic(
        name=external_data.get("name", ""),
        price=external_data.get("price", 0),
        in_stock=external_data.get("in_stock", False)
    )  # Creating a Product instance

    print(product.name)  # 'Laptop'
    print(product.price)  # 999.99
    print(product.in_stock)  # True

    print(type(product.name))
    print(type(product.price))
    print(type(product.in_stock))
