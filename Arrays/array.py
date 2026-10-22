import array

val = array.array('i',[1, 2, 3, 4, 5, 6])

for i in range(len(val) + 1):
    print(i, end=" ")

print("\n")

for i in val:
    print(i, end=", ")