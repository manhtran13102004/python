def square_generator():
    start = 1
    # while True:
    yield start * start
    start += 1
        
for num in square_generator():
    print(num)
    if num > 1000:
        break
    