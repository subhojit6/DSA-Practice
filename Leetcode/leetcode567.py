s1 = "ab"
s2 = "eidbaooo"


def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    left = 0
    ecount = {}
    win_count = {}

    for i in range(len(s1)):
        if s1[i] in ecount:
            ecount[s1[i]] += 1
        else:
            ecount[s1[i]] = 1

    for i in range(len(s1)):
        if s2[i] in win_count:
            win_count[s2[i]] += 1
        else:
            win_count[s2[i]] = 1

    if ecount == win_count:
        return True
    else:
        for right in range(len(s2) - len(s1)):
            win_count[s2[left]] -= 1
            if win_count[s2[left]] == 0:
                win_count.pop(s2[left])
            left += 1
            incoming = s2[right + len(s1)]
            if incoming in win_count:
                win_count[incoming] += 1
            else:
                win_count[incoming] = 1
            if win_count == ecount:
                return True
            
        return False

print(check_inclusion(s1, s2))