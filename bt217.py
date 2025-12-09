"""import json
import csv
import os

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
def load_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["nums"]


def load_from_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            return [int(x) for x in row]  # chuyển chuỗi sang số


if __name__ == "__main__":
    # -------------------------------
    # CHỌN FILE ĐỂ TEST
    # -------------------------------
    file_path = "multildata.csv"   # đổi thành "nums.csv" nếu muốn

    if not os.path.exists(file_path):
        print("❌ File không tồn tại:", file_path)
        exit()

    # -------------------------------
    # TỰ PHÁT HIỆN LOẠI FILE
    # -------------------------------
    if file_path.endswith(".json"):
        nums = load_from_json(file_path)
        print("Đã load dữ liệu từ JSON:", nums)

    elif file_path.endswith(".csv"):
        nums = load_from_csv(file_path)
        print("Đã load dữ liệu từ CSV:", nums)

    else:
        print("❌ File không phải JSON hoặc CSV")
        exit()

    # -------------------------------
    # CHẠY KIỂM TRA TRÙNG LẶP
    # -------------------------------
    s = Solution()
    result = s.containsDuplicate(nums)
    print("👉 Kết quả containsDuplicate:", result)

import json
import csv
import os

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


def load_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["nums"]


def load_from_csv_single(path):
    Đọc 1 dòng CSV (bản cũ của bạn)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            return [int(x) for x in row]


def load_from_csv_multi(path):
    Đọc nhiều dòng CSV -> mỗi dòng là 1 list số
    all_rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            nums = [int(x) for x in row]
            all_rows.append(nums)
    return all_rows


if __name__ == "__main__":
    file_path = "multildata.csv"   # đổi thành file bạn muốn test

    if not os.path.exists(file_path):
        print("❌ File không tồn tại:", file_path)
        exit()

    s = Solution()

    # -------------------------------
    # Nếu là JSON → chỉ có 1 dữ liệu
    # -------------------------------
    if file_path.endswith(".json"):
        nums = load_from_json(file_path)
        print("Đã load dữ liệu từ JSON:", nums)
        print("👉 Kết quả containsDuplicate:", s.containsDuplicate(nums))

    # -------------------------------
    # Nếu là CSV → đọc nhiều dòng
    # -------------------------------
    elif file_path.endswith(".csv"):
        all_data = load_from_csv_multi(file_path)
        print("Đã load dữ liệu từ CSV (nhiều dòng):")
        
        for i, nums in enumerate(all_data, start=1):
            result = s.containsDuplicate(nums)
            print(f"Dòng {i}: {nums} -> {result}")

    else:
        print("❌ File không phải JSON hoặc CSV")"""
import json
import csv
import os

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


def load_from_csv_multi(path):
    """Đọc nhiều dòng CSV -> mỗi dòng là 1 list số"""
    all_rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            nums = [int(x) for x in row]
            all_rows.append(nums)
    return all_rows


if __name__ == "__main__":
    file_path = "multildata.csv"

    if not os.path.exists(file_path):
        print("❌ File không tồn tại:", file_path)
        exit()

    # Load CSV nhiều dòng
    all_data = load_from_csv_multi(file_path)

    s = Solution()

    # ---------------------------------------
    # IN BẢNG KẾT QUẢ ĐẸP – CĂN CỘT
    # ---------------------------------------
    print("=" * 70)
    print(f"{'STT':<5} {'Dữ liệu':<40} {'Kết quả':<10}")
    print("=" * 70)

    for i, nums in enumerate(all_data, start=1):
        result = s.containsDuplicate(nums)
        print(f"{i:<5} {str(nums):<40} {str(result):<10}")

    print("=" * 70)

