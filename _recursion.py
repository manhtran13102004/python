# 1
def sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum(arr[1:])

# 2
def key(n, base):
    if base != 16 or n < 10:
        return str(n)
    dict = {a:chr(a+55) for a in range(10, 16)}
    return dict[n]

def convert_to_str(n, base=1):
    if n < base:
        return key(n, base)
    return convert_to_str(n//base, base) + key(n%base, base)
print(convert_to_str(243, 8))
# 3
def sum2(x):
    return 0 if x == None or x == [] else x if type(x) == int else sum2(x[0]) + sum2(x[1:])

# a = [1, 2, [3,4], [5,6]]

# 4
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# 5
def fibonacci(n):
    if n == 0 or n == 1:    
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 6
def sum_digit(n):
    if n < 10:
        return n
    return n % 10 + sum_digit(n//10)

# 7
def sum3(n, x=0):
    if n-x <= 0:
        return n-x
    
    return n - x + sum3(n, x+2)

# 8
def sum4(n):
    if n == 1:
        return 1
    return round(1/n + sum4(n-1), 2)

# 9
def sum5(n):
    if n <= 0:
        return 1
    return 1/(2**n) + sum5(n-1)

# 10
def pow1(a, b):
    if b == 0:
        return 1
    return pow1(a, b//2) * pow1(a, b//2) if b % 2 == 0 else pow1(a, b//2) * pow1(a, b//2) * a

# 11
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
