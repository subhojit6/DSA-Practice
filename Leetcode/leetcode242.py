s = "aab"
t = "abb"

seen = {}

is_anagram = True

for char in s:
    if char in seen:
        seen[char] += 1
    else:
        seen[char] = 1

for char in t:
    if char in seen:
        seen[char] -= 1
    else:
        is_anagram = False
        break

for key, value in seen.items():
    if value != 0:
        is_anagram = False
        break


print(is_anagram)


    
