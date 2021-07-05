from app.app import db
from app.infra.db.models.user import AddressModel
from app.infra.db.daos.base_dao import BaseDao


class AddressDao(BaseDao):

    def __init__(self):
        super().__init__('Address', AddressModel)

    def getAddress(self, id):
        query = 'SELECT * FROM Address WHERE id = %(id)s'
        result = db.find(query, {'id': id})
        return self._mapper.from_tuple(result)

    def modifyCountry(self, country, id):
        query = 'UPDATE Address SET country = \'{}\' WHERE id = {}'.format(
            country, id)
        db.replace(query, {'id': id, 'country': country})
        return {"id": id, "country": country}

    def modifyCity(self, city, id):
        query = 'UPDATE Address SET city = \'{}\' WHERE id = {}'.format(
            city, id)
        db.replace(query, {'id': id, 'city': city})
        return {"id": id, "city": city}

    def modifyStreet(self, street, id):
        query = 'UPDATE Address SET street = \'{}\' WHERE id = {}'.format(
            street, id)
        db.replace(query, {'id': id, 'street': street})
        return {"id": id, "street": street}

    def modifyApartment(self, apartment, id):
        query = 'UPDATE Address SET apartment = \'{}\' WHERE id = {}'.format(
            apartment, id)
        db.replace(query, {'id': id, 'apartment': apartment})
        return {"id": id, "apartment": apartment}

    def modifyDoorNumber(self, number, id):
        query = 'UPDATE Address SET number = \'{}\' WHERE id = {}'.format(
            number, id)
        db.replace(query, {'id': id, 'number': number})
        return {"id": id, "number": number}

    def save(self, addressModel, autocommit=True):
        if not isinstance(addressModel, AddressModel):
            raise ValueError("addressModel should be of type AddressModel")

        query = 'INSERT INTO Address (`id`,`number`,`apartment`,`street`,`city`,`country`) VALUES (%s, %s, %s, %s, %s, %s)'
        newAddressId = db.create(
            query, self._mapper.to_tuple(addressModel), autocommit)

        if newAddressId:
            return self.getById(newAddressId)
        else:
            raise Exception("Could not save commend")
