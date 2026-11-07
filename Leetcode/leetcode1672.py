accounts = [
    [1, 2, 3],
    [3, 2, 1]
    ]

richest = 0

for account in accounts:
    highest = 0
    for i in account:
        highest += i

    if highest > richest:
        richest = highest

print(richest)
