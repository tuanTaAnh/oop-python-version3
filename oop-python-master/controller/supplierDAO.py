from model.supplier import *

class SupplierDAO:
    def __init__(self):
       self.supList =  []

    def add_supplier(self, supplierID, supplierName, contactName, address, city, postalcode, country, phone):
        assert self.__check_unique_id(supplierID), "The id is not unique"

        sup = Supplier(supplierID, supplierName, contactName, address, city, postalcode, country, phone)
        self.supList.append(sup)


    def get_sup_by_id(self, id):
        for sup in self.supList:
            if sup.get_supplierID() == id:
                return sup
        return None

    def print_suplist(self):
        print("LIST OF SUPPLIERS: ")
        for sup in self.supList:
            print(sup.get_infor())
        print()

    def get_dict_list(self):
        supdictlist = []
        for sup in self.supList:
            supdictlist.append(sup.get_infor_dist())
        return supdictlist


    def __check_unique_id(self, id):
        for sup in self.supList:
            if sup.get_supplierID() == id:
                return False
        return True
