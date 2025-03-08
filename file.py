import os

def find_and_replace(filename, search_word, replace_word):
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Error: The file '{filename}' does not exist.")

        # Read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if the word exists in file
        if search_word not in content:
            print(f"'{search_word}' not found in the file. No changes made.")
            return

        # Replace word in file
        modified_content = content.replace(search_word, replace_word)

        # Write back to file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"Successfully replaced '{search_word}' with '{replace_word}' in '{filename}'.")
    except FileNotFoundError as e:
        print(e)
    except PermissionError:
        print("Error: Permission denied. Check file access permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# User input
filename = input("Enter the file name: ")
search_word = input("Enter the word to find: ")
replace_word = input("Enter the word to replace with: ")
find_and_replace(filename, search_word, replace_word)
