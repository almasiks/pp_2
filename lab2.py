"""
print(10 > 9)
print(10 == 9)
print(10 < 9)
_____________________________________
a = 200
b = 333

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 
_______________________________________
print(type(bool("Hello")))
print(bool(15))
________________________________________

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
____________________________________________

#will return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
#bool({})
_____________________________________________

class myclass():
      def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))
________________________________________________
def myFunction() :
      return True

print(myFunction())

def myFunction() :
      return True
____________________________________________________
if myFunction():
  print("YES!")
else:
  print("NO!")
 
x = 200
print(isinstance(x, int))
   """