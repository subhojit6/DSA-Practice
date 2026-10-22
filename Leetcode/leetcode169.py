nums = [3,3,4]

fre = {}
max_frequency = 0
majority_element = None

for num in nums:
    if num in fre:
        fre[num] += 1
    else:
        fre[num] = 1

for num, count in fre.items():
    if count > max_frequency:
        max_frequency = count
        majority_element = num

print(majority_element)

    