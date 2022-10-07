from typing import Protocol, TypeAlias, TypedDict
from collections.abc import Iterator

from faker import Faker
import random

from services.user_generator import user

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


def generate_users(amount: int) -> Iterator[UserProtocol]:
    for _ in range(amount):
        yield user()


def main():
    amount = 100000
    users = list(generate_users(amount=amount))
    validate(users=users, amount=amount)
    return users


if __name__ == "__main__":
    main()

# Press ⌘F8 to toggle the breakpoint.
