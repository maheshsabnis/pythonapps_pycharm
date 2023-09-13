def getStringLength(str):
    return len(str)

length = getStringLength('Mahesh Rameshrao Sabnis')
print(length)

def reverseString(str):
    return ''.join(reversed(str))

print(reverseString('Mahesh'))
# The 'f' for Literal String Interpolation
def concatenate(str1, str2, str3):
    return f"{str1} {str2} {str3}"

print('Mahesh', 'Rameshrao', 'Sabnis');

# Default Parameters

def addValues(a,b=10,c=20):
    result = 0;
    if(a > 0):
        result = a * b * c
    else:
        result =  a + b + c    
    return result    

print(addValues((-10)))
