class Solution:
    def numMovesStonesII(self, stones):
        stones.sort()
        n = len(stones)

        # --- Tính max_moves ---
        max1 = stones[-1] - stones[1] + 1 - (n - 1)
        max2 = stones[-2] - stones[0] + 1 - (n - 1)
        max_moves = max(max1, max2)

        # --- Tính min_moves bằng sliding window ---
        min_moves = float('inf')
        i = 0

        for j in range(n):
            # Thu nhỏ cửa sổ sao cho window size <= n
            while stones[j] - stones[i] + 1 > n:
                i += 1

            # Số stone trong window
            stones_in_window = j - i + 1
            missing = n - stones_in_window

            # Trường hợp đặc biệt
            # Ví dụ dạng [3,4,5,6,10] → thiếu đúng 1 nhưng cần 2 moves
            if missing == 1 and stones[j] - stones[i] + 1 == n - 1:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, missing)

        return [min_moves, max_moves]
stones = [7, 4, 9]
s = Solution()
print(s.numMovesStonesII([7,4,9]))
