def decimal_to_binary(n):
    if n == 0:
        return "0"
    # keep dividing by 2 and collect remainders
    binary_digits = []
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        binary_digits.append(str(n % 2))
        n //= 2
    binary_str = "".join(reversed(binary_digits))
    return ("-" + binary_str) if is_negative else binary_str

def decimal_to_octal(n):
    if n == 0:
        return "0"
    # same idea but divide by 8
    octal_digits = []
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        octal_digits.append(str(n % 8))
        n //= 8
    octal_str = "".join(reversed(octal_digits))
    return ("-" + octal_str) if is_negative else octal_str

def decimal_to_hex(n):
    # hex digits go 0-9 then A-F
    hex_chars = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hex_digits = []
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        hex_digits.append(hex_chars[n % 16])
        n //= 16
    hex_str = "".join(reversed(hex_digits))
    return ("-" + hex_str) if is_negative else hex_str

def binary_to_decimal(binary_str):
    # each position is a power of 2 from right to left
    try:
        decimal_val = 0
        power = 0
        for bit in reversed(binary_str):
            if bit not in "01":
                raise ValueError("Not a valid binary number")
            decimal_val += int(bit) * (2 ** power)
            power += 1
        return decimal_val
    except:
        return None

def show_all_conversions(decimal_num):
    print(f"\n  Decimal     : {decimal_num}")
    print(f"  Binary      : {decimal_to_binary(decimal_num)}")
    print(f"  Octal       : {decimal_to_octal(decimal_num)}")
    print(f"  Hexadecimal : {decimal_to_hex(decimal_num)}")
    # also using python's built in just to verify
    print(f"\n  (Verified using Python built-ins)")
    print(f"  bin({decimal_num}) = {bin(decimal_num)}")
    print(f"  oct({decimal_num}) = {oct(decimal_num)}")
    print(f"  hex({decimal_num}) = {hex(decimal_num)}")

print("Number System Converter")
print("1. Decimal to Binary/Octal/Hex")
print("2. Binary to Decimal")
print("3. Octal to Decimal")
print("4. Hex to Decimal")
print("5. Show table (decimal 0-20 in all systems)")

choice = input("\nChoose (1-5): ")

try:
    if choice == "1":
        num = int(input("Enter decimal number: "))
        show_all_conversions(num)

    elif choice == "2":
        binary_input = input("Enter binary number (only 0s and 1s): ").strip()
        result = binary_to_decimal(binary_input)
        if result is None:
            print("Invalid binary number! Only 0 and 1 are allowed.")
        else:
            print(f"Binary {binary_input} = Decimal {result}")

    elif choice == "3":
        octal_input = input("Enter octal number: ").strip()
        try:
            result = int(octal_input, 8)  # base 8 conversion
            print(f"Octal {octal_input} = Decimal {result}")
        except ValueError:
            print("Invalid octal number!")

    elif choice == "4":
        hex_input = input("Enter hexadecimal number (e.g. 1F, A3): ").strip()
        try:
            result = int(hex_input, 16)  # base 16 conversion
            print(f"Hex {hex_input.upper()} = Decimal {result}")
        except ValueError:
            print("Invalid hexadecimal number!")

    elif choice == "5":
        print(f"\n{'Decimal':<10} {'Binary':<12} {'Octal':<10} {'Hex':<8}")
        print("-" * 42)
        for i in range(21):
            print(f"{i:<10} {decimal_to_binary(i):<12} {decimal_to_octal(i):<10} {decimal_to_hex(i):<8}")

    else:
        print("Invalid choice.")

except ValueError:
    print("Please enter a valid number.")