def clean_string(text):
    # remove spaces and punctuation, make lowercase
    # so "A man a plan a canal Panama" also works
    cleaned = ""
    for char in text:
        if char.isalnum():  # keep only letters and numbers
            cleaned += char.lower()
    return cleaned

def is_palindrome(text):
    cleaned = clean_string(text)
    # reverse and compare
    return cleaned == cleaned[::-1]

print("Palindrome Checker")
print("Works for words, sentences, and numbers.\n")

while True:
    user_input = input("Enter text (or 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        print("Bye!")
        break

    if len(user_input) == 0:
        print("Please type something!")
        continue

    # check and give result
    cleaned_version = clean_string(user_input)

    if is_palindrome(user_input):
        print(f'  "{user_input}" IS a palindrome!')
        print(f'  (After cleaning: "{cleaned_version}")')
    else:
        print(f'  "{user_input}" is NOT a palindrome.')
        # show what it looks like reversed
        print(f'  Reversed: "{cleaned_version[::-1]}"')

    print()