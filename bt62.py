"""import csv
import math

def uniquePaths(m, n):
    return math.comb(m + n - 2, m - 1)

# Đọc file CSV
with open("data62.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    # In header bảng
    print(f"{'m':<5}{'n':<5}{'Kết quả':<10}")
    print("-" * 20)

    # In từng dòng dữ liệu
    for row in reader:
        m = int(row["m"])
        n = int(row["n"])
        result = uniquePaths(m, n)

        print(f"{m:<5}{n:<5}{result:<10}")
"""
import csv
def uni(m,n):
    a = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 or j==0:
                a[i][j]=1
            else:
                a[i][j]=a[i-1][j]+a[i][j-1]
    return a[m-1][n-1]


# Đọc file CSV
with open("data62.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    # In header bảng
    print(f"{'m':<5}{'n':<5}{'Kết quả':<10}")
    print("-" * 20)

    # In từng dòng dữ liệu
    for row in reader:
        m = int(row["m"])
        n = int(row["n"])
        result = uni(m, n)

        print(f"{m:<5}{n:<5}{result:<10}")
