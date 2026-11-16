# LeetCode #1 - Two Sum
def two_sum(nums, target):
    # dict of value -> index; check if the complement was already seen
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 3], 6))          # [0, 1]
    print(two_sum([1, 2], 10))         # []
