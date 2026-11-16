# LeetCode #304 - Range Sum Query 2D (immutable)
class NumMatrix:
    def __init__(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        # extra zero row and column so border queries need no special cases
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix[r][c + 1]
                    + self.prefix[r + 1][c]
                    - self.prefix[r][c]
                )

    def sum_region(self, r1, c1, r2, c2):
        p = self.prefix
        return p[r2 + 1][c2 + 1] - p[r1][c2 + 1] - p[r2 + 1][c1] + p[r1][c1]


if __name__ == '__main__':
    m = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5],
                   [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(m.sum_region(2, 1, 4, 3))  # 8
    print(m.sum_region(1, 1, 2, 2))  # 11
    print(m.sum_region(1, 2, 2, 4))  # 12
    print(NumMatrix([[5]]).sum_region(0, 0, 0, 0))  # 5
