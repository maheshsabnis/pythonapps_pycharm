rangeValue = input('Enter loop value')

for i in range(int(rangeValue)):
   # print(i)
    if i % 2 == 1:
        print (i) # only Odd number
        
print("Even Number")   


for i in range(int(rangeValue)):
   # print(i)
    if i % 2 == 0:
        print (i) # only Odd number     
    
# Using the Break

for i in range(int(rangeValue)):
   # print(i)
    if i == 6:
       break  
    else:
       print(i)        
