# When we define a function, its is very difficult to kniow which vaue is passed to which posiotnal parameter . This is the reason the python introduces the Keyword arguments  
# When you use the keyword arguments, their names that matter, not their positions.

# Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.

def keyArgFn(a,b):
    print(a ** b)
 
print(keyArgFn(b=4,a=2))    