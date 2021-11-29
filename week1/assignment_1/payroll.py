class Employee:

  def __init__(self, firstName, lastName, hourlyPay, employeeId):
    self.firstName = firstName
    self.lastName = lastName
    self.hourlyPay = hourlyPay
    self.employeeId = employeeId

  def pay(self, totalHours):
    eId = int(input("Please enter the Employee's ID: "))
    fName = input("Please enter the Employee's First Name: ")
    lName = input("Please enter the Employee's Last Name: ")
    hPay = float(input("Please enter the Employee's Hourly Rate: "))
    totalHours = float(input("How many hours did " + fName + " work this week: "))
    if totalHours <= 40:
      newTotal = hPay * 40
      print(fName + " " + lName + "'s" + " paycheck amount is " + "$" + str(newTotal))
    elif totalHours > 40:
      regPay = hPay * 40
      otHours = totalHours - 40
      otPay = hPay * 1.5
      newOtTotal = regPay + (otHours * otPay)
      print(fName + " " + lName + "'s" + " paycheck amount is " + "$" + str(newOtTotal))
    else:
      print("Error: Data entry error for employee ID: " + eId)

newEmployee = Employee("", "", 0.0, 0)
print(newEmployee.pay(""))
