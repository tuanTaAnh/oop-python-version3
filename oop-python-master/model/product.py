

class Product:
    def __init__(self, productID, productName, supplier, category, unit, price):
        self.__check_type__(productID, productName, supplier, category, unit, price)
        self.__productID = productID
        self.productName = productName
        self.supplierID = supplier.get_supplierID()
        self.categoryID = category.get_categoryID()
        self.unit = unit
        self.price = price

    def __check_type__(self, productID, productName, supplier, category, unit, price):
        assert type(productID) == str, "Wrong format"
        assert type(productName) == str, "Wrong format"
        assert str(type(supplier)) == "<class 'model.supplier.Supplier'>", "Wrong format"
        assert str(type(category)) == "<class 'model.category.Category'>", "Wrong format"
        assert type(unit) == int, "Wrong format"
        assert type(price) == float, "Wrong format"


    # getter method
    def get_productID(self):
        return self.__productID

    # getter method
    def get_productName(self):
        return self.productName

    # getter method
    def get_supplierID(self):
        return self.supplierID

    # getter method
    def get_categoryID(self):
        return self.categoryID

    # getter method
    def get_unit(self):
        return self.unit

    # getter method
    def get_price(self):
        return self.price


    # setter method
    def set_productID(self, productID):
        self.__productID = productID

    # setter method
    def set_productName(self, productName):
        self.productName = productName

    # setter method
    def set_supplierID(self, supplierID):
        self.supplierID = supplierID

    # setter method
    def set_categoryID(self, categoryID):
        self.categoryID = categoryID

    # setter method
    def set_unit(self, unit):
        self.unit = unit

    # setter method
    def set_price(self, price):
        self.unit = price

    def get_infor(self):
        return self.__productID + ", " + self.productName + ", " + self.supplierID + ", " + self.categoryID + ", " + str(self.unit) + ", " + str(self.price) + "."

    def get_infor_dist(self):
        return {
            "productID": self.__productID,
            "productName": self.productName,
            "supplierID": self. supplierID,
            "categoryID": self.categoryID,
            "unit": self.unit,
            "price": self.price
        }