seat_prices = {
    "1": ("General", 100),
    "2": ("Silver", 150),
    "3": ("Gold", 200),
    "4": ("Platinum", 300)
}

print("=== Movie Ticket Booking ===\n")

try:
    age = int(input("Enter your age: "))

    if age <= 0 or age > 120:
        print("Please enter a valid age.")
    else:
        print("\nSeat Types:")
        for key, (name, price) in seat_prices.items():
            print(f"  {key}. {name} - Rs {price}")

        seat_choice = input("\nChoose seat type (1-4): ")

        if seat_choice not in seat_prices:
            print("Invalid seat choice!")
        else:
            seat_name, base_price = seat_prices[seat_choice]

            day_type = input("Is it a weekend? (yes/no): ").strip().lower()

            # weekend surcharge - 20% extra on weekends
            if day_type == "yes":
                weekend_extra = base_price * 0.20
            else:
                weekend_extra = 0

            # discount logic based on age
            if age < 5:
                discount_percent = 100  # toddlers get in free
                discount_label = "Free (Under 5)"
            elif age <= 12:
                discount_percent = 40  # kids discount
                discount_label = "Kids Discount (40%)"
            elif age >= 60:
                discount_percent = 30  # senior citizen discount
                discount_label = "Senior Citizen (30%)"
            else:
                discount_percent = 0
                discount_label = "No Discount"

            # calculate final price step by step
            price_after_weekend = base_price + weekend_extra
            discount_amount = price_after_weekend * (discount_percent / 100)
            final_price = price_after_weekend - discount_amount

            print("\n--- Ticket Summary ---")
            print(f"Seat Type     : {seat_name}")
            print(f"Base Price    : Rs {base_price}")
            if weekend_extra > 0:
                print(f"Weekend Extra : Rs {weekend_extra:.2f}")
            print(f"Discount      : {discount_label}")
            print(f"You Pay       : Rs {final_price:.2f}")

except ValueError:
    print("Invalid input! Enter numbers where required.")