# LeetCode #733 - Flood Fill (BFS, avoids Python's recursion limit)
from collections import deque


def flood_fill(image, sr, sc, color):
    old = image[sr][sc]
    if old == color:
        return image
    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    image[sr][sc] = color
    while queue:
        r, c = queue.popleft()
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == old:
                image[nr][nc] = color
                queue.append((nr, nc))
    return image


if __name__ == '__main__':
    print(flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
    # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    print(flood_fill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))  # unchanged
