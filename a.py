#python syntax
"""
if 5 > 2:
     print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
"""
#python comments
#1)This is a comment
"""
2)
print("Hello, World!")
rhubhuinfinfionff
fkormkfmf
ofmfmmfrm
fmkomodmeomd
"""
#variables
"""
x = 5
y = "John"
z = 4.54574
a = True
print(type(x))
print(type(y))
print(type(z))
print(type(a))
___________________________________________
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
Camel Case: myVariableName = "John"

"""
#multivariables
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
#global variables
"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
"""
#data types
"""
x = "Hello World"	                str
x = 20	                                int	
x = 20.5	                        float	
x = 1j                          	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	                        range	
x = {"name" : "John", "age" : 36}	dict
x = {"apple", "banana", "cherry"}	set		
x = True	                        bool
"""
#casting
"""
print(int(35.88))
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

"""
#strings
"""
a = "Hello, World!"
print(a[1:7])
for x in "banana":
  print(x)

txt = "The best things in life are free!"
print("free" in txt)


#slicing
b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[5:])

b = "Hello, World!"
print(b[-5:-2])

#modify strings
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = "            Hello, World!                    "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) 
"""
#String Concatenation
"""
a = "Hello"
b = "World"
c = a + b
print(c)
"""
