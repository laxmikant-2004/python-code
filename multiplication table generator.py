try:
    print("Multiplication Table Generator")
    choice = input("Do you want table for one number or a range? (one/range): ").strip().lower()

    if choice == "one":
        number = int(input("Enter the number: "))
        upto = int(input("Show table up to (default 10): ") or "10")

        print(f"\n--- Table of {number} ---")
        for multiplier in range(1, upto + 1):
            product = number * multiplier
            # align numbers nicely with formatting
            print(f"  {number:3} x {multiplier:3} = {product:5}")

    elif choice == "range":
        start_num = int(input("Start from which number? "))
        end_num = int(input("End at which number? "))
        upto = int(input("Show each table up to (default 10): ") or "10")

        if start_num > end_num:
            print("Start number should be less than end number.")
        else:
            for number in range(start_num, end_num + 1):
                print(f"\n--- Table of {number} ---")
                for multiplier in range(1, upto + 1):
                    product = number * multiplier
                    print(f"  {number:3} x {multiplier:3} = {product:5}")

    else:
        print("Please type 'one' or 'range'.")

except ValueError:
    print("Please enter valid whole numbers.")