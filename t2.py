while True:
    try:
        number1 = float(input("Enter number1: "))
        number2 = float(input("Enter number2: "))
        choice = input("Enter operation\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Mod\n6. Exit\n")

        if choice == '1':
            print("Addition of n1 and n2 =", number1 + number2)
        elif choice == '2':
            print("Subtraction of n1 and n2 =", number1 - number2)
        elif choice == '3':
            print("Multiplication of n1 and n2 =", number1 * number2)
        elif choice == '4':
            if number2 != 0:
                print("Division of n1 and n2 =", number1 / number2)
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
            if number2 != 0:
                print("Mod of n1 and n2 =", number1 % number2)
            else:
                print("Error: Modulo by zero is not allowed.")
        elif choice == '6':
            print("Program terminated\n")
            break
        else:
            print("Invalid operation. Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
