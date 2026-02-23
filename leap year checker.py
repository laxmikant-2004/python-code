def is_leap_year(year):
    # century years like 100, 200 etc. need to be divisible by 400
    # other years just need divisible by 4
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        # divisible by 100 but not 400, so NOT a leap year
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

try:
    year_input = int(input("Enter a year to check: "))

    if year_input <= 0:
        print("Please enter a positive year.")
    else:
        if is_leap_year(year_input):
            print(f"{year_input} IS a leap year. (366 days)")
        else:
            print(f"{year_input} is NOT a leap year. (365 days)")

    # also show next few leap years from what user entered
    print("\nNext 5 leap years after that:")
    count = 0
    check_year = year_input + 1
    while count < 5:
        if is_leap_year(check_year):
            print(f"  {check_year}")
            count += 1
        check_year += 1

except ValueError:
    print("Please enter a valid whole number for the year.")