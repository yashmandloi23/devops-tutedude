# Write to a File Program
# Creates a text file and writes content using open() and write()

# Open file in write mode (creates file if it doesn't exist)
file = open("output.txt", "w")

# Write content to file
file.write("Hello, this is a sample text file.\n")
file.write("This file was created using Python file handling.\n")
file.write("Learning file operations is important.\n")

# Close the file
file.close()

print("Content written successfully to output.txt")
