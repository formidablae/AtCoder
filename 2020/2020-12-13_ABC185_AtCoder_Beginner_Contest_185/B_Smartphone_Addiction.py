N, M, T = map(int, input().split())
in_cafe_times = [[0, 0]]
charge = N
for mline in range(M):
    A, B = map(int, input().split())
    in_cafe_times.append([A, B])
flag = True
for i in range(1, len(in_cafe_times)):
    charge = max(0, charge - (in_cafe_times[i][0] - in_cafe_times[i - 1][1]))
    # print("charge:", charge)
    if charge == 0:
        flag = False
        break
    charge = min(N, charge + (in_cafe_times[i][1] - in_cafe_times[i][0]))
    # print("charge:", charge)
if flag:
    charge = charge - (T - in_cafe_times[-1][1])
    # print("charge:", charge)
    if charge <= 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")