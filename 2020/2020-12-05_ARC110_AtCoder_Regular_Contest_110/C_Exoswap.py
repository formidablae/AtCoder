# N = int(input())
# perm = list(map(int, input().split()))
# if N == 2:
#     if perm[0] > perm[1]:
#         print(1)
#     else:
#         print(-1)
# else:
#     swaps = []
#     smallest = 1
#     biggest = N
#     i = 0
#     for num in range(1, N + 1):
#         smallest, biggest = min(perm[smallest - 1 + i: biggest - i]), max(perm[smallest - 1 + 1: biggest - 1])
#         index_smallest = perm.index(smallest)
#         index_biggest = perm.index(biggest)
#         while index_smallest != smallest - 1:
#             perm[index_smallest], perm[index_smallest - 1] = perm[index_smallest - 1], perm[index_smallest]
#             if index_smallest + 1 in swaps:
#                 print(-1)
#                 break
#             else:
#                 swaps.append(index_smallest + 1)
#
#             if len(swaps) > N - 1:
#                 print(-1)
#                 break
#         while index_biggest != biggest - 1:
#             perm[index_biggest], perm[index_biggest + 1] = perm[index_biggest + 1], perm[index_biggest]
#             if index_biggest + 1 in swaps:
#                 print(-1)
#                 break
#             else:
#                 swaps.append(index_biggest + 1)
#
#             if len(swaps) > N - 1:
#                 print(-1)
#                 break
#             i += 1
#
#     if len(swaps) > N - 1:
#         print(-1)
#         break
#     elif i == N - 1:
#         print(*swaps, sep='\n')
#         break
