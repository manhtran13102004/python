india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# 1
# i
# print('Enter your city:')
# city = input().lower()
# if city not in ['india', 'pakistan', 'bangladesh']:
#     print('Invalid city')
# else:
#     if city == 'india':
#         print(india)
#     elif city == 'pakistan':
#         print(pakistan)
#     else:
#         print(bangladesh)
        
# ii
# print('Enter city 1:')
# city1 = input().lower()
# print('Enter city 2:')
# city2 = input().lower()

# if city1 in india and city2 in india:
#     print('Both cities are in India')
# elif city1 in india and city2 in pakistan:
#     print('Both cities are in Pakistan')
# elif city1 in india and city2 in bangladesh:
#     print('Both cities are in Bangladesh')
# else:
#     print('They dont belong to same country')

print('Enter your fasting sugar level:')
fs_level = int(input())
if fs_level < 80:
    print('Your sugar is low')
elif fs_level > 100:
    print('Your sugar is hight')
else:
    print('Your sugar is normal')
    