
MENU ="""
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_calc()
            choice = input(">>> ").upper()
        elif choice == "F":
            fahrenheit_calc()
            choice = input(">>> ").upper()
        else:
            invalid(MENU)
            choice = input(">>> ").upper()
    print("Thank you.")

def celsius_calc():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))

def fahrenheit_calc():
    fahrenheit = float(input("fahrenheit: "))
    celsius =  (fahrenheit - 32) * 5 / 9
    print("Result: {:.2f} C".format(celsius))

def invalid(MENU,choice):
    print("Invalid option")
    print(MENU)
    return choice

main()