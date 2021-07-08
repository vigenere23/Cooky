from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class AccountUserCreationRequest:
    username: str

@dataclass_json
@dataclass
class AccountInfoCreationRequest:
    firstName: str
    lastName: str
    email: str
    password: str

@dataclass_json
@dataclass
class AccountAddressCreationRequest:
    number: int
    street: str
    city: str
    country: str
    apartment: int = None

@dataclass_json
@dataclass
class AccountCreationRequest:
    user: AccountUserCreationRequest
    account: AccountInfoCreationRequest
    address: AccountAddressCreationRequest
