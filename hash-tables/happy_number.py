# LeetCode #202 - Happy Number
def is_happy(n):
    # every unhappy number falls into the cycle 4, 16, 37, 58, 89, 145, 42, 20, 4
    while n != 1 and n != 4:
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1


def is_happy_set(n):
    # safer version: a repeated value proves a cycle
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1


if __name__ == '__main__':
    for n in (1, 7, 19, 2, 4):
        print(n, is_happy(n), is_happy_set(n))
