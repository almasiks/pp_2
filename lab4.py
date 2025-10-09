from datetime import date, timedelta
from datetime import datetime
import math
import json
"""
def generate(n):
    for i in range(1, n+1):
        yield i * i

k = int(input("enter: "))
for square in generate(k):
    print(square, end = " ")

#____________________________
def evens(n):
    for i in range(0, n+1):
        if i%2==0:
            yield i
            

k = int(input("enter n:"))
print( ",".join(str(num) for num in evens(k)))
#____________________________

def divide(n):
    for i in range(0, n+1):
        if i%3==0 and i %4==0:
            yield i
            
k = int(input("Enter k:"))
for d in divide(k):
    print(d, end=" ")
#____________________________

def squares(a, b):
    for i in range(a, b+1):
        yield i*i
        
x= int(input("enter a:"))
y = int(input("enter b:"))
for s in squares(x, y):
    print(s, end=" ")
#____________________________
 
def g(n):
    for i in range(n, -1, -1):
        yield i
        
k = int(input("enter K:"))
for nums in g(k):
    print(nums, end=" ")
#____________________________ 
 """   
 
 
"""
current = date.today()
new = current - timedelta(days=87)
print(current)
print(new)

#_____________________________

current = date.today()
tomorow = current+ timedelta(days=1)
yesterday = current-timedelta(days=1)
print(current)
print(tomorow)
print(yesterday)
#_____________________________

now = datetime.now()
micro = now.replace(microsecond = 0)
print("Original time:", now)
print("Without microseconds:", micro)
#_____________________________

from datetime import datetime

date1_str = input("Enter the first date  (DD-MM-YYYY HH:MM:SS): ")
date2_str = input("Enter the second date  (DD-MM-YYYY HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%d-%m-%Y %H:%M:%S")
date2 = datetime.strptime(date2_str, "%d-%m-%Y %H:%M:%S")

diff = abs(date2 - date1)
print("Difference in seconds:", diff.total_seconds())
#_____________________________

pi = 3.14
a = int(input('Enter degree:'))
rad =( pi * a)/180
print(rad)


h = int(input())
val1 = int(input())
val2 = int(input())
area = ((val1+val2)/2)*h
print(area)
#_____________________________
 
h = float(input())
val1 = float(input())

area = h* val1
print(area)
#_____________________________


n = int(input("Input sides: "))
s = float(input("length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print("The area is:", round(area, 2))




with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 50 + " " + "-" * 20 + "  " + "-" * 6 + "  " + "-" * 6)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr.get("dn", "")
    desc = attr.get("descr", "")
    speed = attr.get("speed", "")
    mtu = attr.get("mtu", "")
    
    print(f"{dn:<50} {desc:<20} {speed:<8} {mtu:<6}")
""" 