from itertools import permutations
import random
import math
# ex1
def grams_to_ounces(grams):
    return grams / 28.3495231


# ex2
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


# ex3
def solve(num_heads, num_legs):
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if 2 * chickens + 4 * rabbits == num_legs:
            return chickens, rabbits
    return None, None


# ex4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]


# ex5
def print_permutations(s):
    for perm in permutations(s):
        print(''.join(perm))


# ex6
def reverse_sentence(sentence):
    return ' '.join(reversed(sentence.split()))


# ex7
def has_33(nums):
    return any(nums[i] == 3 and nums[i + 1] == 3 for i in range(len(nums) - 1))


# ex8
def spy_game(nums):
    pattern = [0, 0, 7]
    i = 0
    for num in nums:
        if num == pattern[i]:
            i += 1
            if i == len(pattern):
                return True
    return False


# ex9
def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)


# ex10
def unique(lst):
    r = []
    for x in lst:
        if x not in r:
            r.append(x)
    return r


# ex11
def is_palindrome(s):
    p = ''.join(c.lower() for c in s if c.isalnum())
    return p == p[::-1]


# ex12
def histogram(lst):
    for number in lst:
        print('*' * number)


# ex13
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
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


