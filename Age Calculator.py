import datetime

# get today's date from the system
today = datetime.date.today()
current_year = today.year

try:
    birth_year = int(input("Enter your birth year (e.g. 2000): "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))

    # create a date object so we can do proper calculations
    birthday = datetime.date(birth_year, birth_month, birth_day)

    # make sure the date isn't in the future
    if birthday > today:
        print("That date is in the future, can't calculate age!")
    else:
        # calculate exact age
        age_in_years = current_year - birth_year
        # if birthday hasn't come yet this year, subtract 1
        if (today.month, today.day) < (birth_month, birth_day):
            age_in_years -= 1

        # find days lived total
        days_lived = (today - birthday).days

        print(f"\nYou are {age_in_years} years old")
        print(f"Months lived  : approximately {age_in_years * 12}")
        print(f"Days lived    : {days_lived}")
        print(f"Hours lived   : {days_lived * 24}")

        # next birthday calculation
        try:
            next_bday = datetime.date(current_year, birth_month, birth_day)
            if next_bday < today:
                next_bday = datetime.date(current_year + 1, birth_month, birth_day)
            days_to_bday = (next_bday - today).days
            print(f"Days to next birthday: {days_to_bday}")
        except ValueError:
            # feb 29 edge case for non-leap years
            print("(Next birthday calculation skipped - leap year date)")

except ValueError:
    print("Invalid input! Please enter proper numbers for the date.")