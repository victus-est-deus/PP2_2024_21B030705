# EX1
class StringOperations:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string(self):
        print(self.input_string.upper())


# EX2
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# Ex3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# EX4
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# EX5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Cannot withdraw more than the available balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from the balance")


account1 = Account("Alice", 100)

account1.deposit(200)

account1.withdraw(150)

account1.withdraw(200)


# EX6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)
