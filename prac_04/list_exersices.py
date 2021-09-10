number=[]
for x in range(5):
    number.append(int(input("number : ")))

print("first number is {}".format(number[0]))
print("the last number is {}".format(number[-1]))
print("the smallest number is {}".format(min(number)))
print("the largest number is {}".format(max(number)))
print("the average number is {}".format((sum(number)/len(number))))