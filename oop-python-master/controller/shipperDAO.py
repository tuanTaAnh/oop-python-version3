from model.shipper import *

class ShipperDAO:
    def __init__(self):
       self.shipperList =  []

    def add_shipper(self, shipperID, shipperName, Phone):
        assert self.__check_unique_id(shipperID), "The id is not unique"

        shi = Shipper(shipperID, shipperName, Phone)
        self.shipperList.append(shi)

    def get_shi_by_id(self, id):
        for shi in self.shipperList:
            if shi.get_shipperID() == id:
                return shi
        return None


    def print_emplist(self):
        print("LIST OF SHIPPER: ")
        for shi in self.shipperList:
            print(shi.get_infor())
        print()

    def get_dict_list(self):
        shidictlist = []
        for shi in self.shipperList:
            shidictlist.append(shi.get_infor_dist())
        return shidictlist

    def __check_unique_id(self, id):
        for shi in self.shipperList:
            if shi.get_shipperID() == id:
                return False
        return True