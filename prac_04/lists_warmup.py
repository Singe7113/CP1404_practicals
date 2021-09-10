numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 3
# numbers[-1] = 9
# numbers[3] = 1
# numbers[:-1] = 3 1 4 1 5
# numbers[3:4] = 4
# 5 in numbers = [4]
# 7 in numbers = [6]
# "3" in numbers = [0]
# numbers + [6, 5, 3] = 3 1 4 1 5 9 2 6 5 3

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(numbers[4])
print(numbers[6])
print(numbers[0])
print(numbers + [6, 5, 3])

numbers[0] = str('ten')
print(numbers)
numbers[-1] = 1
print(numbers[2:])
if 9 in numbers:
    print("9 is in list of numbers")