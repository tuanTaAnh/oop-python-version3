

class OrderDetail:
    def __init__(self, orderdetailID, order, product, quantity):
        self.__orderdetailID = orderdetailID
        self.orderID = order.get_orderID()
        self.productID = product.get_productID()
        self.quantity = quantity

    def __check_type__(self, orderdetailID, order, product, quantity):
        assert type(orderdetailID) == str, "Wrong format"
        assert str(type(order)) == "<class 'model.order.Order'>", "Wrong format"
        assert str(type(product)) == "<class 'model.product.Product'>", "Wrong format"
        assert type(quantity) == int, "Wrong format"


    # getter method
    def get_orderdetailID(self):
        return self.__orderdetailID

    # getter method
    def get_orderID(self):
        return self.orderID

    # getter method
    def get_productID(self):
        return self.productID

    # getter method
    def get_quantity(self):
        return self.quantity


    # setter method
    def set_orderdetailID(self, orderdetailID):
        self.__orderdetailID = orderdetailID

    # setter method
    def set_orderID(self, orderID):
        self.orderID = orderID

    # setter method
    def set_productID(self, productID):
        self.productID = productID

    # setter method
    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_infor(self):
        return self.__orderdetailID + ", " + self.orderID + ", " + self.productID + ", " + str(self.quantity) +  "."

    def get_infor_dist(self):
        return {
            "orderdetailID": self.__orderdetailID,
            "orderID": self.orderID,
            "productID": self.productID,
            "quantity": self.quantity,
        }