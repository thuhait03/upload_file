import json
import csv
import os

class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0  # con
        j = 0  # cookie

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i


# -------------------------------------------------
# Đọc JSON (1 bộ test)
# -------------------------------------------------
def load_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["g"], data["s"]


# -------------------------------------------------
# Đọc CSV nhiều bộ test
# Format mỗi dòng:  "1,2,3;1,1"
# -------------------------------------------------
def load_from_csv_multi(path):
    all_tests = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if len(row) != 2:
                continue

            g_list = [int(x) for x in row[0].split(",")]
            s_list = [int(x) for x in row[1].split(",")]

            all_tests.append((g_list, s_list))

    return all_tests


# -------------------------------------------------
# CHẠY CHƯƠNG TRÌNH
# -------------------------------------------------
if __name__ == "__main__":
    file_path = "data455.csv"   # hoặc cookies.json

    if not os.path.exists(file_path):
        print("❌ File không tồn tại:", file_path)
        exit()

    s = Solution()

    # ------------------ JSON ------------------
    if file_path.endswith(".json"):
        g, s_list = load_from_json(file_path)
        print("Dữ liệu JSON:", g, s_list)

        result = s.findContentChildren(g, s_list)
        print("👉 Số trẻ hài lòng:", result)

    # ------------------ CSV ------------------
    elif file_path.endswith(".csv"):
        test_cases = load_from_csv_multi(file_path)

        print("=" * 80)
        print(f"{'STT':<5} {'G (greed factors)':<30} {'S (cookies)':<30} {'Kết quả':<10}")
        print("=" * 80)

        for idx, (g, s_list) in enumerate(test_cases, start=1):
            result = s.findContentChildren(g, s_list)

            print(f"{idx:<5} {str(g):<30} {str(s_list):<30} {result:<10}")

        print("=" * 80)

    else:
        print("❌ File không phải JSON hoặc CSV")
