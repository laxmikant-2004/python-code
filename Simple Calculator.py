def show_menu():
    print("\n Simple Calculator ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Pick an option (1-5): ")

    if choice == "5":
        print("Bye!")
        break

    # make sure user typed a valid number
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except ValueError:
        print("That's not a valid number, try again.")
        continue

    if choice == "1":
        result = num1 + num2
        print(f"Answer: {num1} + {num2} = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"Answer: {num1} - {num2} = {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"Answer: {num1} * {num2} = {result}")

    elif choice == "4":
        # can't divide by zero, so check that first
        if num2 == 0:
            print("Error: Can't divide by zero!")
        else:
            result = num1 / num2
            print(f"Answer: {num1} / {num2} = {result:.4f}")

    else:
        print("Invalid choice, pick 1 to 5.")
