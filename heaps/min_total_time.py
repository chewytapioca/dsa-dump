# Custom heap practice: minimum total time
import heapq


def min_total_time(belt, storage):
    # only the distance from 0 matters
    heap = [abs(p) for p in belt]
    heapq.heapify(heap)
    total = 0
    for s in storage:
        d = abs(s)
        closest = heapq.heappop(heap)  # belt nearest to 0
        total += closest + d           # pickup leg + delivery leg
        heapq.heappush(heap, d)        # belt now sits at the storage position
    return total


if __name__ == '__main__':
    print(min_total_time([-3, 5], [2, -4, 1]))  # 16
