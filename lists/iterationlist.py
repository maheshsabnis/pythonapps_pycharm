names = ['Jay','Mahesh', 'Mukesh Sabnis', 'Amit', 'Abhijit','Mayuresh', 'Suprotim', 'Vikram', 'Narayan Dev']

# SImple loop

for name in names:
    print(name)
    
# Iteration with enumerations with idnexs

for record in enumerate(names):
    print(record)    
    
# Print the index and record seprately

for index,record in enumerate(names):
    print (f"Index = {index} value = {record}")
    
# index of a specifc record in list

print(names.index('Mahesh'))    

# If the record is not available then handle error
n = 'Mahesh Sabnis'
if name in names:
   print(f"Index of Mahesh Sabnis in names is {names.index(n)}")
else:
   print('No record found')          
    
    
