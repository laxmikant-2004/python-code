user_text = input("Type any sentence: ")

# just check the string isn't empty before doing anything
if len(user_text) == 0:
    print("You didn't type anything!")
else:
    print("\n--- String Operations ---")

    # uppercase version
    print(f"Uppercase     : {user_text.upper()}")

    # lowercase version
    print(f"Lowercase     : {user_text.lower()}")

    # title case - first letter of each word is capital
    print(f"Title Case    : {user_text.title()}")

    # reversed string - slice trick with [::-1]
    reversed_text = user_text[::-1]
    print(f"Reversed      : {reversed_text}")

    # count how many characters including spaces
    print(f"Total Chars   : {len(user_text)}")

    # count words by splitting on spaces
    word_list = user_text.split()
    print(f"Word Count    : {len(word_list)}")

    # replace spaces with underscore, like a slug
    slug_version = user_text.replace(" ", "_")
    print(f"With _ spaces : {slug_version}")

    # check if it's a palindrome (same forwards and backwards)
    # strip spaces and lowercase for a fair check
    cleaned = user_text.replace(" ", "").lower()
    if cleaned == cleaned[::-1]:
        print("Palindrome    : Yes!")
    else:
        print("Palindrome    : No")
