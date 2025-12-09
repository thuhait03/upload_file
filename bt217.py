class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
s= Solution()
nums1 = [1, 2, 3, 1]
print("Test 1:", s.containsDuplicate(nums1)) 

nums2 = [1, 2, 3, 4]
print("Test 2:", s.containsDuplicate(nums2)) 

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print("Test 3:", s.containsDuplicate(nums3)) 