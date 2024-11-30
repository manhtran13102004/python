
def decorator_function(function):
    def wrapper(arg):
        if arg < 0:
            raise Exception
        return function(arg)
    return wrapper

@decorator_function
def factorial(n):
    for i in range(1, n):
        n *= i
    return n

try:
    print(factorial(int(input())))
except Exception:
    print('Khong the tinh giai thua cua 1 so am hoac 1 so khong nguyen')
