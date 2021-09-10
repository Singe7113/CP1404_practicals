for i in range(1, 21, 2):
    print(i, end=' ')
print()

for x in range(0, 110, 10):
    print(x, end=' ')
print()

for y in range(20, 0, -1):
    print(y, end=' ')
print()

number_of_star = int(input("what number of stars do you want? : "))
for number_of_star in range(0, number_of_star,1):
    print("*", end='')
    
star_staircase = int(input("what number of stars do you want? : "))
for star_staircase in range(0,star_staircase):
    for X in range (0,star_staircase+1):
        print("*",end='')
    print()