my_list = ['a', [1,2,3],'z']
print(my_list[1])
print(my_list[1][0])
print(my_list[1][1])

print(my_list[1][-1] == my_list[1][2])

my_list2 = [4,5,6,7,8,4,2,5,7,2,6,35]
temp_list = my_list2.sort()
print(temp_list)


from operator import itemgetter


data = [['derick',2],['fhannah',7],['sam',18],['tommy',13],['adam',4]]
print(data)
data.sort()
print(data)


# this is helpful for the assessment
#
# using split is also helpful
#
# search the join method 

my_str = "this is a test"
string_elements = my_str.split()
print(string_elements)

reverse_elements =[]

for element in string_elements:
    reverse_elements.append(element[::-1]) 

print(reverse_elements)

choice = input("choose a,b,c or d:")
while choice not in["a","b","c","d"]:
    print("invald input")
    choice = input("choose a,b,c or d:")
# basic layout for menu



