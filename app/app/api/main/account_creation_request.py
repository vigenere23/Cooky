from dataclasses import dataclass


@dataclass
class AccountUserCreationRequest:
    username: str

@dataclass
class AccountInfoCreationRequest:
    firstName: str
    lastName: str
    email: str
    password: str

@dataclass
class AccountAddressCreationRequest:
    number: int
    street: str
    city: str
    country: str
    apartment: int = None

@dataclass
class AccountCreationRequest:
    user: AccountUserCreationRequest
    account: AccountInfoCreationRequest
    address: AccountAddressCreationRequest
