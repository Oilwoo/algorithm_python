N = int(input())
scores = list(map(int, input().split()))

scores.sort()

result = scores[N - 1] - scores[0]

print(result)
