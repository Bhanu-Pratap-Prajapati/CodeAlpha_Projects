import re

# Input and output files
input_file = "data.txt"
output_file = "emails.txt"

# Pattern for email extraction
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Read file content
with open(input_file, "r",encoding="utf-8") as file:
    text = file.read()

# Find all emails
emails = re.findall(email_pattern, text)

# Write to output file
with open(output_file, "w",encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

print("✔ Email extraction complete! Saved to emails.txt")
