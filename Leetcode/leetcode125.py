s = "A man, a plan, a canal: Panama"
s = s.lower()

l = 0
r = len(s) - 1 

is_palindrome = True

while l < r:

    while l < r and not s[l].isalnum():
        l += 1

    while l < r and not s[r].isalnum():
        r -= 1

    if s[l] != s[r]:
        is_palindrome = False
        break
    else:
        l += 1
        r -= 1

print(is_palindrome)


