gain =  [-5, 1, 5, 0, -7]
#     gain[i + 1] = gain[i] + gain[i + 1]

# highest = 0

# for altitude in gain:
#     if altitude > highest and altitude > 0:
#         highest = altitude

# print(highest)

# for i in range(len(gain) - 1):
#     gain[i + 1] = gain[i] + gain[i + 1]

# highest = 0

# for altitude in gain:
#     if altitude > highest and altitude > 0:
#         highest = altitude

# print(highest)

altitude = 0
highest = 0

for change in gain:
    altitude += change
    if altitude > highest:
        highest = altitude

print(highest)
