import re

# Regex examples
# r”\d{3}-\d{3}-\d{4}”  This line of code matches U.S. phone numbers in the format 111-222-3333.
# r”^-?\d*(\.\d+)?$”  This line of code matches any positive or negative number, with or without decimal places.
# r”^[a-zA-Z0-9_]*$”  This line of code matches any alphanumeric string that contains no spaces.
# r”/^(.+)/([^/]+)$/” This line of code matches any path and filename.

def check_character_groups(text):
  result = re.search(r"\w+\s\w+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


