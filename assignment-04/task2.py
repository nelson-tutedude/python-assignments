# 1.   Takes user input and writes it to a file named output.txt.
user_input = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(user_input + '\n') 
print("Data successfully written to output.txt")

# 2.   Appends additional data to the same file.
additional_input = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write(additional_input + '\n')
print("Data successfully appended to output.txt")
    
# 3.   Reads and displays the final content of the file.
with open('output.txt', 'r') as file:
    print("Final content of output.txt:")
    for line in file:
        print(line.strip())
