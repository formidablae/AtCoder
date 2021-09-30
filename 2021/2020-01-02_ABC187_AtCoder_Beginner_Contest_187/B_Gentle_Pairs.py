N = int(input())
points = []
for tc in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
count = 0
for i in range(N):
    for j in range(i + 1, N):
        xdiff = points[i][0] - points[j][0]
        ydiff = points[i][1] - points[j][1]
        slope = ydiff / xdiff
        # print(xdiff)
        # print(ydiff)
        # print(slope)
        if -1 <= slope <= 1:
            count += 1
print(count)