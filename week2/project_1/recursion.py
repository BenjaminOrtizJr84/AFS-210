# Week 2 Project 1: Recursion

def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop1Rec(num,odd_sum):
    if num == 20:
        return odd_sum
    else:
        if (num % 2) == 1:
            odd_sum += num
    return loop1Rec((num + 1), odd_sum)

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum
    
def loop2Rec(num,even_sum):
    if (num==20):
        return even_sum
    else:
        if (num % 2) == 0:
            even_sum += num
        num += 1
    return loop2Rec((num + 1), even_sum)

print("Sum of odds between 1 and 20 using 'for' loop = " + str(loop1()))
print("Sum of odds between 1 and 20 using recursion = " + str(loop1Rec(0,0)))
print("Sum of evens between 1 and 20 using 'while loop = " + str(loop2()))
print("Sum of evens between 1 and 20 using recursion = " + str(loop2Rec(0,0)))