from model.category import *

class CategoryDAO:
    def __init__(self):
       self.catList =  []

    def add_category(self, categoryID, categoryName, descriptione):
        assert self.__check_unique_id(categoryID), "The id is not unique"

        cat = Category(categoryID, categoryName, descriptione)
        self.catList.append(cat)


    def get_cat_by_id(self, id):
        for cat in self.catList:
            if cat.get_categoryID() == id:
                return cat
        return None

    def print_carlist(self):
        print("LIST OF Category: ")
        for cat in self.catList:
            print(cat.get_infor())
        print()

    def get_dict_list(self):
        catdictlist = []
        for cat in self.catList:
            catdictlist.append(cat.get_infor_dist())
        return catdictlist


    def __check_unique_id(self, id):
        for cat in self.catList:
            if cat.get_categoryID() == id:
                return False
        return True
