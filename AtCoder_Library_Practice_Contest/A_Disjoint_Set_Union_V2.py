N, Q = map(int, input().split())
groups = []

for _ in range(Q):
  t, u, v = map(int, input().split())
  if t == 0:
    if len(groups) == 0: groups.append([u, v])
    else:
      flagFound = False
      indexFound = -1
      ind = 0
      while ind < len(groups):
        if u in groups[ind] and v not in groups[ind]:
          flagFound = True
          if indexFound != -1 and indexFound != ind:
            groups[indexFound].append(v)
            for elem in groups[ind]:
              if elem not in groups[indexFound]:
                groups[indexFound].append(elem)
            groups.pop(ind)
          elif indexFound == -1:
            groups[ind].append(v)
            indexFound = ind
        elif v in groups[ind] and u not in groups[ind]:
          flagFound = True
          if indexFound != -1 and indexFound != ind:
            groups[indexFound].append(u)
            for elem in groups[ind]:
              if elem not in groups[indexFound]:
                groups[indexFound].append(elem)
            groups.pop(ind)
          elif indexFound == -1:
            groups[ind].append(u)
            indexFound = ind
        elif u in groups[ind] and v in groups[ind]:
          flagFound = True
          if indexFound != -1 and indexFound != ind:
            groups[indexFound].append(u)
            for elem in groups[ind]:
              if elem not in groups[indexFound]:
                groups[indexFound].append(elem)
            groups.pop(ind)
          elif indexFound == -1:
          	indexFound = ind
        ind = ind + 1
      if not flagFound: groups.append([u, v])
  else:
    flagConnect = False
    for group in groups:
      if u in group and v in group:
        print(1)
        flagConnect = True
        break
    if not flagConnect: print(0)
