def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"successfully wrote to {filename}")
    except PermissionError:
        print("Error: Insufficient permission to write to the file.")
    except Exception as e:
         print(f"An error occurred: {e}")

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"contents of {filename}: \n{content}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
        print(f"Successfully appended to {filename}")
    except PermissionError:
        print("Error: Insufficient permission to append to the file.")
    except Exception as e:
        print(print(f"An error occurred: {e}"))



# File creation
write_to_file("my_file.txt", "This is the first line.\n")
write_to_file("my_file.txt", "Here's some more text with a number: 42\n")
write_to_file("my_file.txt", "The last line for initial content.\n")

# File reading
read_from_file("my_file.txt")

# File appending
append_to_file("my_file.txt", "\nAppended line 1.\n")
append_to_file("my_file.txt", "Appended line 2 with another number: 100\n")
append_to_file("my_file.txt", "Final appended line.\n")

# Read again to show appended content
read_from_file("my_file.txt")
