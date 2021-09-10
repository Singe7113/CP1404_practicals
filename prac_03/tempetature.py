import random

# gets and reads temperatures
def main():
    input_temp = file.readlines()
    temp_file = open("temps_output.txt","w")
    for x in range(len(input_temp)):
        temp = input_temp[x]
        print(temp)
        output_temp = temp_conversions(temp)
        print(output_temp)
        print("{} frahenhiet converteted to celcusis is {:.2f}".format(float(input_temp[x]),output_temp),file=temp_file)
    temp_file.close

# temperature conversion
def temp_conversions(temp):
    celsius =  float((float(temp) - 32) * 5 / 9)
    return celsius

# creates random temperatures to convert
def create_temp():
    number_of_temps = int(input("how many random temps do you want to make? : "))
    for x in range(number_of_temps):
        temp = random.randrange(-200,200)
        print("{}".format(temp),file=temp_file)

temp_file = open("temps_input.txt","a")
create_temp()
temp_file.close()

file = open("temps_input.txt","r")
main()
file.close