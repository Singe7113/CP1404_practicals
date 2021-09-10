import random
def main():
    
    number_of_temps = int(input("how many random temps do you want to make? : "))
    for x in range(number_of_temps):
        temp = random.randrange(-200,200)
        print("{}".format(temp),file=temp_file)

temp_file = open("temps_input.txt","a")
main()
temp_file.close()