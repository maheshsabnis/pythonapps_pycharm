# Lambda Expression: Python lambda expressions allow you to define anonymous functions.
# Anonymous functions are functions without names. The anonymous functions are useful when you need to use them once.

# A lambda expression typically contains one or more arguments, but it can have only one expression.

# defining lambda


# Here the Third Parameter is formatter which is an anonymous function
def power(x,y, raisedTo):
    return raisedTo(x,y)

print(power(3,4,lambda x,y:  x ** y))

print(power(3,4,lambda x,y:  y ** x))

# Function that returns a lambda
# 1. Define a function  

def sq(x):
    return lambda x: x * x

# 2. Calling the function
square = sq(1)

# Since the sq() function returns a function, the square is also a function

print(square(100))
