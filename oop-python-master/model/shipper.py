
class Shipper:
    def __init__(self, shipperID, shipperName, Phone):
        self.__check_type__(shipperID, shipperName, Phone)
        self.__shipperID = shipperID
        self.shipperName = shipperName
        self.Phone = Phone

    def __check_type__(self, shipperID, shipperName, Phone):
        assert type(shipperID) == str, "Wrong format"
        assert type(shipperName) == str, "Wrong format"
        assert type(Phone) == str, "Wrong format"

    # getter method
    def get_shipperID(self):
        return self.__shipperID

    # getter method
    def get_shipperName(self):
        return self.shipperName

    # getter method
    def get_Phone(self):
        return self.Phone

    # setter method
    def set_shipperID(self, shipperID):
        self.__shipperID = shipperID

    # setter method
    def set_shipperName(self, shipperName):
        self.shipperName = shipperName

    # setter method
    def set_Phone(self, Phone):
        self.Phone = Phone

    def get_infor(self):
        return str(self.__shipperID) + ", " + self.shipperName + ", "  + self.Phone + "."

    def get_infor_dist(self):
        return {
            "shipperID": self.__shipperID,
            "shipperName": self.shipperName,
            "Phone": self.Phone
        }