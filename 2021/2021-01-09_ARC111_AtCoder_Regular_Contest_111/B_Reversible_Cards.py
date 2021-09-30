# N = int(input())
# comb = []
# max_length = 0
# for row in range(N):
#     a, b = map(int, input().split())
#     if len(comb) == 0:
#         comb.append(set([a]))
#         comb.append(set([b]))
#     else:
#         i = 0
#         dim = len(comb)
#         while i < min(dim, len(comb)):
#             if a in comb[i] and b not in comb[i]:
#                 comb[i].add(b)
#                 max_length = max(max_length, len(comb[i]))
#                 if len(comb[i]) < max_length:
#                     comb.pop(i)
#                     i -= 1
#             elif a not in comb[i] and b in comb[i]:
#                 comb[i].add(a)
#                 max_length = max(max_length, len(comb[i]))
#                 if len(comb[i]) < max_length:
#                     comb.pop(i)
#                     i -= 1
#             elif a in comb[i] and b in comb[i]:
#                 max_length = max(max_length, len(comb[i]))
#                 if len(comb[i]) < max_length:
#                     comb.pop(i)
#                     i -= 1
#             else:
#                 newset = comb[i].copy()
#                 comb[i].add(a)
#                 newset.add(b)
#                 max_length = max(max_length, len(comb[i]))
#                 if len(comb[i]) < max_length:
#                     comb.pop(i)
#                     i -= 1
#                 max_length = max(max_length, len(newset))
#                 if len(newset) == max_length:
#                     comb.append(newset)
#             i += 1
#             if 0 < i < min(dim, len(comb)) and comb[i - 1] == comb[i]:
#                 comb.pop(i)
#     # print(comb)
# print(max_length)
