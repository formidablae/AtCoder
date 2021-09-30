A, B = map(int, input().split())
sumA = sum([int(d) for d in str(A)])
sumB = sum([int(d) for d in str(B)])
print(max(sumA, sumB))
