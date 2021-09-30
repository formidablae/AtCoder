def dfs_is_connected(graph, u, v):
  stack      = []
  discovered = []
  stack.append(u)
  while stack:
    current_node = stack.pop()
    if v in graph[current_node] or current_node in graph[v]: return 1
    if current_node not in discovered:
      discovered.append(current_node)
      for connected_node in graph[current_node]:
        stack.append(connected_node)
  return 0
    
N, Q = map(int, input().split())
graph = []
for num in range(0, N):
  graph.append([])

for _ in range(Q):
  t, u, v = map(int, input().split())
  if t == 0:
    graph[u].append(v)
    graph[v].append(u)
  else: print(dfs_is_connected(graph, u, v))
