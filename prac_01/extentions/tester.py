minimum = int(input("what is the minimum number or x value? :"))
maximum = int(input("what is the largest or y value? : "))

for i in range(minimum, maximum, 1):
    print(i, end=' ')
print()


for i in range(minimum, maximum, 1):
    print((i*i), end=' ')
print()

