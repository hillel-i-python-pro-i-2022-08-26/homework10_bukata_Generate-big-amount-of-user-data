from typing import Protocol, TypeAlias
from collections.abc import Iterator

from faker import Faker
import random

from moduls.user_class import User
from services.user_generator import get_login

fake = Faker()

T_LOGIN: TypeAlias = str
T_PASSWORD: TypeAlias = str


class UserProtocol(Protocol):
    login: T_LOGIN
    password: T_PASSWORD


def validate(users: list[UserProtocol], amount: int) -> None:
    logins = set(map(lambda user: user.login, users))
    if amount != (amount_of_logins := len(logins)):
        raise ValueError(
            f'Not enough of unique items. Required: "{amount}". Provided: "{amount_of_logins}"'
        )


def generate_users(amount: int) -> Iterator[User]:
    logins = set()
    while len(logins) < amount:
        login = get_login(key=amount)

        if login in logins:
            continue

        logins.add(login)

        yield User(
            login=login,
            password=f"{fake.unique.password()}{random.randint(1, 100000)}",
        )


def main():
    amount = 100000
    users = list(generate_users(amount=amount))
    validate(users=users, amount=amount)


#    print(users)


if __name__ == "__main__":
    main()
