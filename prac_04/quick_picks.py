import random

templist=[]
number_of_quick_picks = int(input("what number of quick picks do youw want? : "))
random_number_list = [[]]*number_of_quick_picks

for column in range(number_of_quick_picks):
    for row in range(6):
        temp_number = random.randint(1, 46)
        while temp_number in templist:
            temp_number = random.randint(1, 46)
        templist.append(temp_number)
    random_number_list[column] = templist
    random_number_list[column].sort()
    templist = []
for column in range(len(random_number_list)):
    print("{:4}".format(random_number_list[column]))
