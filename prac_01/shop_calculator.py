total = 0
error = 0
number_of_items =0
while error<=0:
    number_of_items = int(input("Number of items: "))
    if number_of_items>0:
        error = 2
    else:
        print("Invalid number of items!")
for i in range(0,number_of_items):
    price_of_item = float(input("price of item: "))
    total = total + price_of_item

#flybuys discounts
if total>100:
    discounted_total = total-(total*0.1)
    print(discounted_total)
else:
    print(total)