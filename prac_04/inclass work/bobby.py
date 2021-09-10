name = input("what is your name? : ")
vowels = ['a','e','i','o','u']
vowel_counter =0
for char in name.lower():
    if char in vowels:
        vowel_counter = vowel_counter + 1
print("{} has {} vowels".format(name,vowel_counter))
