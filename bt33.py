import csv
import ast  # dùng để chuyển chuỗi "[4,5,6]" thành list

def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Nửa trái tăng chuẩn
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # Nửa phải tăng chuẩn
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1 

"""import csv
def arr(mang,chon):
    trai=0
    phai=len(mang)-1
    giua=int((phai+trai)/2)

    while True:
        print(trai,giua,phai)
        if chon==mang[trai]:
            return trai
        if chon==mang[phai]:
            return phai
        if chon==mang[giua]:
            return giua
        
        if trai==phai or trai==giua or phai == giua:
            return -1

        if chon<mang[giua]:
            if chon>mang[trai]:    
                phai=giua
                giua=int((phai+trai)/2)
            else:
                trai=giua
                giua=int((phai+trai)/2)
        else:
            if chon>mang[phai]:    
                phai=giua
                giua=int((phai+trai)/2)
            else:
                trai=giua
                giua=int((phai+trai)/2)
        


if __name__=='__main__':
    a=[17,18,19,20,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    chon=11
    print(arr(a,chon))"""
# Đọc file CSV
with open("data33.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    print(f"{'nums':<25}{'target':<10}{'kết quả':<10}")
    print("-" * 50)

    for row in reader:
        nums = ast.literal_eval(row["nums"])  # chuyển chuỗi thành list
        target = int(row["target"])
        result = search(nums, target)

        print(f"{str(nums):<25}{target:<10}{result:<10}")
