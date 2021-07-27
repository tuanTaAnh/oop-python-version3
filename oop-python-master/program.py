from controller.customerDAO import CustomerDAO
from controller.employeeDAO import EmployeeDAO
from controller.shipperDAO import ShipperDAO
from controller.orderDAO import OrderDAO
from controller.supplierDAO import SupplierDAO
from controller.categoryDAO import CategoryDAO
from controller.productDAO import ProductDAO
from controller.orderdetailDAO import OrderDetailDAO

import datetime
import pandas as pd
import os

ROOTPATH = r"data"


def create_cus(cusList):
    print("Nhap ID khach hang:", end=" ")
    customerID = input()
    print("Nhap ten khach hang:", end=" ")
    customerName = input()
    print("Nhap ten lien lac khach hang:", end=" ")
    contactName = input()
    print("Nhap dia chi khach hang:", end=" ")
    address = input()
    print("Nhap thanh pho khach hang:", end=" ")
    city = input()
    print("Nhap ma buu chinh khach hang:", end=" ")
    postalcode = input()
    print("Nhap quoc gia khach hang:", end=" ")
    country = input()

    cusList.add_customer(customerID, customerName, contactName, address, city, postalcode, country)

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be DD-MM-YYYY")

def create_emp(empList):
    print("Nhap ID Nhan Vien:", end=" ")
    employID = input()
    print("Nhap lastname cua Nhan Vien:", end=" ")
    lastname = input()
    print("Nhap firstname cua Nhan Vien:", end=" ")
    firstname = input()
    print("Nhap birthdate cua Nhan Vien (dd-mm-YYYY):", end=" ")
    birthdate = input()
    validate(birthdate)
    birthdate = datetime.datetime.strptime(birthdate, '%d-%m-%Y').date()
    print("Nhap duong dan anh cua Nhan Vien:", end=" ")
    photos = input()
    print("Nhap notes cua Nhan Vien:", end=" ")
    notes = input()

    empList.add_employee(employID, lastname, firstname, birthdate, photos, notes)

def create_shipper(shiList):
    print("Nhap notes cua Shipper:", end=" ")
    shipperID = input()
    print("Nhap ten cua Shipper:", end=" ")
    shipperName = input()
    print("Nhap SDT cua Shipper:", end=" ")
    Phone = input()

    shiList.add_shipper(shipperID, shipperName, Phone)

def create_order(cusList, empList, shiList, ordList):
    print("Nhap ID cua Order:", end=" ")
    orderID = input()

    print("Nhap customerID cua Order:", end=" ")
    customerID = input()

    print("Nhap employeeID cua Order:", end=" ")
    employeeID = input()

    print("Nhap shipperID cua Order:", end=" ")
    shipperID = input()

    print("Nhap OrderDate cua Order (dd-mm-YYYY):", end=" ")
    OrderDate = input()
    validate(OrderDate)
    OrderDate =  datetime.datetime.strptime(OrderDate, '%d-%m-%Y').date()

    customer = cusList.get_cus_by_id(customerID)
    assert customer != None, "No found customer ID"

    employee = empList.get_emp_by_id(employeeID)
    assert employee != None, "No found employee ID"

    shipper = shiList.get_shi_by_id(shipperID)
    assert shipper != None, "No found shipper ID"

    ordList.add_order(orderID, customer, employee, shipper, OrderDate)

def create_supplier(supList):
    print("Nhap ID cua Nha Cung Cap:", end=" ")
    supplierID = input()
    print("Nhap ten cua Nha Cung Cap:", end=" ")
    supplierName = input()
    print("Nhap ten lien lac cua Nha Cung Cap:", end=" ")
    contactName = input()
    print("Nhap dia chi cua Nha Cung Cap:", end=" ")
    address = input()
    print("Nhap thanh pho cua Nha Cung Cap:", end=" ")
    city = input()
    print("Nhap ma buu chinh cua Nha Cung Cap:", end=" ")
    postalcode = input()
    print("Nhap quoc gia cua Nha Cung Cap:", end=" ")
    country = input()
    print("Nhap SDT cua Nha Cung Cap:", end=" ")
    phone = input()

    supList.add_supplier(supplierID, supplierName, contactName, address, city, postalcode, country, phone)

def create_category(catList):
    print("Nhap ID cua Loai SP:", end=" ")
    categoryID = input()
    print("Nhap ten cua Loai SP:", end=" ")
    categoryName = input()
    print("Nhap mieu ta cua Loai SP:", end=" ")
    description = input()

    catList.add_category(categoryID, categoryName, description)

def create_product(supList, catList, prodList):
    print("Nhap ID cua San Pham:", end=" ")
    productID = input()
    print("Nhap ten cua San Pham:", end=" ")
    productName = input()

    print("Nhap supplierID cua San Pham:", end=" ")
    supplierID = input()

    print("Nhap categoryID cua San Pham:", end=" ")
    categoryID = input()

    print("Nhap unit cua San Pham:", end=" ")
    unit = input()
    assert unit.isnumeric(), 'Wrong format'
    
    print("Nhap gia cua San Pham:", end=" ")
    price = input()######## Here price can be float but is
    assert price.isnumeric(), 'Wrong format' ### This is wrong


    supplier = supList.get_sup_by_id(supplierID)
    assert supplier != None, "No found customer ID"

    category = catList.get_cat_by_id(categoryID)
    assert category != None, "No found employee ID"

    prodList.add_product(productID, productName, supplier, category, unit, price)


def create_orderdetail(ordList, prodList, ord_detList):
    print("Nhap ID cua Order Chi tiet:", end=" ")
    orderdetailID = input()

    print("Nhap orderID cua Order Chi tiet:", end=" ")
    orderID = input()

    print("Nhap productID cua Order Chi tiet:", end=" ")
    productID = input()

    print("Nhap so luong cua Order Chi tiet:", end=" ")
    quantity = input()
    assert quantity.isnumeric(), 'Wrong format'



    order = ordList.get_ord_by_id(orderID)
    assert order != None, "No found customer ID"

    product = prodList.get_pro_by_id(productID)
    assert product != None, "No found employee ID"

    ord_detList.add_orderdetail(orderdetailID, order, product, quantity)

def introduction():

    print("Bam 1 de nhap thong tin Customer")
    print("Bam 2 de nhap thong tin Employee")
    print("Bam 3 de nhap thong tin Shipper")
    print("Bam 4 de nhap thong tin Order")
    print("Bam 5 de nhap thong tin Supplier")
    print("Bam 6 de nhap thong tin Category")
    print("Bam 7 de nhap thong tin Product")
    print("Bam 8 de nhap thong tin OrderDetail")
    print("Bam cac phim khac bat ky de ket thuc chuong trinh!")


def save_csv(cusList, empList, shiList, ordList, supList, catList, prodList, ord_detList):
    cusdf = pd.DataFrame(cusList.get_dict_list())
    empdf = pd.DataFrame(empList.get_dict_list())
    shidf = pd.DataFrame(shiList.get_dict_list())
    orddf = pd.DataFrame(ordList.get_dict_list())
    supdf = pd.DataFrame(supList.get_dict_list())
    catdf = pd.DataFrame(catList.get_dict_list())
    proddf = pd.DataFrame(prodList.get_dict_list())
    ord_detdf = pd.DataFrame(ord_detList.get_dict_list())

    cusdf.to_csv(os.path.join(ROOTPATH, "cus.csv"))
    empdf.to_csv(os.path.join(ROOTPATH, "empdf.csv"))
    shidf.to_csv(os.path.join(ROOTPATH, "shidf.csv"))
    orddf.to_csv(os.path.join(ROOTPATH, "orddf.csv"))
    supdf.to_csv(os.path.join(ROOTPATH, "supdf.csv"))
    catdf.to_csv(os.path.join(ROOTPATH, "catdf.csv"))
    proddf.to_csv(os.path.join(ROOTPATH, "proddf.csv"))
    ord_detdf.to_csv(os.path.join(ROOTPATH, "ord_detdf.csv"))

    print("SAVE CSV FILES SUCCESSFULLY!")


def progame():
    cusList = CustomerDAO()
    empList = EmployeeDAO()
    shiList = ShipperDAO()
    ordList = OrderDAO()
    supList = SupplierDAO()
    catList = CategoryDAO()
    prodList = ProductDAO()
    ord_detList = OrderDetailDAO()

    introduction()

    while True:
        try:
            print("Nhap yeu cau: ", end="")
            option = input()
            if option == "1":
                create_cus(cusList)
            elif option == "2":
                create_emp(empList)
            elif option == "3":
                create_shipper(shiList)
            elif option == "4":
                create_order(cusList, empList, shiList, ordList)
            elif option == "5":
                create_supplier(supList)
            elif option == "6":
                create_category(catList)
            elif option == "7":
                create_product(supList, catList, prodList)
            elif option == "8":
                create_orderdetail(ordList, prodList, ord_detList)
            else:
                break
        except AssertionError as e:
            print("INPUT ERROR: ", e)
            print("Ban ghi khong duoc chap nhan.")

    cusList.print_cuslist()

    save_csv(cusList, empList, shiList, ordList, supList, catList, prodList, ord_detList)

    print("END PROGRAME")




if __name__ == '__main__':
    progame()




