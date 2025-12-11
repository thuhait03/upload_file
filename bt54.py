from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    m, n = len(matrix), len(matrix[0])
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    res: List[int] = []

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1

        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1

    return res

if __name__ == "__main__":
    a1 = [[1,2,3],[4,5,6],[7,8,9]]
    print("a1:", spiralOrder(a1))

    """a2 = [[1,2,3,4,5],[6,7,8,9],[10,11,12,13,14,15]]
    print("a2:", spiralOrder(a2))"""

    a3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print("a3:", spiralOrder(a3))   # OK
