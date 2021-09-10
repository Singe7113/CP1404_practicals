# scores = []
# score = int(input("score: "))
# while score >=0:
#     scores.append(score)
#     score = int(input("score: "))
# print(scores)
# print("your hightest score is {}".format(max(scores)))


print([n for n in range(1,5)])

my_list = []
for n in range(1,5):
    my_list.append(n)
print(my_list)

print([z for z in range(0,10,2)])

squares = [n**2 for n in range(1,100)]
print(squares)