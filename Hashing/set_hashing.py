nums = [5, 2, 8, 2, 9, 5, 1]

seen = set()

for num in nums:
    if num in seen:
        print("Duplicate found:", num)
        break

    seen.add(num)