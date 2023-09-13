# Using the map() function
# The map() function iterates over all elements in a list (or a tuple), applies a function to each, and returns a new iterator of the new elements.

 
names = ['Jay','Mahesh', 'Mukesh Sabnis', 'Amit', 'Abhijit','Mayuresh', 'Suprotim', 'Vikram', 'Narayan Dev']

# Convert each record in list into the uppercase

def changeToUpper(record):
    return record.upper()

iterator = map(changeToUpper,names)

for n in iterator:
    print(n)
    
# Using lambda

newiterator = map(lambda record:record.upper(),names)    
for n in newiterator:
    print(n)
 