integer = [0, 1, -2, -3, 4, 5, -5, 6, 7, 8]
binary = [bin(x)[2 if x >= 0 else 3:] for x in integer]
binary_dict = {}
for i in range(len(integer)):
    binary_dict[integer[i]] = binary[i]
    
additive_inverse = [-x for x in integer]

sq_set = {x * x for x in integer}

print(sq_set)