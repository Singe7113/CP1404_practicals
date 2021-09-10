import string
def alphabetcial_shnagans():
    string_to_test = input("please type something for my will to live: ")
    list_of_letters = string.ascii_lowercase
    count =0
    for x in len(string_to_test):
        for char in string_to_test:
            if char in list_of_letters:
                count=+1
    print(str(count))

alphabetcial_shnagans()
