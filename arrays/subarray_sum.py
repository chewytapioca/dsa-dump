# LeetCode #560 - Subarray Sum Equals K
def subarray_sum_brute(nums, k):
    # try every subarray with a running sum: O(n^2)
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1
    return count


def subarray_sum(nums, k):
    # prefix sums + dict: a subarray ends here if an earlier prefix == total - k
    prefix_count = {0: 1}
    total = 0
    count = 0
    for x in nums:
        total += x
        count += prefix_count.get(total - k, 0)
        prefix_count[total] = prefix_count.get(total, 0) + 1
    return count


if __name__ == '__main__':
    for fn in (subarray_sum_brute, subarray_sum):
        print(fn.__name__,
              fn([1, 1, 1], 2),   # 2
              fn([1, 2, 3], 3),   # 2
              fn([1, -1, 0], 0),  # 3
              fn([-1, -1, 1], 0)) # 1
