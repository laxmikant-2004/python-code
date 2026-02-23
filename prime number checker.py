def check_prime(n):
    # 1 and below are not prime by definition
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not prime
    if n % 2 == 0:
        return False

    # only need to check divisors up to square root of n
    # this makes it faster than checking all numbers up to n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # jump by 2 since we already handled even numbers

    return True

def primes_in_range(start, end):
    # collect all primes between start and end
    prime_list = []
    for num in range(start, end + 1):
        if check_prime(num):
            prime_list.append(num)
    return prime_list

print("Prime Number Checker")
print("1. Check if a number is prime")
print("2. Find all primes in a range")

choice = input("\nChoose (1 or 2): ")

try:
    if choice == "1":
        num = int(input("Enter a number: "))
        if check_prime(num):
            print(f"\n{num} IS a prime number.")
            # find next prime after this one
            next_num = num + 1
            while not check_prime(next_num):
                next_num += 1
            print(f"Next prime after {num} is {next_num}")
        else:
            print(f"\n{num} is NOT a prime number.")
            if num > 1:
                # find factors to show why it's not prime
                factors = [i for i in range(2, num) if num % i == 0]
                print(f"Its factors include: {factors[:5]}")  # show first 5 factors

    elif choice == "2":
        range_start = int(input("Start of range: "))
        range_end = int(input("End of range: "))

        if range_start > range_end:
            print("Start must be less than end!")
        else:
            found_primes = primes_in_range(range_start, range_end)
            print(f"\nPrimes between {range_start} and {range_end}:")
            print(found_primes)
            print(f"Total count: {len(found_primes)}")
    else:
        print("Invalid choice.")

except ValueError:
    print("Please enter valid whole numbers.")