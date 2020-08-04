scores = [[0] * 4] * 5
for i in range(5):
    scores[i] = list(map(int, input().split()))

winner, win_score = 0, 0
for i in range(5):
    score = sum(scores[i])
    if score > win_score:
        win_score = score
        winner = i
winner += 1
print(winner, win_score)