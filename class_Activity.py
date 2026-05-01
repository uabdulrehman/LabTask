# Mall Management System

# Mall class
class MallManagement:
    def __init__(self, mall_name, number_of_floors, number_of_employees):
        self.mall_name = mall_name
        self.number_of_floors = number_of_floors
        self.number_of_employees = number_of_employees
    
    def open(self):
        print(f"{self.mall_name} is now open!")

# Floor class
class Floor:
    def __init__(self, floor_number, number_of_shops):
        self.floor_number = floor_number
        self.number_of_shops = number_of_shops
    
    def floorDetails(self):
        print(f"Floor {self.floor_number} has {self.number_of_shops} shops")
    
    def shopStatus(self):
        print(f"Checking shops on floor {self.floor_number}")

# Shops class
class Shops:
    def __init__(self, shop_name, owner_name, area_of_shop, number_of_employees):
        self.shop_name = shop_name
        self.owner_name = owner_name
        self.area_of_shop = area_of_shop
        self.number_of_employees = number_of_employees
    
    def shopDetails(self):
        print(f"Shop: {self.shop_name}, Owner: {self.owner_name}")
    
    def calcBill(self, prices):
        total = sum(prices)
        print(f"Bill: {total} Rs")
        return total

# Customer class
class Customer:
    def __init__(self, customer_id, customer_name, purchased_amount):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.purchased_amount = purchased_amount
    
    def customerDetails(self):
        print(f"Customer {self.customer_name} purchased {self.purchased_amount} Rs")

# Employee class
class Employee:
    def __init__(self, employee_id, employee_name, employee_age, employee_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_age = employee_age
        self.employee_salary = employee_salary
    
    def employeeDetails(self):
        print(f"Employee: {self.employee_name}, Age: {self.employee_age}")
    
    def calcSalary(self):
        print(f"Salary: {self.employee_salary} Rs")
        return self.employee_salary

# Maintenance class
class Maintenance:
    def __init__(self, floor_number, maintenance_incharge_name, number_of_employees):
        self.floor_number = floor_number
        self.maintenance_incharge_name = maintenance_incharge_name
        self.number_of_employees = number_of_employees
    
    def maintenance_check(self):
        print(f"Maintenance check on floor {self.floor_number}")
    
    def maintenanceDetails(self):
        print(f"Maintenance manager: {self.maintenance_incharge_name}")
    
    def checkMaintenance(self):
        print("Checking maintenance status")
    
    def staffDetails(self):
        print(f"Staff count: {self.number_of_employees}")

# Electricals class
class Electricals:
    def __init__(self, number_of_lights, number_of_fans, number_of_ac, number_of_lift, number_of_escalator):
        self.number_of_lights = number_of_lights
        self.number_of_fans = number_of_fans
        self.number_of_ac = number_of_ac
        self.number_of_lift = number_of_lift
        self.number_of_escalator = number_of_escalator
    
    def electricalsDetails(self):
        print(f"Lights: {self.number_of_lights}, Fans: {self.number_of_fans}")
        print(f"ACs: {self.number_of_ac}, Lifts: {self.number_of_lift}")
    
    def calcPowerConsumption(self):
        total_power = (60 * self.number_of_lights) + (75 * self.number_of_fans) + (1500 * self.number_of_ac)
        print(f"Power consumption: {total_power}W")
       

# MaintenanceStaff class extends Employee
class MaintenanceStaff(Employee):
    def __init__(self, employee_id, employee_name, employee_age, employee_salary, specialization):
        super().__init__(employee_id, employee_name, employee_age, employee_salary)
        self.specialization = specialization
    
    def employeeDetails(self):
        super().employeeDetails()
        print(f"Specialization: {self.specialization}")

# Shopkeeper class extends Employee
class Shopkeeper(Employee):
    def __init__(self, employee_id, employee_name, employee_age, employee_salary, shop_name):
        super().__init__(employee_id, employee_name, employee_age, employee_salary)
        self.shop_name = shop_name
    
    def employeeDetails(self):
        super().employeeDetails()
        print(f"Works at: {self.shop_name}")

# Main program
print("Mall Management System")
print("-----------------------")

# Create mall
mall = MallManagement("Centaurus Mall", 4, 100)
mall.open()

# Create floor
floor1 = Floor(1, 15)
floor1.floorDetails()

# Create shop
shop1 = Shops("Khaadi", "Abdul Rehman", 200, 6)
shop1.shopDetails()
shop1.calcBill([1500, 800, 350])

# Create customer
cust1 = Customer("C1", "M. Saad", 2650)
cust1.customerDetails()

# Create employee
emp1 = Employee("E1", "Asad", 24, 35000)
emp1.employeeDetails()

# Create maintenance
maint1 = Maintenance(1, "Abdul Wahab", 8)
maint1.maintenanceDetails()
maint1.maintenance_check()

# Create electricals
elec1 = Electricals(80, 30, 5, 2, 1)
elec1.electricalsDetails()
elec1.calcPowerConsumption()

# Create maintenance staff
mstaff1 = MaintenanceStaff("MS1", "Muneeb", 28, 28000, "Electrical")
mstaff1.employeeDetails()

# Create shopkeeper
sk1 = Shopkeeper("SK1", "Bilal", 32, 40000, "Khaadi")
sk1.employeeDetails()

print("-----------------------")
print("Program end")


