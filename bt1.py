
def two_Sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # maps value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
  
    raise ValueError("No two sum solution")

# Ví dụ kiểm thử
if __name__ == "__main__":
    print(two_Sum([2, 8, 11, 15], 17))    
    print(two_Sum([3, 2, 4], 7))         
    print(two_Sum([3, 3], 6))            

