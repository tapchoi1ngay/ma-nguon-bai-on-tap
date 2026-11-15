import subprocess

print("ĐANG BIÊN DỊCH bai35.cpp...\n")
subprocess.run(["g++", "bai35.cpp", "-o", "bai35.exe"])

# 6 test case bắt buộc của Bài 35
tests = ["30", "100", "1000", "10000", "100000", "1000000"]

print("KẾT QUẢ CHẠY 6 TEST BÀI 35:")
print("-" * 60)
for t in tests:
    result = subprocess.run([r".\bai35.exe"], input=t, text=True, capture_output=True)
    print(f"Đầu vào: n = {t:<8} | Kết quả in ra: {result.stdout.strip()}")
print("-" * 60)
