class Employee:

  def __init__(self, firstName, lastName, hourlyPay, employeeId):
    self.firstName = firstName
    self.lastName = lastName
    self.hourlyPay = hourlyPay
    self.employeeId = employeeId

  def pay(self, totalHours):
    if totalHours <= 40:
      newTotal = self.hourlyPay * 40
    elif totalHours > 40:
      regPay = self.hourlyPay * 40
      otHours = totalHours - 40
      otPay = self.hourlyPay * 1.5
      newTotal = regPay + (otHours * otPay)
    else:
      newTotal = 0
      print("Error: Data entry error for employee ID: " + self.employeeId)
    return newTotal
      
eId = int(input("Please enter the Employee's ID: "))
fName = input("Please enter the Employee's First Name: ")
lName = input("Please enter the Employee's Last Name: ")
hPay = float(input("Please enter the Employee's Hourly Rate: "))
totalHours = float(input("How many hours did " + fName + " work this week: "))

print( fName + "'s " + "paycheck amount is ${:,.2f}".format(totalHours))

newEmployee = Employee(eId, fName, lName, hPay)
print(newEmployee.pay(totalHours))