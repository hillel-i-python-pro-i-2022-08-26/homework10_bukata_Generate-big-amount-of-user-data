from collections.abc import Iterator

from faker import Faker
import random

from moduls.user_class import User

fake = Faker()


def user() -> User:
    return User(
        login=f"{fake.unique.user_name()}_{fake.unique.word()}{random.randint(1965, 2010)}",
        password=f"{fake.unique.password()}{random.randint(1, 100000)}",
    )
