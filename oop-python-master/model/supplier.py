
class Supplier:
    def __init__(self, supplierID, supplierName, contactName, address, city, postalcode, country, phone):
        self.__check_type__(supplierID, supplierName, contactName, address, city, postalcode, country, phone)
        self.__supplierID = supplierID
        self.supplierName = supplierName
        self.contactName = contactName
        self.address = address
        self.city = city
        self.postalcode = postalcode
        self.country = country
        self.phone = phone

    def __check_type__(self, supplierID, supplierName, contactName, address, city, postalcode, country, phone):
        assert type(supplierID) == str, "Wrong format"
        assert type(supplierName) == str, "Wrong format"
        assert type(contactName) == str, "Wrong format"
        assert type(address) == str, "Wrong format"
        assert type(city) == str, "Wrong format"
        assert type(postalcode) == str, "Wrong format"
        assert type(country) == str, "Wrong format"
        assert type(phone) == str, "Wrong format"

    # getter method
    def get_supplierID(self):
        return self.__supplierID

    # getter method
    def get_supplierName(self):
        return self.supplierName

    # getter method
    def get_contactName(self):
        return self.contactName

    # getter method
    def get_address(self):
        return self.address

    # getter method
    def get_city(self):
        return self.city

    # getter method
    def get_postalcode(self):
        return self.postalcode

    # getter method
    def get_country(self):
        return self.country

    # getter method
    def get_phone(self):
        return self.phone

    # setter method
    def set_supplierID(self, supplierID):
        self.__supplierID = supplierID

    # setter method
    def set_supplierName(self, supplierName):
        self.supplierName = supplierName

    # setter method
    def set_contactName(self, contactName):
        self.contactName = contactName

    # setter method
    def set_address(self, address):
        self.address = address

    # setter method
    def set_city(self, city):
        self.city = city

    # setter method
    def set_postalcode(self, postalcode):
        self.postalcode = postalcode

    # setter method
    def set_country(self, country):
        self.country = country

    # setter method
    def set_phone(self, phone):
        self.phone = phone

    def get_infor(self):
        return self.__supplierID + "," + self.supplierName + "," \
               + self.contactName + "," + self.address + "," + self.country + "," + self.phone + "."

    def get_infor_dist(self):
        return {
            "shipperID": self.__supplierID,
            "supplierName": self.supplierName,
            "contactName": self.contactName,
            "address": self.address,
            "city": self.city,
            "postalcode": self.postalcode,
            "country": self.country,
            "Phone": self.phone
        }