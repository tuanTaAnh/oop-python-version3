from controller.customerDAO import CustomerDAO
from controller.employeeDAO import EmployeeDAO
from controller.shipperDAO import ShipperDAO
from controller.orderDAO import OrderDAO
from controller.supplierDAO import SupplierDAO
from controller.categoryDAO import CategoryDAO
from controller.productDAO import ProductDAO
from controller.orderdetailDAO import OrderDetailDAO

from datetime import datetime



if __name__ == '__main__':

    cusList = CustomerDAO()

    cusList.add_customer("123", "Ta Anh Tuan", "TuanTA51", "Duy Tan", "Ha Noi", "B123", "VietNam")
    cusList.add_customer("1234", "Ta Anh ABC", "ABC51", "Duy Tan", "Ha Noi", "B123", "VietNam")
    cusList.print_cuslist()


    empList = EmployeeDAO()

    empList.add_employee("123", "Ta", "Anh Tuan", datetime.strptime("26-10-1998", '%d-%m-%Y').date(), "forder/taanhtuan", "Fresher")
    empList.add_employee("120", "Ta", "Van A", datetime.strptime("20-10-1999", '%d-%m-%Y').date(), "forder/tavana", "Fresher")
    empList.print_emplist()


    shiList = ShipperDAO()

    shiList.add_shipper("123", "Ta Anh Tuan", "0326831080")
    shiList.add_shipper("124", "Phan Duc Duy", "0982914798")
    shiList.print_emplist()


    ordList = OrderDAO()

    orderID = "145"
    customerID = "123"
    employeeID = "120"
    shipperID = "123"
    OrderDate = datetime.strptime("20-12-2020", '%d-%m-%Y').date()

    cus = cusList.get_cus_by_id(customerID)
    assert cus != None, "No found customer ID"

    emp = empList.get_emp_by_id(employeeID)
    assert emp != None, "No found employee ID"

    shi = shiList.get_shi_by_id(shipperID)
    assert shi != None, "No found shipper ID"

    ordList.add_order(orderID, cus, emp, shi, OrderDate)
    ordList.print_ordlist()

    supList = SupplierDAO()

    supList.add_supplier("123", "LS", "Cong ty LS", "Duy Tan", "Ha Noi", "B123", "VietNam", "0326831080")
    supList.add_supplier("1234", "Samsung", "Cong ty SamSung", "Duy Tan", "Ha Noi", "B123", "VietNam", "0983412874")
    supList.print_suplist()

    catList = CategoryDAO()

    catList.add_category("120", "Tivi", "Man 2k")
    catList.add_category("1204", "Dien thoai", "Phan khuc tam trung")
    catList.print_carlist()

    prodList = ProductDAO()

    productID = "120"
    productName = "SamsungS9"
    supplierID = "123"
    categoryID = "120"
    unit = 20
    price = 1000

    sup = supList.get_sup_by_id(supplierID)
    assert sup != None, "No found customer ID"

    cat = catList.get_cat_by_id(categoryID)
    assert cat != None, "No found employee ID"

    prodList.add_product(productID, productName, sup, cat, unit, float(price))
    prodList.print_prodlist()

    ord_detList = OrderDetailDAO()

    orderdetailID = "199"
    orderID = "145"
    productID = "120"
    quantity = 10

    ord = ordList.get_ord_by_id(orderID)
    assert ord != None, "No found customer ID"

    pro = prodList.get_pro_by_id(productID)
    assert pro != None, "No found employee ID"

    ord_detList.add_orderdetail(orderdetailID, ord, pro, quantity)
    ord_detList.print_orderdetaildlist()



