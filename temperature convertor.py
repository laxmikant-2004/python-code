def celsius_to_fahrenheit(c):
    # standard formula: multiply by 9/5 then add 32
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    # reverse of above formula
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    # kelvin is just celsius + 273.15
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = input("\nChoose conversion (1-6): ")

try:
    temp = float(input("Enter temperature value: "))

    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")

    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")

    elif choice == "3":
        # kelvin can't be negative
        if celsius_to_kelvin(temp) < 0:
            print("That would give negative Kelvin which doesn't exist!")
        else:
            result = celsius_to_kelvin(temp)
            print(f"{temp}°C = {result:.2f} K")

    elif choice == "4":
        if temp < 0:
            print("Kelvin can't be negative!")
        else:
            result = kelvin_to_celsius(temp)
            print(f"{temp} K = {result:.2f}°C")

    elif choice == "5":
        # convert F to C first then to K
        celsius = fahrenheit_to_celsius(temp)
        result = celsius_to_kelvin(celsius)
        print(f"{temp}°F = {result:.2f} K")

    elif choice == "6":
        if temp < 0:
            print("Kelvin can't be negative!")
        else:
            celsius = kelvin_to_celsius(temp)
            result = celsius_to_fahrenheit(celsius)
            print(f"{temp} K = {result:.2f}°F")

    else:
        print("Invalid choice!")

except ValueError:
    print("Enter a valid temperature number please.")