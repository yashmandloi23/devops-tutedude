# Read from a File Program
# Opens a file in read mode and prints its contents

# Open file in read mode
file = open("output.txt", "r")

# Read content from file
content = file.read()

# Print content
print("File Content:\n")
print(content)

# Close file
file.close()
print("File closed successfully.")