# expenses = [2200, 2350, 2600, 2130, 2190]

# # 1
# print(expenses[1] - expenses[0])
# # 2
# print(sum(expenses[:3]))
# # 3 
# print(2000 in expenses)
# # 4
# expenses.append(1980)
# # 5
# expenses[3] += 200

# print(expenses)

heros=['spider man','thor','hulk','iron man','captain america']
# 1
print(len(heros))
# 2
heros.append('black panther')
print(heros)

# 3
heros.remove('black panther')
heros = heros[:3] + ['black panther'] + heros[3:]
print(heros)

# 4
heros = heros[:1] + ['doctor strange'] + heros[3:]
print(heros)

# 5
# print(dir(heros))
heros.sort()
print(heros)