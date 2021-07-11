from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class AddressEditionRequest:
    country: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    number: Optional[int] = None
    apartment: Optional[int] = None


@dataclass_json
@dataclass
class AccountEditionRequest:
    email: Optional[str] = None
    password: Optional[str] = None
