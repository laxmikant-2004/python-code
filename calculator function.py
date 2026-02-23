import math

# each operation is a separate function for clean code

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None  # can't divide by zero
    return a / b

def power(base, exp):
    return base ** exp

def square_root(n):
    if n < 0:
        return None  # can't take sqrt of negative (in real numbers)
    return math.sqrt(n)

def absolute_value(n):
    return abs(n)

def floor_division(a, b):
    if b == 0:
        return None
    return a // b

def modulo(a, b):
    if b == 0:
        return None
    return a % b

def logarithm(n, base=10):
    if n <= 0:
        return None  # log undefined for 0 and negative
    if base == 10:
        return math.log10(n)
    return math.log(n, base)

# menu display
def show_menu():
    print("\n--- Advanced Calculator ---")
    print("1.  Add")
    print("2.  Subtract")
    print("3.  Multiply")
    print("4.  Divide")
    print("5.  Power (a^b)")
    print("6.  Square Root")
    print("7.  Absolute Value")
    print("8.  Floor Division")
    print("9.  Modulo (remainder)")
    print("10. Logarithm (base 10)")
    print("11. Natural Log (base e)")
    print("0.  Exit")

while True:
    show_menu()
    choice = input("\nSelect operation: ")

    if choice == "0":
        print("Exiting calculator.")
        break

    try:
        # operations that need two numbers
        if choice in ["1", "2", "3", "4", "5", "8", "9"]:
            a = float(input("First number: "))
            b = float(input("Second number: "))

            if choice == "1":
                print(f"Result: {add(a, b)}")
            elif choice == "2":
                print(f"Result: {subtract(a, b)}")
            elif choice == "3":
                print(f"Result: {multiply(a, b)}")
            elif choice == "4":
                result = divide(a, b)
                if result is None:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"Result: {result:.6f}")
            elif choice == "5":
                print(f"Result: {a}^{b} = {power(a, b)}")
            elif choice == "8":
                result = floor_division(a, b)
                if result is None:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"Result: {int(a)} // {int(b)} = {result}")
            elif choice == "9":
                result = modulo(a, b)
                if result is None:
                    print("Error: Cannot mod by zero!")
                else:
                    print(f"Result: {a} % {b} = {result}")

        # operations needing just one number
        elif choice in ["6", "7", "10", "11"]:
            a = float(input("Enter number: "))

            if choice == "6":
                result = square_root(a)
                if result is None:
                    print("Error: Cannot take square root of a negative number!")
                else:
                    print(f"√{a} = {result:.6f}")
            elif choice == "7":
                print(f"|{a}| = {absolute_value(a)}")
            elif choice == "10":
                result = logarithm(a)
                if result is None:
                    print("Error: Log undefined for zero or negative numbers!")
                else:
                    print(f"log10({a}) = {result:.6f}")
            elif choice == "11":
                if a <= 0:
                    print("Error: Natural log undefined for zero or negative!")
                else:
                    print(f"ln({a}) = {math.log(a):.6f}")
        else:
            print("Invalid choice, try again.")

    except ValueError:
        print("Please enter valid numbers.")