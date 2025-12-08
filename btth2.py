class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""

        # Lấy chuỗi ngắn nhất để so sánh
        shortest = min(strs, key=len)

        # So sánh từng ký tự
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[:i]

        return shortest
# ---------------- DEMO CHẠY THỬ ----------------

s = Solution()

# Example 1
strs1 = ["flower", "flow", "flight"]
print("Input:", strs1)
print("Output:", s.longestCommonPrefix(strs1))   # fl

print("--------------------------")

# Example 2
strs2 = ["dog", "racecar", "car"]
print("Input:", strs2)
print("Output:", s.longestCommonPrefix(strs2))   # (empty string)

