def count_words(text):
    # split on whitespace to get individual words
    words = text.split()
    return len(words)

def count_sentences(text):
    # count sentences by counting . ! and ? marks
    sentence_count = 0
    for char in text:
        if char in ".!?":
            sentence_count += 1
    # if no punctuation, assume whole thing is one sentence
    return sentence_count if sentence_count > 0 else 1

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_consonants(text):
    consonants_count = 0
    for char in text:
        # check it's a letter but not a vowel
        if char.isalpha() and char.lower() not in "aeiou":
            consonants_count += 1
    return consonants_count

def get_word_frequency(text):
    # count how many times each word appears
    word_freq = {}
    # remove punctuation and lowercase before counting
    words = text.lower().split()
    for word in words:
        clean_word = ""
        for ch in word:
            if ch.isalpha():
                clean_word += ch
        if clean_word:
            if clean_word in word_freq:
                word_freq[clean_word] += 1
            else:
                word_freq[clean_word] = 1
    return word_freq

def get_most_common_words(freq_dict, top_n=5):
    # sort by frequency descending and take top n
    sorted_words = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]

def average_word_length(text):
    words = text.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# get text from user
print("Text Analysis Tool")
print("Paste or type your text below. Press Enter twice when done.\n")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

full_text = " ".join(lines)

if len(full_text.strip()) == 0:
    print("No text entered!")
else:
    word_count = count_words(full_text)
    sentence_count = count_sentences(full_text)
    char_count = len(full_text)
    char_no_spaces = len(full_text.replace(" ", ""))
    vowel_count = count_vowels(full_text)
    consonant_count = count_consonants(full_text)
    avg_word_len = average_word_length(full_text)
    freq = get_word_frequency(full_text)
    top_words = get_most_common_words(freq, 5)

    print("\n--- Text Analysis Results ---")
    print(f"Characters (with spaces)    : {char_count}")
    print(f"Characters (without spaces) : {char_no_spaces}")
    print(f"Word Count                  : {word_count}")
    print(f"Sentence Count              : {sentence_count}")
    print(f"Vowels                      : {vowel_count}")
    print(f"Consonants                  : {consonant_count}")
    print(f"Average Word Length         : {avg_word_len:.2f} letters")
    print(f"Unique Words                : {len(freq)}")

    print(f"\nTop {len(top_words)} most common words:")
    for rank, (word, freq_count) in enumerate(top_words, 1):
        print(f"  {rank}. '{word}' - {freq_count} time(s)")

    # check if text is mostly uppercase or lowercase
    upper_chars = sum(1 for c in full_text if c.isupper())
    lower_chars = sum(1 for c in full_text if c.islower())
    if upper_chars > lower_chars:
        print("\nText is mostly UPPERCASE")
    else:
        print("\nText is mostly lowercase")