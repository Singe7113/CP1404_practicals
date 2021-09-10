minimum = int(input("what is the minimum number or x value? :"))
maximum = int(input("what is the largest or y value? : "))
print("--------- please choose one of the following options ----------")
print("1) Show the even numbers from x to y")
print("2) Show the odd numbers from x to y")
print("3) Show the squares from x to y")
print("4) Exit the program")
choice =0
while choice != '4':
    choice = str(input(">> "))
    if choice == '1':
        print("Showing all the even numbers from %s to %s"%(minimum,maximum))
        if (minimum/2) == True:
            print("he even")
            for i in range(minimum, maximum, 2):
                print(i, end=' ')
            print()
        else:
            print("he odd")
            for i in range(minimum+1, maximum, 2):
                print(i, end=' ')
            print()
    elif choice == '2':
        print("Showing all the odd numbers from %s to %s"%(minimum,maximum))
        if (minimum/2) == True:
            print("he even")
            for i in range(minimum+1, maximum, 2):
                print(i, end=' ')
            print()
        else:
            print("he odd")
            for i in range(minimum, maximum, 2):
                print(i, end=' ')
            print()
    elif choice =='3':
        print("Showing all the square from %s to %s"%(minimum,maximum))
        for i in range(minimum, maximum, 1):
            print((i*i), end=' ')
        print()
    elif choice =='4':
        print('Program terminated')
        break
    else:
        print("invalde choice please try again")