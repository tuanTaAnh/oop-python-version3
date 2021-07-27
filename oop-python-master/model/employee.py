import datetime

class Employee:
    def __init__(self, employeeID, lastname, firstname, birthdate, photos, notes):
        self.__check_type__(employeeID, lastname, firstname, birthdate, photos, notes)
        self.__employeeID = employeeID
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.photos = photos
        self.notes = notes

    def __check_type__(self, employeeID, lastname, firstname, birthdate, photos, notes):
        assert type(employeeID) == str, "Wrong format"
        assert type(lastname) == str, "Wrong format"
        assert type(firstname) == str, "Wrong format"
        assert type(birthdate) == datetime.date, "Wrong format"
        assert type(photos) == str, "Wrong format"
        assert type(notes) == str, "Wrong format"


    # getter method
    def get_employeeID(self):
        return self.__employeeID

    # getter method
    def get_lastname(self):
        return self.lastname

    # getter method
    def get_firstname(self):
        return self.firstname

    # getter method
    def get_birthdate(self):
        return self.birthdate

    # getter method
    def get_photos(self):
        return self.photos

    # getter method
    def get_notes(self):
        return self.notes

    # setter method
    def set_employeeID(self, employeeID):
        self.__employeeID = employeeID

    # setter method
    def set_lastname(self, lastname):
        self.lastname = lastname

    # setter method
    def set_firstname(self, firstname):
        self.firstname = firstname

    # setter method
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    # setter method
    def set_photos(self, photos):
        self.photos = photos

    # setter method
    def set_notes(self, notes):
        self.notes = notes

    def get_infor(self):
        return str(self.__employeeID) + ", " + self.lastname + ", " \
               + self.firstname + ", " + str(self.birthdate) + ", " + self.photos + ", " + self.notes + "."

    def get_infor_dist(self):
        return {
            "employID": self.__employeeID,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "photos": self.photos,
             "notes":  self. notes
        }