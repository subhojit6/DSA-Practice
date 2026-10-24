s = "abcabcbb"

left = 0
char_set = set()
max_length = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
    curr_length = right - left + 1
    if curr_length > max_length:
        max_length = curr_length
print(max_length)