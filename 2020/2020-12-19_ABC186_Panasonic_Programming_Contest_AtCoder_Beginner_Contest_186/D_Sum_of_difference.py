# import numpy as np
#
# N = int(input())
# integs = list(map(int, input().split()))
# integs.sort(reverse=True)
# summat_matrix = np.zeros((N - 1, N - 1), dtype=int)
# for i in reversed(range(N - 1)):
#     for j in range(i, N - 1):
#         if j == N - 2 and i == j:
#             summat_matrix[i][j] = integs[i] - integs[i + 1]
#         elif i == j:
#             summat_matrix[i][j] = integs[i] - integs[i + 1] + summat_matrix[i][j + 1]
#         else:
#             summat_matrix[i][j] = summat_matrix[i][j - 1] + summat_matrix[j][j]
# print(summat_matrix.sum())
#
# N = int(input())
# integs = list(map(int, input().split()))
# summat = 0
# for i in range(N):
#     for j in range(i + 1, N):
#         summat += abs(integs[i] - integs[j])
# print(summat)