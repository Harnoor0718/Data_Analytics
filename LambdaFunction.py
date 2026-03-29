# a = lambda b: b * 5
# print(a(4))

# x = lambda a, b, c: (a+b)*c
# print(x(2, 7, 5)) 

# Local Variables and Global Variables
# x = 5
# def hello():
#     global x
#     x = 25
#     return x
# print(hello())
# print(x)

# Problem Solving - Functions

# 1. WAF to find max of 3 numbers
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(max_of_three(12, 45, 34))

# 2. WAF to create and print a list where the values are square of numbers between 1 and 10 (both included)
def square_list():
    square = []
    for i in range(1, 11):
        square.append(i**2)
    return square

print(square_list())    

# 3. WAF tp find whether a given number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))

# 4. WAF to sum all the numbers in a list
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

print(sum_list([1, 2, 3, 4, 5]))

# 5. Fibonacci Sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10))

# using Recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

print(fibonacci(10))