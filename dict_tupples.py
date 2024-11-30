import numpy as np
from math import pi
def program1():
    dict = {"china": 143, "india": 136, "usa": 32, "pakistan": 21}
    print("Choose your choice: print/add/remove/query")
    choice = input()
    if choice not in {"print", "add", "remove", "query"}:
        print("Not valid choice!")
        return

    if choice == "print":
        for id, value in dict.items():
            print(f"{id}==>{value}")
    elif choice == "add":
        print("Enter your country u want to add:")
        country = input()
        if country in dict:
            print("Country exists")
            return
        print("Enter population:")
        population = input()
        dict[country] = population
        for id, value in dict.items():
            print(f"{id}==>{value}")
    elif choice == "remove":
        print("Enter the country name u want to remove")
        country = input()
        country = country.lower()
        if country not in dict:
            print("Country doesn't exist")
            return

        del dict[country]
        for id, value in dict.items():
            print(f"{id}==>{value}")
    else:
        print("Enter the country name")
        country = input()
        country = country.lower()
        if country not in dict:
            print("Country doesn't exist")
            return
        print(f"{country}==>{dict[country]}")


def program2():
    dict = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}
    print("Enter your choice: (print/add):")
    choice = input()
    choice = choice.lower()
    if choice not in {"print", "add"}:
        return
    elif choice == "print":
        for id, value in dict.items():
            print(f"{id} ==> {value} ==> avg: {round(np.mean(value), 2)}")
    else:
        print("Enter your stock to be added:")
        stock = input()
        stock = stock.lower()
        print("Enter the price:")
        price = float(input())
        if stock not in dict:
            dict[stock] = price
            print(dict)
            return
        dict[stock].append(price)
        print(dict)

def circle_calc(radius):
    area = pi * radius * radius
    cir = 2 * radius * pi
    dia = 2 * radius
    area, cir, dia = [round(x, 2) for x in [area, cir, dia]]
    return [area, cir, dia]

a, b, c = circle_calc(float(input()))
print(f"area: {a}, circumference: {b}, diameter: {c}")