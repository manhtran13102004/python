# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

# heads_time = 0
# for rs in result:
#     if rs == 'heads':
#         heads_time += 1
        
# print(heads_time)

# print([x**2 for x in range(1, 11) if x % 2 == 1])

# expense_list = [2340, 2500, 2100, 3100, 2980]
# month_list = ['January', 'Febuary', 'March', 'April', 'May']

# print('Enter an expense amount:')
# expense = int(input())
# for i, val in enumerate(expense_list):
#     if val == expense:
#         print(month_list[i])
#         break
#     if i == 4:
#         print('Not found')

# for i in range(1, 5):
#     print('Are u tired?')
#     choice = input().lower()
#     if choice == 'yes':
#         print('You didnt finish the race')
#         break
#     else:
#         if i == 4:
#             print('Congratulation!')
#         continue
        
for i in range(5):
    print('*' * (i + 1))