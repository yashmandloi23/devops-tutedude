# Write to a File Program

# Open file in write mode
file = open("output.txt", "w")

# Write content to file
file.write("Hello, this is a sample text file.\n")
file.write("This file was created for an test purpose")
file.write("new line in the end")

# Close the file
file.close()
print("file closed")