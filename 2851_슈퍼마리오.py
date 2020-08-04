scores = []
for _ in range(10):
    scores.append(int(input()))

result = 0
for i in range(10):
    sum = 0
    for j in range(0, i + 1):
        sum += scores[j]
    if abs(sum - 100) == abs(100 - result) and sum > result:
        result = sum
    if abs(sum - 100) < abs(100 - result):
        result = sum
print(result)
