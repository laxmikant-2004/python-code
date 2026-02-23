def pattern_right_triangle(rows):
    # simple right angle triangle with numbers
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # move to next line after each row

def pattern_pyramid(rows):
    # star pyramid - centered
    for i in range(1, rows + 1):
        # spaces before stars to center it
        print(" " * (rows - i), end="")
        # print stars, using odd number formula
        print("* " * i)

def pattern_inverted_triangle(rows):
    # upside down triangle
    for i in range(rows, 0, -1):
        print("* " * i)

def pattern_number_pyramid(rows):
    # pyramid with numbers, centered
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def pattern_diamond(rows):
    # diamond shape - first go up then come down
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)

try:
    print("Number Pattern Printer")
    print("1. Right Triangle")
    print("2. Star Pyramid")
    print("3. Inverted Triangle")
    print("4. Number Pyramid")
    print("5. Diamond")

    choice = input("\nChoose pattern (1-5): ")
    rows = int(input("How many rows? "))

    if rows <= 0:
        print("Rows must be a positive number.")
    else:
        print()
        if choice == "1":
            pattern_right_triangle(rows)
        elif choice == "2":
            pattern_pyramid(rows)
        elif choice == "3":
            pattern_inverted_triangle(rows)
        elif choice == "4":
            pattern_number_pyramid(rows)
        elif choice == "5":
            pattern_diamond(rows)
        else:
            print("Invalid choice!")

except ValueError:
    print("Please enter a valid number for rows.")