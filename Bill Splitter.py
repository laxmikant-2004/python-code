try:
    total_bill = float(input("Enter the total bill amount (Rs): "))

    if total_bill <= 0:
        print("Bill amount should be more than zero.")
    else:
        num_people = int(input("How many people are splitting? "))

        if num_people <= 0:
            print("Number of people must be at least 1.")
        else:
            tip_percent = float(input("Enter tip percentage (e.g. 10 for 10%): "))

            # calculate the tip amount first
            tip_amount = (tip_percent / 100) * total_bill

            # total including tip
            grand_total = total_bill + tip_amount

            # each person's share
            share_per_person = grand_total / num_people

            print("\n--- Bill Summary ---")
            print(f"Original Bill  : Rs {total_bill:.2f}")
            print(f"Tip ({tip_percent}%)     : Rs {tip_amount:.2f}")
            print(f"Grand Total    : Rs {grand_total:.2f}")
            print(f"Each Person    : Rs {share_per_person:.2f}")

except ValueError:
    print("Please enter valid numbers only!")