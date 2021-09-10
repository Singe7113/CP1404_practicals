name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

print("{} {} for about ${:,.0f}!".format(year,name,cost))
print()
x=0
for i in range(4):
    print("{:>3}".format(x))
    x+=50
    print()


def fn(x, y):
    z = x + y

print(fn(1, 2))