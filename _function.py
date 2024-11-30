def calculate_area (base, height, shape="triangle"):
    if shape == "rectangle":
        return round(base * height, 2)
    return round(base * height / 2, 2)


print ('ok')
def print_pattern(n):
    for i in range(1,n+1):
        print("*" * i)
