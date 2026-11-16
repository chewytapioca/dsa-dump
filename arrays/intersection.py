# LeetCode #349 - Intersection of Two Arrays
def intersection(nums1, nums2):
    # sets remove duplicates and give O(1) lookups
    return list(set(nums1) & set(nums2))


# Mock version: parse two lines of input, return sorted result
def parse(line):
    line = line.strip()
    return [int(x) for x in line.split()] if line else []


def intersect_sorted(a, b):
    return sorted(set(a) & set(b))


if __name__ == '__main__':
    print(sorted(intersection([1, 2, 2, 1], [2, 2])))  # [2]
    print(intersection([1], [2]))                      # []
    print(intersection([], [1]))                       # []
    print(intersect_sorted(parse('4 9 5 9'), parse('9 4 9 8 4')))  # [4, 9]
    print(intersect_sorted(parse(''), parse('1 2')))   # []
