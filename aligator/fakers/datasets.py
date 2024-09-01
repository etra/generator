from faker_datasets import Provider, add_dataset


@add_dataset("cities", "./data/datasets/cities.json", picker="city")
class Cities(Provider):
    pass


@add_dataset("cities", "./data/datasets/countries.json", picker="country")
class Countries(Provider):
    pass


@add_dataset("cities", "./data/datasets/products.json", picker="product")
class Products(Provider):
    pass