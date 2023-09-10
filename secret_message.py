import random

# User input to create the dictionary
print("Enter word-count pairs (e.g., 'and: 22'). Type 'done' when finished.")
word_counts = {}
while True:
    input_line = input().strip()
    if input_line.lower() == 'done':
        break
    try:
        word, count = input_line.split(':')
        word = word.strip()
        count = int(count.strip())
        word_counts[word] = count
    except ValueError:
        print("Invalid input. Please use the format 'word: count'.")

# Create a list of words based on their frequencies
word_list = [word for word, count in word_counts.items() for _ in range(count)]

# Shuffle the word list to randomize the order
random.shuffle(word_list)

# Generate a sentence using the shuffled word list
generated_sentence = ' '.join(word_list)

# Print the generated sentence
print("Generated Sentence:")
print(generated_sentence)
