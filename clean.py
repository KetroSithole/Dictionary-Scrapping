input_file_path = "Dictionary.txt"
output_file_path = "clean.txt"

# Open the input file in read mode
with open(input_file_path, "r", encoding="utf-8") as input_file:
    # Read the content of the input file
    content = input_file.readlines()

# Add hyphen at the beginning of lines if it doesn't exist
modified_content = ["-" + line if not line.strip().startswith("-") else line for line in content]

# Open the output file in write mode
with open(output_file_path, "w", encoding="utf-8") as output_file:
    # Write the modified content to the output file
    output_file.writelines(modified_content)

print(f"Modification complete. Check the '{output_file_path}' file.")
