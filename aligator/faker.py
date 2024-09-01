from faker import Faker
from aligator.fakers.datasets import Cities, Countries, Products

def create_faker():
    fake = Faker()
    fake.add_provider(Cities)
    fake.add_provider(Countries)
    fake.add_provider(Products)
    return fake


faker = create_faker()
