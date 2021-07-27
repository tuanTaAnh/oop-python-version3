from model.customer import *

class CustomerDAO:
    def __init__(self):
       self.cusList =  []

    def add_customer(self, customerID, customerName, contactName, address, city, postalcode, country):
        assert self.__check_unique_id(customerID), "The id is not unique"

        cus = Customer(customerID, customerName, contactName, address, city, postalcode, country)
        self.cusList.append(cus)


    def get_cus_by_id(self, id):
        for cus in self.cusList:
            if cus.get_customerID() == id:
                return cus
        return None

    def print_cuslist(self):
        print("LIST OF CUSTOMERS: ")
        for cus in self.cusList:
            print(cus.get_infor())
        print()

    def get_dict_list(self):
        cusdictlist = []
        for cus in self.cusList:
            cusdictlist.append(cus.get_infor_dist())
        return cusdictlist

    def __check_unique_id(self, id):
        for cus in self.cusList:
            if cus.get_customerID() == id:
                return False
        return True
