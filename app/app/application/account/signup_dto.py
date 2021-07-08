from dataclasses import dataclass


@dataclass
class UserInfo:
    username: str

@dataclass
class AccountInfo:
    firstName: str
    lastName: str
    email: str
    password: str

@dataclass
class AddressInfo:
    number: int
    street: str
    city: str
    country: str
    apartment: int = None

@dataclass
class SignupDto:
    user: UserInfo
    account: AccountInfo
    address: AddressInfo
