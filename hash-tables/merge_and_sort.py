# Reported style question: merge two lists of strings and sort several ways
def merge_and_sort(a, b):
    merged = set(a) | set(b)  # union removes duplicates
    return {
        'alphabetical': sorted(merged, key=str.lower),
        'by_length': sorted(merged, key=lambda s: (len(s), s)),
        'reverse': sorted(merged, reverse=True),
    }


if __name__ == '__main__':
    print(merge_and_sort(['pear', 'Apple'], ['fig', 'pear']))
    print(merge_and_sort([], []))
