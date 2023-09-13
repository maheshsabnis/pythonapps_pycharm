# Using the if Statement
print('Enter x')
x = input()
print('Enter y')
y = input()
# Using the 'and' keyword 
if(int(x) > 10) and (int(y) < 20):
    print ('Value is between 10 and 20 both excluding')   
else:
    print('range is invalid')     

# using the 'or' keyword
if(int(x) > 10) or (int(y)<19):
    print('the correct value')
else:
    print('Invalid value')    
    
# Using 'not'
print('Enter true/false for authenticated' )
isAuthenticated = input();
if(not (bool(isAuthenticated))):
    print('Sorry you are not authenticated');
else:
    print('You are authenticated')    
    

