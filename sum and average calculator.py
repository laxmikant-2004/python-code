print("Sum and Average Calculator")
print("Enter numbers one by one. Type 'done' when finished.\n")

numbers_list = []

while True:
    user_input = input(f"Enter number {len(numbers_list) + 1} (or 'done'): ").strip()

    if user_input.lower() == "done":
        # stop collecting when user says done
        break

    try:
        num = float(user_input)
        numbers_list.append(num)
    except ValueError:
        print("That's not a valid number, try again.")

# need at least one number to calculate anything
if len(numbers_list) == 0:
    print("You didn't enter any numbers!")
else:
    total_sum = sum(numbers_list)
    average = total_sum / len(numbers_list)
    largest = max(numbers_list)
    smallest = min(numbers_list)
    count = len(numbers_list)

    # find how many are positive and negative
    positive_count = len([n for n in numbers_list if n > 0])
    negative_count = len([n for n in numbers_list if n < 0])

    print(f"\n--- Results ---")
    print(f"Numbers entered : {count}")
    print(f"Sum             : {total_sum}")
    print(f"Average         : {average:.2f}")
    print(f"Largest         : {largest}")
    print(f"Smallest        : {smallest}")
    print(f"Positive count  : {positive_count}")
    print(f"Negative count  : {negative_count}")

    # show sorted version too
    sorted_nums = sorted(numbers_list)
    print(f"Sorted (asc)    : {sorted_nums}")