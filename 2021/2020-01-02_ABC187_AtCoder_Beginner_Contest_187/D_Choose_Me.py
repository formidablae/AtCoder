N = int(input())
towns = []
for tc in range(N):
    A, B = map(int, input().split())
    towns.append([A, B, A + B, A * 2 + B])

towns = sorted(towns, key=lambda x: x[3], reverse=True)
votes_aoki = 0
votes_takahashi = 0
for t in towns:
    votes_aoki += t[0]
count = 0
i = 0
while i < N and votes_takahashi <= votes_aoki:
    votes_aoki -= towns[i][0]
    votes_takahashi += towns[i][2]
    count += 1
    i += 1
print(count)