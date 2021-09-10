try:
    numerator = int(input("Enter the numerator: "))

    # added a while loop to achive question 3, avoiding the zero division error
    denominator =''
    while denominator != 't':
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("please enter a value (+ -) 0")
        else:
            break
    
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
    # 1) error vaule occures when a non numberical character is added into the fraction
except ZeroDivisionError:
    print("Cannot divide by zero!")
    # 2) zero division error will occure when the user trys to divide a number by zero
print("Finished.")