# Get the recursion Limit
import sys
print(sys.getrecursionlimit())


# Recursive function for the number count down


def print_Count_Down(value):
    print(value)
    # decrease value
    next = value - 1
    #condition
    if next > 0:
        print_Count_Down(next)
        
        
print(print_Count_Down(10)) 

# REsursion to calculate teh sum of numbers

def calculateSum(value):
    sum=0
    for v in range(value):
        sum+=v
    return sum    
    
print(calculateSum(10000))

# Simple Recursion to calculate the sum

def calculateSumSimple(value):
    if value > 0:
        return value + calculateSumSimple(value - 1)
    return 0
    
print(calculateSumSimple(100))


     