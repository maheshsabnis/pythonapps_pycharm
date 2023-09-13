# Defining  List

numbers = [1,2,3,4,5,6,7,8,9]

print(numbers)

# Number at the 0th index and the last number

print(f"0th index = {numbers[0]} and last number {numbers[-1]}")

# Lets update the number at 0th index

numbers[0]=10;
print(f"0th index = {numbers[0]} and last number {numbers[-1]}")

# Add an element in the list
numbers.append(100);
print(numbers)

# insert the number in list at any postion
numbers.insert(2,200) 
print(numbers)
numbers.insert(6,200) 

# Removing the number from the list
print(f"Original list {numbers}")
del numbers[10]

print(f"List afdter deleting the record {numbers}")

# Remove last record from the list

print(f"Original list {numbers}")
last = numbers.pop()

print(f"Last record removed {last}") 

print(f"List afdter deleting the record {numbers}")

# Pop the element by its position

print(f"Original list {numbers}")
element = numbers.pop(3)

print(f"Last element removed {element}") 

print(f"List afdter deleting the record {numbers}")

# Remove the first occurred  element matched by value

print(f"Original list {numbers}")

numbers.remove(200)

print(f"List after deleting the record {numbers}")