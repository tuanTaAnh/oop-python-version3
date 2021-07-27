from model.orderdetails import *

class OrderDetailDAO:
    def __init__(self):
       self.orddeList =  []

    def add_orderdetail(self, orderdetailID, order, product, quantity):
        assert self.__check_unique_id(orderdetailID), "The id is not unique"

        ord_det = OrderDetail(orderdetailID, order, product, quantity)
        self.orddeList.append(ord_det)


    def get_orderdetail_by_id(self, id):
        for ord_det in self.orddeList:
            if ord_det.get_orderdetailID() == id:
                return ord
        return None

    def print_orderdetaildlist(self):
        print("LIST OF ORDER DETAILS: ")
        for ord_det in self.orddeList:
            print(ord_det.get_infor())
        print()

    def get_dict_list(self):
        ord_dedictlist = []
        for ord_de in self.orddeList:
            ord_dedictlist.append(ord_de.get_infor_dist())
        return ord_dedictlist


    def __check_unique_id(self, id):
        for ord_det in self.orddeList:
            if ord_det.get_orderdetailID() == id:
                return False
        return True
