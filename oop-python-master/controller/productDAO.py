from model.product import *

class ProductDAO:
    def __init__(self):
       self.prodList =  []

    def add_product(self, productID, productName, supplier, category, unit, price):
        assert self.__check_unique_id(productID), "The id is not unique"

        prod = Product(productID, productName, supplier, category, unit, price)
        self.prodList.append(prod)


    def get_pro_by_id(self, id):
        for prod in self.prodList:
            if prod.get_productID() == id:
                return prod
        return None

    def print_prodlist(self):
        print("LIST OF PRODUCTS: ")
        for prod in self.prodList:
            print(prod.get_infor())
        print()

    def get_dict_list(self):
        proddictlist = []
        for prod in self.prodList:
            proddictlist.append(prod.get_infor_dist())
        return proddictlist


    def __check_unique_id(self, id):
        for prod in self.prodList:
            if prod.get_productID() == id:
                return False
        return True
