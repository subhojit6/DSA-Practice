def is_palindrome(word):

    # Base case
    if len(word) <= 1:
        return True

    # Compare first and last chars
    if word[0] != word[-1]:
        return False

    # Check the reamining middle portions
    return is_palindrome(word[1:-1])

print(is_palindrome("madam"))
print(is_palindrome("racecar"))