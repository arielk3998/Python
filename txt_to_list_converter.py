while True:
    file_name = input("Enter file name: ")
    print()  # Adds a blank line after the file name input
    try:
        file_handle = open(file_name)
        break  # Exit the loop if the file is successfully opened
    except FileNotFoundError:
        print(f"File {file_name} not found. Please try again.")

count = 0
string_to_be_split = input(file_handle.read())
split_string_list = string_to_be_split.split()

for line in file_handle:
    count += 1
    print(line, end="")  # Replaces auto \n in print() with "" instead

file_handle.close()  # Close the file when done

print(f'''\n\nThere were {count} lines in {file_name}.''')
