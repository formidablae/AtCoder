# class Tree:
#     def __init__(self, x):
#         self.val = x
#         self.c = 0
#         self.children = None
#         self.edges = None
#
#     def __str__(self):
#         ans = str(self.val) + " "
#         if self.children is not None:
#             for c in self.children:
#                 ans += str(c)
#         return ans
#
#     def str_c(self):
#         return str(self.c)
#
#     def search_by_key(self, key):
#         # Base Cases: root is null or key is present at root
#         if self is None or self.val == key:
#             return self
#
#         if self.children is not None:
#             for child_c in self.children:
#                 answ = child_c.search_by_key(key)
#                 if answ is not None:
#                     return answ
#         else:
#             return None
#
#     def search_edge(self, key):
#         # Base Cases: root is null or key is present at root
#         if self.edges is None:
#             return None
#
#         for ed in self.edges:
#             if ed[0] == key:
#                 return ed
#
#         if self.children is not None:
#             for child_c in self.children:
#                 answ = child_c.search_edge(key)
#                 if answ is not None:
#                     return answ
#         else:
#             return None
#
#
# def increment_c(strtvert, dntrch, x_incr):
#     if strtvert is not None:
#         strtvert.c += x_incr
#     if strtvert is not None and strtvert.children is not None:
#         for chld in strtvert.children:
#             if chld != dntrch:
#                 increment_c(chld, dntrch, x_incr)
#
#
# tree = Tree(None)
# vertexlist = []
# N = int(input())
# for tc in range(N - 1):
#     a, b = map(int, input().split())
#     a_nodepresent = tree.search_by_key(a)
#     b_nodepresent = tree.search_by_key(b)
#     if a_nodepresent is not None:
#         if b_nodepresent is not None:
#             child = b_nodepresent
#             if a_nodepresent.children is not None:
#                 a_nodepresent.children.append(child)
#             else:
#                 a_nodepresent.children = [child]
#             if a_nodepresent.edges is not None:
#                 a_nodepresent.edges.append((tc + 1, a_nodepresent, child))
#             else:
#                 a_nodepresent.edges = [(tc + 1, a_nodepresent, child)]
#         else:
#             child = Tree(b)
#             vertexlist.append(child)
#             if a_nodepresent.children is not None:
#                 a_nodepresent.children.append(child)
#             else:
#                 a_nodepresent.children = [child]
#             if a_nodepresent.edges is not None:
#                 a_nodepresent.edges.append((tc + 1, a_nodepresent, child))
#             else:
#                 a_nodepresent.edges = [(tc + 1, a_nodepresent, child)]
#     else:
#         if b_nodepresent is not None:
#             child = Tree(a)
#             vertexlist.append(child)
#             if b_nodepresent.children is not None:
#                 b_nodepresent.children.append(child)
#             else:
#                 b_nodepresent.children = [child]
#             if b_nodepresent.edges is not None:
#                 b_nodepresent.edges.append((tc + 1, a_nodepresent, child))
#             else:
#                 b_nodepresent.edges = [(tc + 1, a_nodepresent, child)]
#             tree = b_nodepresent
#         else:
#             tree = Tree(a)
#             child = Tree(b)
#             vertexlist.append(tree)
#             vertexlist.append(child)
#             tree.children = [child]
#             if tree.edges is not None:
#                 tree.edges.append((tc + 1, tree, child))
#             else:
#                 tree.edges = [(tc + 1, tree, child)]
# print(vertexlist)
# Q = int(input())
# for q in range(Q):
#     t, e, x_val = map(int, input().split())
#     edge = tree.search_edge(e)
#     if t == 1:
#         startvertex = edge[1]
#         dontreach = edge[2]
#         increment_c(startvertex, dontreach, x_val)
#     else:
#         startvertex = edge[2]
#         dontreach = edge[1]
#         increment_c(startvertex, dontreach, x_val)
# for vert in vertexlist:
#     print(vert.str_c())
