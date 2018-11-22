import re

def check_email(email):
    regex = r'\b[\w.-]+?@\w+?\.\w+?\b'
    match =  re.findall(regex, email)
    if match:
        return True
    return False