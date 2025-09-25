"""
#boolean
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
   
#lists
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

"""
#tuple
"""
tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))
"""
#set
"""
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

____________________________________
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset.pop())

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
_________________________________________

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
__________________________________________

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
__________________________________________

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
_____________________________________________

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
______________________________________________
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)
_____________________________________________

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
"""
#dictionaries
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])
print(len(thisdict))
x = thisdict.keys()
y = thisdict.values()
print(x)
____________________________________


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
___________________________________

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
"""
#if else
"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
_________________________________

a = 33
b = 200

if b > a:
  pass
"""
#match
"""
day = 7
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
"""
#while
"""
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  _________________________
  
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
"""
#for loop
"""
for x in "banana":
  print(x)
_____________________________________
for x in range(6):
  print(x)
_______________________________________

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
"""
