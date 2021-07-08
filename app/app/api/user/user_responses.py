from dataclasses import dataclass

@dataclass
class AddressResponse:
    id: int
    number: int
    street: str
    city: str
    country: str
    apartment: int = None

@dataclass
class AccountResponse:
    id: int
    id_User: int
    id_Address: int
    firstName: str
    lastName: str
    email: str
    address: AddressResponse
