# task 1
name = str(input("what is your name? : "))
temp_file = open("name.txt","w")
print("{}".format(name), file = temp_file)
temp_file.close()

# task 2
temp_file = open("name.txt","r")
print("Your name is {}".format(temp_file.read()))
temp_file.close()

#task 3
temp_file = open("numbers.txt","r")
numbers = temp_file.readlines()
sum_of_numbers = (int(numbers[0])+int(numbers[1]))
print(sum_of_numbers)
temp_file.close()

#task 4
file = open("numbers.txt","r")
numbers = file.readlines()
total = 0
for i in range(0, len(numbers)):
    total += int(numbers[i])
print(total)
file.close()
