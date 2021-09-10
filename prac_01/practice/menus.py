user_name = str(input("what is your name my child? :"))
print("here are some options:")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice =0
while choice != 'Q':
    choice = str(input(">> "))
    if choice == 'H':
        print("hello "+user_name)
    elif choice == 'G':
        print("Goodbye "+user_name)
    elif choice =='Q':
        print('FINISHED')
        break
    else:
        print("invalde choice please try again")