def modify_content(content):
    """
    Modify the file content in some way.
    Here, we'll make all text uppercase.
    You can change this to any transformation you want.
    """
    return content.upper()


try:
    # Ask user for filename
    input_file = input("Enter the filename to read: ")

    # Read the file content
    with open(input_file, "r") as file:
        content = file.read()

    # Modify the content
    modified_content = modify_content(content)

    # Write to a new file
    output_file = "modified_" + input_file
    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"File successfully read and modified! New file saved as '{output_file}'.")

except FileNotFoundError:
    print("Error: The file was not found. Please check the filename and try again.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
