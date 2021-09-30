H, W = map(int, input().split())
grid = []
blocks_to_rem = 0
for tc in range(H):
    grid = grid + list(map(int, input().split()))
minim = min(grid)
for elem in grid:
    blocks_to_rem += elem - minim
print(blocks_to_rem)
