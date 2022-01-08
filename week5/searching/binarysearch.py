def binary_search(sorted_list, search_term):
    size_of_list = len(sorted_list) - 1
    
    first_index = 0
    last_index = size_of_list
    
    while first_index <= last_index:
        midpoint = (first_index + last_index) // 2
        
        if sorted_list[midpoint] == search_term:
            return True
        
        elif search_term > sorted_list[midpoint]:
            first_index = midpoint + 1
            
        elif search_term < sorted_list[midpoint]:
            last_index = midpoint - 1
        
    return False
    
myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
myList2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(binary_search(myList, 7))
print(binary_search(myList, 77))
print(binary_search(myList2, "Delta"))
