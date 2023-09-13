names = ['Jay','Mahesh', 'Mukesh Sabnis', 'Amit', 'Abhijit','Mayuresh', 'Suprotim', 'Vikram', 'Narayan Dev']
print(f"Original Names {names}")
# The sort() method
# By default, the sort() method sorts the elements of a list using the less-than operator (<). In other words, it places the lower elements before the higher ones.
names.sort()
print(f"After Sort {names}")
# Sort with reverse
names.sort(reverse=True)
print(f"After Sort with reverse {names}")

# Using the Python List sort() method to sort a list of tuples

companies = [
    ('Microsoft',500.78),
    ('Oracle', 340.89),
    ('Google', 450.56),
    ('Facebook', 80.78),
    ('Adobe', 78.67)
]

# Sort the list of tuplese of companies based on revenues

# The Sort key function
# Here the record is an entry of the tuple from the list and the 1 is the index of the value from the tuple based on which the sort is performed
def sortKey (record):
    return record[1]

companies.sort(key=sortKey)
print(companies)

# Let's try to sort the list by length of each string record from it

def sortByLen(str):
    return len(str)

names.sort(key=sortByLen)
print(f" Sort by length of each record in list {names}") 

names.sort(key=sortByLen, reverse=True)
print(f" Reverse by length of each record in list {names}") 

# Noe lets us ethe lambda instaed of explicitly declared function

names.sort(key=lambda record:len(record))
print(f" Sort by length of each record in list with lambda {names}") 


# The Sorted method
# The 'sort()' method modifies the original list whereas 'sorted()' method return the modoified string

sorted_names = sorted(names)
print(f"The new sorted list {sorted_names}") 



