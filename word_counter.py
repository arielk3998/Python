import string
from collections import Counter

def tokenize_and_clean(text):
    translator = str.maketrans('', '', string.punctuation)
    words = text.split()
    cleaned_words = [word.translate(translator) for word in words if word.isalpha()]
    return cleaned_words

def analyze_text(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as read_file_handle:
            string_to_be_split = read_file_handle.read()
            word_tokens = tokenize_and_clean(string_to_be_split)

            word_count = Counter(word_tokens)
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

            count_of_words = len(word_tokens)
            unique_words_count = len(word_count)

            print(f"Total words: {count_of_words}")
            print(f"Unique words: {unique_words_count}")

            count_of_lines = string_to_be_split.count('\n') + 1

            print("\nSorted Unique Words and Their Counts:")
            for word, count in sorted_word_count:
                print(f"{word}: {count}")

            print(f"\nThere were {count_of_lines} lines in {file_name}.")

    except FileNotFoundError:
        print(f"File {file_name} not found. Please try again.")
    except UnicodeDecodeError:
        print("Error: Unable to decode the file with UTF-8 encoding.")

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    analyze_text(file_name)
