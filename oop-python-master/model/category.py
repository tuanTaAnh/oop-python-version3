
class Category:
    def __init__(self, categoryID, categoryName, description):
        self.__check_type__(categoryID, categoryName, description)
        self.__categoryID = categoryID
        self.categoryName = categoryName
        self.description = description

    def __check_type__(self, categoryID, categoryName, description):
        assert type(categoryID) == str, "Wrong format"
        assert type(categoryName) == str, "Wrong format"
        assert type(description) == str, "Wrong format"


    # getter method
    def get_categoryID(self):
        return self.__categoryID

    # getter method
    def get_categoryName(self):
        return self.categoryName

    # getter method
    def get_description(self):
        return self.description


    # setter method
    def set_categoryID(self, categoryID):
        self.__categoryID = categoryID

    # setter method
    def set_categoryName(self, categoryName):
        self.categoryName = categoryName

    # setter method
    def set_description(self, description):
        self.description = description


    def get_infor(self):
        return self.__categoryID + "," + self.categoryName + ","  + self.description + "."

    def get_infor_dist(self):
        return {
            "categoryID": self.__categoryID,
            "categoryName": self.categoryName,
            "description": self.description,
        }