s = "(())"

pairs = {")" : "(",
         "]" : "[",
         "}" : "{"
         }

stack = []

for char in s:
    if char not in pairs:
        stack.append(char)

    elif stack:
        if stack[-1] == pairs[char]:
            stack.pop()
        else:
            print(False)
            break
    else:
        print(False)
        break
if stack:
    print(False)
else:
    print(True)

        
