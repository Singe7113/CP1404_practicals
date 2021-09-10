for char in 'hi mum':
    print(char, type(char))

print('\n')

x=2 #inseart ranndo number to see if he is even or not
if (x/2) == True:
            print("he even")
print('\n')

#how to test to see if a str vaule is present in another str vaule
word = 'aabbccdd'
if 'a' in word:
    print("there a nother a in there")
print('\n')

#strings are inmutable, they can not be mutated, only cut and copied
word = 'spam'
print(word[:1])
print(word[2:])
new_word = word[:1] + 'l' +word[2:]
print(new_word)
print('\n')

#functions : len
word = 'hello world'
print(word)
print(len(word))
print('\n')

text = 'pyrhon Rules!'
print(text)
print (text.upper())
print('\n')

print(text)
print (text.find('l')) #tells me the location of the l in the test str
print('\n')

#chaining methods
# this is used to make sure that you have all the same type of str.types 
print(text)
print (text.upper())
print (text.find('L'))
print('\n')

#string testing
file_name = input("test file name: ")
if not file_name.endswith('.txt'):
    print("imma stop you here boi")
print('\n')

#string formating
time = 60
print("sorry, is this the {} minute thingy ma bob".format(time))
print('\n')

#using {:.2f} to limmit the number of floating point decimals 
# using {:>10s} this is used to aling text left or right or center, < > ^ respectivly 

for i in range(5):
    print("{:10d} --> {:4d}".format(i,i**2))

import math
print(math.pi)
print("pi but with a sigfig limit on it : {:.4f}".format(math.pi))



# finding letters in a word and listing the letter location
river = 'mississippi'
target = input("input a charaacter to find: ")
for index in range(len(river)):
    if river[index] == target:
        print("letter found at index {}".format(index))
        break
    else:
        print('letter', target, 'not found in index')

#split function
name  = 'John Marewood Clesse'
first, middle, last = name.split()
print(name)
print(first)
print(last)
transformed = last + ', '+first + ' '+middle
print(transformed)


#writing stuff in to a text file
temp_file = open("temp.txt","w")
print("first line", file=temp_file)
print("Second line but there is no third line", file=temp_file)
print("sike there is a thrid line", file=temp_file)
print("also a forth line", file=temp_file)
temp_file.close()

input_file = open("temp.txt", "r")
output_file = open("output_file.txt","w")
for line_str in input_file:
    new_str = ''
    line_str = line_str.strip()
    for char in line_str:
        new_str = char + new_str
        print(new_str,file=output_file)
        print('line : {:12s} reversed is: {:s}'.format(line_str, new_str))
input_file.close()
output_file.close()

temp_file2 = open("temp.txt", "r")
first_line_str = temp_file2.read(3)
print(first_line_str)
