# Custom practice: fewest reporting links between two people (BFS)
from collections import defaultdict, deque


def distance(pairs, start, target):
    graph = defaultdict(list)
    for emp, mgr in pairs:
        graph[emp].append(mgr)
        graph[mgr].append(emp)  # undirected: path can go up then down
    if start not in graph or target not in graph:
        return -1
    dist = {start: 0}  # doubles as the visited set
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if cur == target:
            return dist[cur]
        for nxt in graph[cur]:
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
    return -1


if __name__ == '__main__':
    pairs = [('Ann', 'Bob'), ('Cy', 'Bob'), ('Bob', 'Dee'), ('Eve', 'Fay')]
    print(distance(pairs, 'Ann', 'Cy'))   # 2
    print(distance(pairs, 'Ann', 'Dee'))  # 2
    print(distance(pairs, 'Ann', 'Ann'))  # 0
    print(distance(pairs, 'Ann', 'Eve'))  # -1
    print(distance(pairs, 'Ann', 'Zed'))  # -1
