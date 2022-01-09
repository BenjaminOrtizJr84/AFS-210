import random

myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

print ("The original list is: " + str(myList))

for i in range(len(myList)-1, 0, -1):
        j = random.randint(0, i + 1)
        myList[i], myList[j] = myList[j], myList[i]
print ("Here is my shuffled list: " + str(myList))

# The time complexity for this algorithm is O(n).