ransomNote = "aa"
magazine = "aab"

seen = {}

for i in range(len(magazine)):
    if magazine[i] in seen:
        seen[magazine[i]] += 1
    else:
        seen[magazine[i]] = 1

for i in range(len(ransomNote)):
    if ransomNote[i] not in seen:
        print(False)
        break
    elif seen[ransomNote[i]] == 0:
        print(False)
        break
    else:
        seen[ransomNote[i]] -= 1
else:
    print(True)



