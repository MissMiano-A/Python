# File Read & Write Challenge with Error Handling

# Ask user for the input file name
filename = input("Enter the file name you want to read: ")

try:
    # Try to open the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write the modified content into a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Done! Modified content saved in '{new_filename}'.")

except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print("Something went wrong:", e)
