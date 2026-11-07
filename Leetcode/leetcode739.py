temperatures = [73,74,75,71,69,72,76,73]

result = [0] * len(temperatures)
stack = []

for i in range(len(temperatures)):
    while stack and temperatures[stack[-1]] < temperatures[i]:
        prev_day = stack.pop()
        result[prev_day] = i - prev_day
    stack.append(i)

print(result)
        
               