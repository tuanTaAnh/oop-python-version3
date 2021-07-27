
class Customer:
    def __init__(self, customerID, customerName, contactName, address, city, postalcode, country):
        self.__check_type__(customerID, customerName, contactName, address, city, postalcode, country)
        self.__customerID = customerID
        self.customerName = customerName
        self.contactName = contactName
        self.address = address
        self.city = city
        self.postalcode = postalcode
        self.country = country

    def __check_type__(self, customerID, customerName, contactName, address, city, postalcode, country):
        assert type(customerID) == str, "Wrong format"
        assert type(customerName) == str, "Wrong format"
        assert type(contactName) == str, "Wrong format"
        assert type(address) == str, "Wrong format"
        assert type(city) == str, "Wrong format"
        assert type(postalcode) == str, "Wrong format"
        assert type(country) == str, "Wrong format"


    # getter method
    def get_customerID(self):
        return self.__customerID

    # getter method
    def get_customerName(self):
        return self.customerName

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

    # setter method
    def set_customerID(self, customerID):
        self.__customerID = customerID

    # setter method
    def set_customerName(self, customerName):
        self.customerName = customerName

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

    def get_infor(self):
        return self.__customerID + ", "+ self.customerName + "," + self.contactName + "," \
               + self.address + "," + self.city + "," + self.country + "," + self.postalcode + "."

    def get_infor_dist(self):
        return {
            "customerID": self.__customerID,
            "customerName": self.customerName,
            "contactName": self.contactName,
            "address": self.address,
            "city": self.city,
            "country":self.country,
             "postalcode":  self.postalcode
        }