import csv

"""def letterCombinations(digits):
    if not digits:
        return []

    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    res = []

    def backtrack(index, path):
        if index == len(digits):
            res.append("".join(path))
            return

        for ch in phone[digits[index]]:
            path.append(ch)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return res

def print_table(rows):
    col1 = 8   # digits
    col2 = 60  # results

    line = "+" + "-"*col1 + "+" + "-"*col2 + "+"
    print(line)
    print(f"| {'digits':<{col1-1}}| {'kết quả':<{col2-1}}|")
    print(line)

    for d, r in rows:
        result_str = ", ".join(r)

        print(f"| {d:<{col1-1}}| {result_str:<{col2-1}}|")

    print(line)

# Đọc CSV và chạy test
with open("data17.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    print(f"{'digits':<10}{'kết quả':<50}")
    print("-" * 60)

    for row in reader:
        digits = row["digits"].strip().replace('"', '')
        result = letterCombinations(digits)

        print(f"{digits:<10}{str(result):<50}")


rows = []

with open("data17.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        digits = row["digits"].strip().replace('"', '')
        combos = letterCombinations(digits)
        rows.append((digits, combos))

# In bảng ASCII đẹp
print_table(rows)"""



numb = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def sinh(idx, current, digits, res):
    if idx == len(digits):
        res.append(current)
        return

    letters = numb[int(digits[idx])]
    for c in letters:
        sinh(idx + 1, current + c, digits, res)

def letterCombinations(digits):
    if not digits:
        return []
    res = []
    sinh(0, "", digits, res)
    return res

# Đọc CSV và in kết quả
with open("data17.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    print(f"{'digits':<10}{'kết quả':<50}")
    print("-" * 60)

    for row in reader:
        digits = row["digits"].strip().replace('"', '')
        result = letterCombinations(digits)

        print(f"{digits:<10}{str(result):<50}")  # in đúng


