from faker import Faker
import random

from moduls.user_class import User

fake = Faker()


def get_login(key: int | None = None) -> User:
    login = f"{fake.unique.user_name()}_{fake.bothify(text='??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    if key:
        login = (
            f"{fake.unique.user_name()}_{fake.bothify(text='??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')}_"
            f"{fake.word()}{random.randint(1965, 2010)}"
        )
    return login
