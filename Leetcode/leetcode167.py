numbers = [2,7,11,15] 
target = 9

r = len(numbers) - 1
l = 0

while l < r:
    total = numbers[l] + numbers[r]

    if total == target:
        print(f"{l + 1}, {r + 1}")
        break
    elif numbers[l] + numbers[r] < target:
        l += 1
    else:
        r -= 1


        