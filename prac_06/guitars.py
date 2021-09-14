from guitar import guitar

print("My guitars!")
print("""
... snip ...

These are my guitars:""")

guitars=[]
x=0
while x<1:
    name = input("Name: ")
    if len(name) ==0:
        break
    year = input("Year: ")
    cost = input("Cost: ")
    print("{} ({}), worth $ {}".format(name,year,cost))
    guitars.append(guitar(name,year,cost))

# guitars.append(guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(guitar("Line 6 JTV-59", 2010, 1512.9))
# guitars.append(guitar("Fender Stratocaster", 2014, 765.40))

for listed_guitar in range(len(guitars)):
    vintage = ''
    x = guitars[listed_guitar].year
    if 2020 - x >50:
        vintage = "(vintage)" 
    print("Guitar {}:{self.name:>21} ({self.year}), worth $ {self.cost:>2}".format((listed_guitar+1),self = guitars[listed_guitar]),end=" ")
    print(vintage)