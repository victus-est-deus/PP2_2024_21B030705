# 1
def generate_squares(N):
    for i in range(N):
        yield i ** 2


for square in generate_squares(5):
    print(square)


# 2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


n = int(input("Enter a number: "))
print(','.join(str(num) for num in even_numbers(n)))


# 3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


for num in divisible_by_3_and_4(100):
    print(num)


# 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


for square in squares(1, 5):
    print(square)


# 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


for num in countdown(5):
    print(num)
