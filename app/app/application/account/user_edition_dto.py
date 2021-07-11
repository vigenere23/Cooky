from dataclasses import dataclass


@dataclass
class AddressInfoEditionDto:
    country: str = None
    city: str = None
    street: str = None
    number: int = None
    apartment: int = None


@dataclass
class AccountInfoEditionDto:
    email: str = None
    password: str = None
