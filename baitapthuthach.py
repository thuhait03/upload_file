import json
import csv
import re

# --- Hàm validate ---
def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone: str) -> bool:
    pattern = r'^0\d{9}$'   # 10 số, bắt đầu bằng 0
    return re.match(pattern, phone) is not None


# --- 1. Đọc file JSON ---
with open("user.json", "r", encoding="utf-8") as f:
    users = json.load(f)

results = []

# --- 2. Validate từng user ---

for u in users:
    email_ok = is_valid_email(u["email"])
    phone_ok = is_valid_phone(u["phone"])

    results.append({
        "name": u["name"],
        "email": u["email"],
        "email_valid": "OK" if email_ok else "FAIL",
        "phone": u["phone"],
        "phone_valid": "OK" if phone_ok else "FAIL"
    })

# --- 3. Ghi file CSV output ---
with open("validate_result.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "email", "email_valid", "phone", "phone_valid"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("Đã xuất file validate_result.csv thành công!")
