def organize_contacts(contact_list):
    # Your solution here
    
    # 1. Create helper functions for validation
    # - Function to validate email format
    # - Function to clean and validate phone numbers
    
    # 2. Process each contact
    # - Clean email (lowercase) and phone (digits only)
    # - Check if email and phone are valid
    # - Check for duplicates
    
    # 3. Return the clean contact list
'''
Create a function named organize_contacts that processes a list of contact dictionaries to create a clean contact database.

Each contact dictionary in the input list has these keys:

    name: The person's name
    email: The person's email address
    phone: The person's phone number

Your function should:

    Remove duplicate contacts (contacts with the same email or phone number)
    Standardize all emails to lowercase
    Filter out contacts with invalid email addresses
    Filter out contacts with invalid phone numbers
    Return a list of cleaned contact dictionaries

Validation rules:

    Valid email: Must contain '@' and '.', and must not have spaces
    Valid phone: Must contain exactly 10 digits (ignore non-digit characters like dashes or parentheses)

For cleaning phone numbers, you should use Python's str.isdigit() method to extract only the numeric digits from phone numbers. This method returns True if a character is a digit (0-9) and False otherwise, making it perfect for filtering out non-digit characters.
Example Input:

contacts = [
    {"name": "John Doe", "email": "john@email.com", "phone": "123-456-7890"}
]

Expected Output:

[
    {"name": "John Doe", "email": "john@email.com", "phone": "1234567890"}
]
'''    
name_input=input()
email_input=str(input())
phone_input =int(input())
contact_list={
    name="name_input"
    email="email_input"
    phone="phone_input"

}
print(type(contact_list))
print(contact_list)