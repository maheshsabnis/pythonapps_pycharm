names = ['Jay','Mahesh', 'Mukesh Sabnis', 'Amit', 'Abhijit','Mayuresh', 'Suprotim', 'Vikram', 'Narayan Dev']
# Start from the first index (1) and go till the
# End to the index (n-1) means if n is 4th record in the list means the 3rd value considering from the 0th index  
slicedList = names[1:4]

print(slicedList);

# Get the first n elements from the list
# The following expression will return first 6 element from the list
# means from 0 to 5 (indexes) 
print(names[:6])

# Get every specific nth record from the list
# Get every third record from the list
# the 3 is the step
print(names[::3])

# Reverse the list using slice with value as -1
print(names[::-1]);

# Using slicign to updating specific elements from the list
print(f"Orginal List {names}")
names[0:3] = ['Jay Kumar','Mahesh Sabnis']
print(f"After Modification List {names}")

 