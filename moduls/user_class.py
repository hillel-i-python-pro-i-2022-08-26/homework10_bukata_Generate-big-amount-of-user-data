from typing import NamedTuple


class User(NamedTuple):
    login: str
    password: str

    def __str__(self):
        return f"{self.login}: {self.password}"
