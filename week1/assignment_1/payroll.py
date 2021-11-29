class Employee:
    
    def __init__(self, firstName, lastName, employeeID, hourlyPay, totalHours):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID
        self.hourlyPay = hourlyPay
        self.totalHours = totalHours
        
    def pay(self):
        if self.totalHours <= 40:
            newTotal = self.totalHours * self.hourlyPay
            print(newEmployee.firstName + " " + newEmployee.lastName + "'s" " paycheck amount is " + "$" + str(newTotal))
        elif self.totalHours > 40:
            regularPay = 40 * self.hourlyPay
            overTime = self.totalHours - 40
            overTimePay = self.hourlyPay * 1.5
            newTotalPay =  overTime * overTimePay + regularPay
            print(newEmployee.firstName + " " + newEmployee.lastName + "'s" " paycheck amount is " + "$" + str(newTotalPay))
        else:
            print('Error: Data entered did not calculate, please try again.')

newEmployee = Employee(employeeID = int(input("Please enter the Employee's ID: ")), 
                       firstName = input("Please enter the Employee's First Name: "),
                       lastName = input("Please enter the Employee's Last Name: "), 
                       hourlyPay = float(input("Please enter the Employee's Hourly Pay Rate: ")), 
                       totalHours = float(input("How many hours did the Employee work this week? ")))
  
print(newEmployee.pay())