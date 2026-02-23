def calculate_factorial(n):
    # factorial of 0 is 1 by definition (mathematical convention)
    if n == 0:
        return 1

    result = 1
    # multiply from 1 up to n
    for i in range(1, n + 1):
        result *= i
    return result

def show_factorial_steps(n):
    # show the actual calculation like 5! = 5 x 4 x 3 x 2 x 1 = 120
    if n == 0:
        return "0! = 1"

    steps = " x ".join(str(i) for i in range(n, 0, -1))
    return f"{n}! = {steps} = {calculate_factorial(n)}"

try:
    number = int(input("Enter a number to find factorial: "))

    if number < 0:
        print("Factorial is not defined for negative numbers!")
    elif number > 20:
        # numbers above 20 get really huge, still calculable but show warning
        print(f"Warning: {number}! is a very large number")
        fact = calculate_factorial(number)
        print(f"{number}! = {fact}")
    else:
        print(f"\nStep by step:")
        print(show_factorial_steps(number))

        # also show factorials of all numbers from 0 to n
        print(f"\nFactorials from 0 to {number}:")
        for i in range(0, number + 1):
            print(f"  {i}! = {calculate_factorial(i)}")

except ValueError:
    print("Please enter a whole number only.")