import builtins
import math
import os
import string
"""
numbers = []
x = int(input())
for i in range(x):
    num = int(input())
    numbers.append(num)
print(math.prod(numbers))
#-------------------------------------
x = input("write a string:")
u = 0
l = 0
for ch in x:
    if ch.isupper():
        u = u+1     
for ch in x:
    if ch.islower():
        l = l+1   
print(u, l)
#-------------------------------------

s = input("на палиндром надо чекнуть:")
for ch in range(len(s)//2):
    if s[ch] != s[-ch-1]:
        print('not a palindrome')
        break
    
else:
    print('palindrome goi')
#-------------------------------------


x = int(input())
y = int(input())
sq = math.sqrt(x)
print('Square root of', x ,'after', y ,'miliseconds is', sq)
#-------------------------------------

t = tuple(input())
res= all(t)
print(res)
#-------------------------------------

x = input()
print(x)
if os.path.exists(x):
    print('it exists')
    print('readeable', os.access(x, os.R_OK))
    print('writeable', os.access(x, os.W_OK))
    print(os.access(x, os.X_OK))
else:
    print('doesnt exists ')
#-------------------------------------

text = input()
if os.path.exists(text):
    print('ok')
    print(os.path.dirname(text))
    print(os.path.basename(text))
else:
    print('no') 
#-------------------------------------

file = input()
with open(file, 'r') as f:
    lines = f.readlines()
    print(len(lines))
#-------------------------------------
   
    
list1 = ['Almas', 'Alua', 'Aziz']
with open("names.txt", 'w') as f:
    for name in list1:
        f.write(name + '\n')     
print('added to a list')
#-------------------------------------

for l in string.ascii_uppercase:
    with open(f"{l}.txt", 'w') as f:
        f.write(f"it is a file {l}.txt\n")
print('created a files from a to z')
#-------------------------------------

s = input()
d = input()
with open(s, 'r') as f1, open(d, 'w') as f2:
    f2.write(f1.read())
    
print('ok')
    
#-------------------------------------

text = input()
if os.path.exists(text):
    if os.access(text, os.W_OK):
        os.remove(text)
        print('deleted')
    else:
        print('no problem i guess')
else:
    print('file jokkoi brat')
#-------------------------------------
"""
