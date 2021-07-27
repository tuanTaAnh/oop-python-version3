import datetime

class Order:
    def __init__(self, orderID, customer, employee, shipper, OrderDate):
        self.__check_type__(orderID, customer, employee, shipper, OrderDate)
        self.__orderID = orderID
        self.customerID = customer.get_customerID()
        self.employeeID = employee.get_employeeID()
        self.shipperID = shipper.get_shipperID()
        self.OrderDate = OrderDate

    def __check_type__(self, orderID, customer, employee, shipper, OrderDate):
        assert type(orderID) == str, "Wrong format"
        assert str(type(customer)) == "<class 'model.customer.Customer'>", "Wrong format"
        assert str(type(employee)) == "<class 'model.employee.Employee'>", "Wrong format"
        assert str(type(shipper)) == "<class 'model.shipper.Shipper'>", "Wrong format"
        assert type(OrderDate) == datetime.date, "Wrong format"



    # getter method
    def get_orderID(self):
        return self.__orderID

    # getter method
    def get_customerID(self):
        return self.customerID

    # getter method
    def get_employeeID(self):
        return self.employeeID

    # getter method
    def get_shipperID(self):
        return self.shipperID

    # getter method
    def get_OrderDate(self):
        return self.OrderDate


    # setter method
    def set_orderID(self, orderID):
        self.__orderID = orderID

    # setter method
    def set_customerID(self, customerID):
        self.customerID = customerID

    # setter method
    def set_employeeID(self, employeeID):
        self.employeeID = employeeID

    # setter method
    def set_shipperID(self, shipperID):
        self.shipperID = shipperID

    # setter method
    def set_OrderDate(self, OrderDate):
        self.OrderDate = OrderDate

    def get_infor(self):
        return self.__orderID + "," + self.customerID + "," + self.employeeID + "," + self.shipperID + "," + str(self.OrderDate) + "."

    def get_infor_dist(self):
        return {
            "orderID": self.__orderID,
            "customerID": self.customerID,
            "employeeID": self.employeeID,
            "orderDate": self.OrderDate,
            "shipperID": self.shipperID
        }