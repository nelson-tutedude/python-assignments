# 1.   Opens and reads a text file named sample.txt.
try:
    my_file = open('sample.txt', 'r')

# 2.   Prints its content line by line.
    print("Reading file content:")
    for line in my_file:
        print(line.strip())

# 3.   Handles errors gracefully if the file does not exist.            
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
