class Employee:
    
    def __init__(self, firstName, lastName, employeeID, hourlyPay):
        self.firstName = input("Enter first name: ")
        self.lastName = input("Enter last name: ")
        self.employeeID = int(input("Enter employee id: "))
        self.hourlyPay = float(input("Enter hourly rate: "))
        
    