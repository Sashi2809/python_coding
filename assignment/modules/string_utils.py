def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False