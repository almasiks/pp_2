import math
import itertools
import random
"""class StringHandler:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())
        
#_____________________________________________________

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        
#______________________________________________________
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
#______________________________________________________
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

#________________________________________________________
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
#____________________________________________________________
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

nums = [1, 2, 3, 4, 5, 6, 7, 11, 15, 17, 19, 20]
primes = list(filter(lambda x: is_prime(x), nums))
print("Prime numbers:", primes)


#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
if __name__ == "__main__":

    sh = StringHandler()
    sh.text = "hello world"
    sh.printString()
#___________________________________________________________________
sq = Square(5)
    print("Square area:", sq.area())
  rect = Rectangle(4, 6)
    print("Rectangle area:", rect.area())
#___________________________________________________________________
   # Point1
    p1 = Point(3, 4)
    p2 = Point(0, 0)
    p1.show()
    print("Distance from p1 to p2:", p1.dist(p2))

    # Account test
    acc = Account("Almas", 100)
    acc.deposit(50)
    acc.withdraw(30)
    acc.withdraw(200)

#Python functions
import math
import itertools

# 1. 
def grams_to_ounces(grams):
    return 28.3495231 * grams

print("100 grams =", grams_to_ounces(100), "ounces")


# 2. 
def fahrenheit_to_celsius(f):
    return (5/9) * (f - 32)

print("100°F =", fahrenheit_to_celsius(100), "°C")


# 3.
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2*chickens + 4*rabbits == numlegs:
            return chickens, rabbits
    return None, None

ch, rb = solve(35, 94)
print("Chickens:", ch, "Rabbits:", rb)

# 4. 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

print("Primes:", filter_prime([1, 2, 3, 4, 5, 17, 18, 19]))


# 5. 
def string_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

print("Permutations of 'abc':", string_permutations("abc"))


# 6.
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_sentence("We are ready"))


# 7. 
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))   # True
print(has_33([1, 3, 1, 3])) # False
print(has_33([3, 1, 3]))    # False


# 8.
def spy_game(nums):
    code = [0, 0, 7]
    idx = 0
    for n in nums:
        if n == code[idx]:
            idx += 1
            if idx == len(code):
                return True
    return False

print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False


# 9.
def sphere_volume(radius):
    return (4/3) * math.pi * (radius**3)

print("Volume of sphere radius 3 =", sphere_volume(3))



# 10.
def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print("Unique list:", unique_list([1, 2, 2, 3, 4, 4, 5]))


# 11.
def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == s[::-1]

print("madam ->", is_palindrome("madam"))
print("KBTU ->", is_palindrome("KBTU"))


# 12. 
def histogram(lst):
    for num in lst:
        print("*" * num)

print("Histogram:")
histogram([4, 9, 7])


# 13. 
def guess_game():
    print("Hello! What is your name?")
    name = input()
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
        
"""
# 14.
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

from movie_functions import (
    is_above_5_5,
    movies_above_5_5,
    movies_by_category,
    average_imdb,
    average_imdb_by_category
)

# 1.
print(is_above_5_5(movies[0]))  

# 2. 

print("Movies with IMDB > 5.5:", [m["name"] for m in movies_above_5_5(movies)])

# 3. 
print("Romance movies:", [m["name"] for m in movies_by_category(movies, "Romance")])

# 4. 
print("Average IMDB of all movies:", average_imdb(movies))

# 5.
print("Average IMDB of Romance movies:", average_imdb_by_category(movies, "Romance"))

