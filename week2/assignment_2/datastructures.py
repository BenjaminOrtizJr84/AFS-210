# Assignment 2: Python Data Structures (List, Tuple, Set, Dictionary)

# Data1 (Tuple)
Data1 = (7, False, "Apple", True, 7, 98.6)

print(len(Data1))
print(Data1[3])
print(Data1.count(7))

# Data2 (Set)
Data2 = set(["July", 4, 8, "Tango", 4.3, "Bingo"])

Data2.pop()
Data2.add("Alpha")
print(Data2)

# Data3 (List)
Data3 = ["A", 7, -1, 3.14, True, 7]

Data3.reverse()
print(Data3)
Data3[1] = "B"
Data3.remove("A")
print(Data3)

# Data4 (Dictionary)
Data4 = { "name": "Joe", "age": 26, "active": True, "hourly_wage": 14.75 }

Data4["active"] = False
Data4["Address"] = "123 West Main Street"
hours_worked = Data4["hourly_wage"] * 40.0
print(hours_worked)
print(Data4)